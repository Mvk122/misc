'''
makes a file called htmldump.txt and adds all videos on the front page 
of youtube to it
''' 
import requests 
import bs4
import re 
import lxml
import string

pagedata = requests.get("https://youtube.com")
cleanpagedata = bs4.BeautifulSoup(pagedata.text, 'lxml')
cleanpagedata2 = ''.join(filter(lambda x: x in string.printable, str(cleanpagedata)))
pattern = re.compile(r'watch\?v=...........')
matches = pattern.findall(cleanpagedata2)
videoset = set()
for match in matches:
    videoset.add('youtube.com/' + match)    
file = open("htmldump.txt" , "w+")
for video in videoset:
    file.write(video)
    file.write("\n")
file.close()
print("done")