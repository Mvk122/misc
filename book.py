"""
Task 3.3
Designing a menu driven interface that will bla bla bla 
This program uses Tkinter (a python module) for its GUI 
Each book entry contains 
title, author, release date
"""
from tkinter import *
from tkinter import ttk

txtfilename = "bookcontents.txt"
def loadfile(nameoftextfile):
    with open(nameoftextfile , 'r') as f:
        contents = f.read().split('\n') # reads the file and puts each line of the text file into a new entry on the array
    books = []
    for book in contents:
        books.append(book.split(","))
    return books 


def writefile(nameoftextfile, books):
    with open(nameoftextfile, "w+") as f:
        for book in books:
            f.write(book[0] + "," + book[1] + "," + book[2] + "\n")

def addbook(author, title, lenght, books):
    assert type(author) == str
    assert type(title) == str 
    assert type(lenght) == int
    books.append([author , title, lenght])


def authorsearch(author, books):
    author = author.lower()
    returnlist = []
    for book in books:
        if book[0].lower() == author:
            returnlist.append(book[1])
    return returnlist


def searchwindow():
    def close_window():
        win1.destroy()

    global searchentry
    global books
    author = searchentry.get()
    results = authorsearch(author, books)
    if len(results) == 0:
        results = ["No books written by author %s" %(author)]

    win1 = Toplevel()
    titlelabel = Label(win1, text="Books by %s" %(author))
    titlelabel.pack()
    win1.geometry("200x300")
    for entry in results:
        Label(win1, text=entry).pack()
    button1 = Button(win1, text= "Close window", command= close_window)
    button1.pack()
    

def addbook():
    global txtfilename
    def submitbook():
        books.append([authorentry.get(), booktitleentry.get(), pagecountentry.get()])
        writefile(txtfilename, books)

    global books 
    win2 = Toplevel()
    titlelabel = Label(win2, text="Add a new book")
    
    booktitlelabel = Label(win2, text= "Book Title")
    booktitlelabel.pack()
    booktitleentry = Entry(win2)
    booktitleentry.pack()

    authorlabel = Label(win2, text= "Author name")
    authorlabel.pack()
    authorentry = Entry(win2)
    authorentry.pack()

    pagecount = Label(win2, text="Number of pages")
    pagecount.pack()
    pagecountentry = Entry(win2)
    pagecountentry.pack()

    submitbutton = Button(win2, text="Submit", command=submitbook)
    submitbutton.pack()


books = loadfile(txtfilename)
app = Tk()
app.title("Book App")
Title = Label(app, text="Books in the library:  ")
Title.pack()
app.geometry("500x500")

booklist = Listbox(app)
print(books)
for book in books:
    if type(book) == list():
        booklist.insert(END, book[1])
booklist.pack()

searchlabel = Label(app, text= "Search by author")
searchlabel.pack()
searchentry = Entry(app)
searchentry.pack()
searchbutton = Button(app, text="Search", command=searchwindow)
searchbutton.pack()

addbookbutton = Button(app, text="Add a new book", command=addbook)
addbookbutton.pack()

if __name__ == "__main__":
    app.mainloop()
