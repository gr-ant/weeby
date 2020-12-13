from tkinter import *
import requests
from bs4 import BeautifulSoup
import urllib.request
from tkinter.filedialog import asksaveasfile

window = Tk()
window.title("Weebs R Us")


lblapi = Label(window,text="API Key:")
lblapi.grid(column=1,row=2)

lbluserid = Label(window,text="User ID:")
lbluserid.grid(column=1,row=1)


txtapi = Text(window,height=1,width=15)
txtapi.grid(column=2,row=2)

txtuser = Text(window,height=1,width=15)
txtuser.grid(column=2,row=1)

lblSearch = Label(window,text="Search String:")
lblSearch.grid(column=1,row=3)

txtbox = Text(window,height=1,width=25)
txtbox.grid(column=2,row=3)


def save(a):
    files = [('All Files', '*.*')]

    string = txtbox.get("1.0","end-1c")
    api = txtapi.get("1.0","end-1c")
    user = txtuser.get("1.0","end-1c")


    response = requests.get('https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags='
                            + string.replace(' ','+')+'&api_key=' + api + '&user_id='+user)

    soup = BeautifulSoup(response.text,'html.parser')
    with open('parse.txt','w+',encoding="utf-8") as file:
        file.write(str(response.text))
    with open('parse.txt','r',encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
            img = (line[line.find('file_url')+10:line.find('" p',line.find('file_url')+3)])
            #filesave = asksaveasfile(filetypes=files, defaultextension=files)
            img_data = requests.get(img).content
            with open((str(count)+img[len(img)-5:len(img)]), 'wb+') as handler:
                handler.write(img_data)
        Message(window,"IMPORT COMPLETE")

    #file = asksaveasfile(filetypes=files, defaultextension=files)

btn = Button(window, text='Save')
btn.grid(column=3,row=3)
btn.bind('<Button-1>',save)

window.mainloop()