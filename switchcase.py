def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

userinput = input("Enter a function to choose: ")
functiondict = {
    'a' : a,
    'b' : b,
    'c' : c
}
#functiondict[userinput] points to the function, adding () and any arguments to it will call the function
functiondict[userinput]()
