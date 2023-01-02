import tkinter
from tkinter import *
import os
import tkinter.filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import shutil
import time
import numpy

global bufferPath
bufferPath = 'images/buffer.jpg'

global mangaDirectoryPath
mangaDirectoryPath = ''

global mangaChaptersPath
mangaChaptersPath = ''

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


def repack():


    startTime = time.time()

    
    global repackButton
    repackButton.config(state=DISABLED)

    global mangaChaptersPath

    mangaChaptersPath = mangaDirectoryPath + "/"
    print(mangaChaptersPath)

    # Put all full directory paths into a list
    listOfDir = []
    for file in os.listdir(mangaChaptersPath):
        d = os.path.join(mangaChaptersPath, file)
        if os.path.isdir(d):
            listOfDir.append(d)

    # Sort full path of directories
    listOfDir.sort(key = lambda x: float(x.rsplit(' ', 1)[1]))

    # Put all directory names from current directory into a list
    allD = os.listdir(mangaChaptersPath)

    # Get number of chapters
    # -4 because of 4 python files needed in current directory
    numberOfChapters = len(allD)

    # Rename directories to the wanted form
    for k in range(numberOfChapters-1, -1, -1):
        os.rename(listOfDir[k], mangaDirectoryPath + "/Chapter " + str(k+1))

    chapterRename.config(text='Renaming chapters ✓', font=boldFont)

    chapterRenameTime = (time.time() - startTime)

    chapterRenameTime = str(round(chapterRenameTime, 2)) + 's'

    chapterRTime.config(text=chapterRenameTime)


    startTime = time.time()

    listOfDir = []
    for file in os.listdir(mangaChaptersPath):
        d = os.path.join(mangaChaptersPath, file)
        if os.path.isdir(d):
            listOfDir.append(d)

    badDir = []
    for dir in listOfDir:
        dir_path = dir + "\\"
        fileCount = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                fileCount += 1
        print(dir, ': ', fileCount)
        if(fileCount <= 9):
            # Appends directories with less than 10 files in a list
            badDir.append(dir)

            # Adds needed buffers
            for l in range(fileCount+1, 10):
                shutil.copy(bufferPath, dir + "\\" + "0" + str(l) + ".jpg")
            shutil.copy(bufferPath, dir + "\\10.jpg")

            # Adds 0 in front of file names (e.g. 1.jpg -> 01.jpg)
            for m in range(fileCount+1):
                if(os.path.isfile(dir + "\\" + str(m) + ".jpg")):
                    os.rename(dir + "\\" + str(m) + ".jpg", dir + "\\0" + str(m) + ".jpg")
                elif(os.path.isfile(dir + "\\" + str(m) + ".png")):
                    os.rename(dir + "\\" + str(m) + ".png", dir + "\\0" + str(m) + ".png")
                elif(os.path.isfile(dir + "\\" + str(m) + ".webp")):
                    os.rename(dir + "\\" + str(m) + ".webp", dir + "\\0" + str(m) + ".webp")

    print("\n\nChapters with less than 10 pages:")

    for dir in badDir:
        print(dir)

    if(len(badDir) == 0):
        print("None found.")
    else:
        print(len(badDir), " chapters fixed.")

    check10.config(text='Fixing chapters with less than 10 pages ✓', font=boldFont)
    
    check10T = (time.time() - startTime)

    check10T = str(round(check10T, 2)) + 's'

    check10Time.config(text=check10T)



    startTime = time.time()

    numberOfChapters = len(next(os.walk(mangaChaptersPath))[1])
        
    # Makes folder for all files to be put into
    os.mkdir(mangaChaptersPath + mangaName + " - All Chapters")

    dirPath = mangaChaptersPath + mangaName + " - All Chapters/"


    i = 0

    for chapterNum in numpy.arange(1, numberOfChapters+1, 1):
        print(chapterNum)

        # addZero is used for cases where number of files in one chapter exceeds 100
        addZero = ""
        numberforRename = 10

        chapter = mangaChaptersPath + "Chapter " + str(chapterNum) + "/"

        # folder path
        dir_path = chapter
        fileCount = 0

        # Get number of files
        # Iterate directory
        for path1 in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path1)):
                fileCount += 1
        print('File Count:', fileCount)


        if(fileCount >= 100):
            addZero = "0"
            numberforRename = 100

        
        for k in range(fileCount, numberforRename-1, -1):
            if(os.path.isfile(chapter + str(k) + ".jpg")):
                os.rename(chapter + str(k) + ".jpg", dirPath + str(i+k) + ".jpg")
            elif(os.path.isfile(chapter + str(k) + ".png")):
                os.rename(chapter + str(k) + ".png", dirPath + str(i+k) + ".jpg")
            elif(os.path.isfile(chapter + str(k) + ".webp")):
                os.rename(chapter + str(k) + ".webp", dirPath + str(i+k) + ".jpg")

        i = i + 1

        for l in range(1, numberforRename):

            if(l>=10):
                addZero = ""
            if(os.path.isfile(chapter + "0" + addZero + str(l) + ".jpg")):
                os.rename(chapter + "0" + addZero + str(l) + ".jpg", dirPath + str(i) + ".jpg")
            elif(os.path.isfile(chapter + "0" + addZero + str(l) + ".png")):
                os.rename(chapter + "0" + addZero + str(l) + ".png", dirPath + str(i) + ".jpg")
            elif(os.path.isfile(chapter + "0" + addZero + str(l) + ".webp")):
                os.rename(chapter + "0" + addZero + str(l) + ".webp", dirPath + str(i) + ".jpg")
            i = i + 1

        if(fileCount >= 100):
            i = i + fileCount - 100
        else:
            i = i + fileCount - 10

        os.rmdir(chapter)

    renamePages.config(text='Renaming pages ✓', font=boldFont)
    
    renamePagesT = (time.time() - startTime)

    renamePagesT = str(round(renamePagesT, 2)) + 's'

    renamePagesTime.config(text=renamePagesT)

    startTime = time.time()


    all_chapters = mangaChaptersPath + mangaName + " - All Chapters/"

    number_of_files = len(os.listdir(all_chapters))

    start = -999
    end = 0


    while(number_of_files > 0):
        
        start = start + 1000

        if(number_of_files - 1000 <= 0):
            end = end + number_of_files
            os.mkdir(mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end))
            print("Folder created: ", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end))
            for k in range(start, end+1):
                if(os.path.isfile(all_chapters + str(k) + ".jpg")):
                    os.rename(all_chapters + str(k) + ".jpg", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".jpg")
                elif(os.path.isfile(all_chapters + str(k) + ".png")):
                    os.rename(all_chapters + str(k) + ".png", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".png")
                elif(os.path.isfile(all_chapters + str(k) + ".webp")):
                    os.rename(all_chapters + str(k) + ".webp", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".webp")

            break

        end = end + 1000

        os.mkdir(mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end))

        for k in range(start, end+1):
            if(os.path.isfile(all_chapters + str(k) + ".jpg")):
                os.rename(all_chapters + str(k) + ".jpg", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".jpg")
            if(os.path.isfile(all_chapters + str(k) + ".png")):
                os.rename(all_chapters + str(k) + ".png", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".png")
            if(os.path.isfile(all_chapters + str(k) + ".webp")):
                os.rename(all_chapters + str(k) + ".webp", mangaChaptersPath + mangaName + " " + str(start) + "-" + str(end) + "\\" + str(k) + ".webp")


        number_of_files = number_of_files - 1000

    os.rmdir(all_chapters)

    distributePages.config(text='Distributing pages ✓', font=boldFont)
    
    distributePagesT = (time.time() - startTime)

    distributePagesT = str(round(distributePagesT, 2)) + 's'

    distributePagesTime.config(text=distributePagesT)


