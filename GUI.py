from tkinter import *
import requests
from bs4 import BeautifulSoup
import shutil



window = Tk()
window.title("Weebs R Us")

lbl = Label(window,text="Search for a Tag")
lbl.pack()

txtbox = Text(window,height=1,width=20)
txtbox.pack()

def listpop(entry):
    lstBox.delete(0,END)
    with open('tags.txt','r') as file:
        for i in file:
            tag = str(i[i.find(',')+1:len(i)-1])
            if txtbox.get("1.0","end-1c") in tag and tag != "tag" and 'Posts' not in tag:
                lstBox.insert(1,tag)
    print(entry)
    print('Searching')

btn = Button(window,text="Search")
btn.pack()
btn.bind('<Button-1>',listpop)

lstBox = Listbox(window)
lstBox.pack()

def img(selection):
    results = await Gelbooru.search_posts(tags=[tags], exclude_tags=[exclude])


btn2 = Button(window,text="Download")
btn2.pack()
btn2.bind('<Button-1>',img)

#btn.bind('<Return>',listpop())


window.mainloop()