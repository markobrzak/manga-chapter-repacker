import tkinter
from tkinter import *
import os
import tkinter.filedialog
from PIL import Image, ImageTk
from tkinter import ttk


global mangaDirectoryPath
mangaDirectoryPath = ''

global mangaName
mangaName = ''

boldFont = 'Helvetica 9 bold'
regularFont = 'Helvetica 9'

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
    global mangaDirectoryPath
    mangaDirectoryPath = tkinter.filedialog.askdirectory()
    mangaLocationLabel.config(text=mangaDirectoryPath)

    global mangaName
    mangaName = (os.path.basename(mangaDirectoryPath))
    mangaNameRegular.config(text=mangaName)

    global repackButton
    repackButton.config(state=ACTIVE)


def main():

    eraseRoot()

    global mangaDirectoryPath

    directoryFrame = LabelFrame(root, height=120, width=600)
    directoryFrame.place(x=50, y=50)

    selectDirectoryLabel = Label(directoryFrame, text='Browse for folder:', font = boldFont)
    selectDirectoryLabel.place(x=5, y=5)

    selectDirectoryButton = Button(directoryFrame, image=selectDirectoryIcon, command=selectFolder)
    selectDirectoryButton.place(x=125, y=4)

    mangaDirectoryLabel = Label(directoryFrame, text='Manga directory location: ', font = boldFont)
    mangaDirectoryLabel.place(x=5, y=30)

    global mangaLocationLabel
    mangaLocationLabel = Label(directoryFrame, text = '', font=regularFont)
    mangaLocationLabel.place(x=155, y=30)

    mangaNameLabel = Label(directoryFrame, text='Manga name: ', font=boldFont)
    mangaNameLabel.place(x=5, y=55)

    global mangaNameRegular
    mangaNameRegular = Label(directoryFrame, text=mangaName, font=regularFont)
    mangaNameRegular.place(x=90, y=55)

    global repackButton
    repackButton = ttk.Button(directoryFrame, text='Repack', width=95, state=DISABLED)
    repackButton.place(x=5, y=80)


root = Tk()
root.geometry(centerScreen(700, 500))
root.title('Manga Repacker')


selectDirectoryIcon=Image.open('images/icon.png')
selectDirectoryIcon=selectDirectoryIcon.resize((15,15))
selectDirectoryIcon=ImageTk.PhotoImage(selectDirectoryIcon)



main()

root.mainloop()