def main():

    eraseRoot()

    global mangaDirectoryPath

    directoryFrame = LabelFrame(root, height=120, width=600)
    directoryFrame.place(x=50, y=50)

    selectDirectoryLabel = Label(directoryFrame, text='Browse for folder:', font = boldFont)
    selectDirectoryLabel.place(x=5, y=5)

    selectDirectoryButton = Button(directoryFrame, image=selectDirectoryIcon, command=selectFolder)
    selectDirectoryButton.place(x=120, y=4)

    directoryLocationLabel = Label(directoryFrame, text='Directory location: ', font = boldFont)
    directoryLocationLabel.place(x=5, y=30)

    global mangaLocationLabel
    mangaLocationLabel = Label(directoryFrame, text = '', font=regularFont)
    mangaLocationLabel.place(x=115, y=30)

    mangaNameLabel = Label(directoryFrame, text='Manga name: ', font=boldFont)
    mangaNameLabel.place(x=5, y=55)

    global mangaNameRegular
    mangaNameRegular = Label(directoryFrame, text='', font=regularFont)
    mangaNameRegular.place(x=90, y=55)

    global repackButton
    repackButton = ttk.Button(directoryFrame, text='Repack', width=95, state=DISABLED, command=repack)
    repackButton.place(x=7.5, y=80)

    stagesFrame = LabelFrame(root, height=300, width=600)
    stagesFrame.place(x=50, y=180)

    global chapterRename
    chapterRename = Label(stagesFrame, text='Renaming chapters ...', font=boldFont)
    chapterRename.place(x=5, y=5)

    global chapterRTime
    chapterRTime = Label(stagesFrame, text='', font=boldFont, justify=LEFT)
    chapterRTime.place(x=550, y=5)

    global check10
    check10 = Label(stagesFrame, text='Fixing chapters with less than 10 pages ...', font=boldFont)
    check10.place(x=5, y=25)

    global check10Time
    check10Time = Label(stagesFrame, text='', font=boldFont, justify=LEFT)
    check10Time.place(x=550, y=25)

    global renamePages
    renamePages = Label(stagesFrame, text='Renaming pages ...', font=boldFont)
    renamePages.place(x=5, y=45)

    global renamePagesTime
    renamePagesTime = Label(stagesFrame, text='', font=boldFont, justify=LEFT)
    renamePagesTime.place(x=550, y=45)

    global distributePages
    distributePages = Label(stagesFrame, text='Distributing pages ...', font=boldFont)
    distributePages.place(x=5, y=65)

    global distributePagesTime
    distributePagesTime = Label(stagesFrame, text='', font=boldFont, justify=LEFT)
    distributePagesTime.place(x=550, y=65)

root = Tk()
root.geometry(centerScreen(700, 525))
root.title('Manga Repacker')


selectDirectoryIcon=Image.open('images/icon.png')
selectDirectoryIcon=selectDirectoryIcon.resize((15,15))
selectDirectoryIcon=ImageTk.PhotoImage(selectDirectoryIcon)



main()

root.mainloop()