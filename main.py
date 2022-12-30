import tkinter
from tkinter import *
import os
import tkinter.filedialog
from PIL import Image, ImageTk


def centerScreen(w, h):

    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    return "%dx%d+%d+%d" % (w, h, x, y)

def eraseRoot():
    for widget in root.winfo_children():
        widget.destroy()

def selectFolder():
    global mangaDirectory
    mangaDirectory = tkinter.filedialog.askdirectory()
    print(mangaDirectory)

def main():

    eraseRoot()

    directoryFrame = LabelFrame(root, height=75, width=400)
    directoryFrame.place(x=50, y=50)

    selectDirectoryLabel = Label(directoryFrame, text='Browse for folder:')
    selectDirectoryLabel.place(x=5, y=5)

    selectDirectoryButton = Button(directoryFrame, image=selectDirectoryIcon, command=selectFolder)
    selectDirectoryButton.place(x=110, y=3)





root = Tk()
root.geometry(centerScreen(500, 500))
root.title('Manga Repacker')


selectDirectoryIcon=Image.open('images/icon.png')
selectDirectoryIcon=selectDirectoryIcon.resize((15,15))
selectDirectoryIcon=ImageTk.PhotoImage(selectDirectoryIcon)



main()

root.mainloop()