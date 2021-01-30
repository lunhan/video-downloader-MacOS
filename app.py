from tkinter import *
from tkinter.filedialog import askdirectory
import pytube

def selectPath():
    doc = askdirectory()
    path.set(doc)

def download():
    video_url = url.get()#get it from url
    dl_loc = path.get()
    try:
        yt = pytube.YouTube(video_url)
        video = yt.streams.first() #will download the lowest one
        video.download(dl_loc)
        note.config(fg="green", text="Video downloaded")
    except Exception as e:
        print(e)
        note.config(fg="red", text="Video cannot be downloaded")

#main ui
ui = Tk() #that's create a pop up windows
ui.title("youtube downloader")
#put some text in ui
Label(ui, text="Youtube Downloader", fg="red", font=(20)) .grid(sticky=N, padx=100, row=0)
#use grid to actually put it on screen, sticky=N center, 100 units space left&right
Label(ui, text="Url:", fg="light blue", font=(15)) .grid(sticky=W, row=1, pady=10)
#pady gives 10 units spaces to above
url = StringVar()#create a variable named url
path = StringVar()
#input
Entry(ui, width=30, textvariable=url).grid(sticky=E, pady=1, row=1)
Entry(ui, width=30, textvariable=path).grid(sticky=E, pady=1, row=2)
#button, command=download will cal def download
Button(ui, width=20, text="File", font=15, command=selectPath) .grid(sticky=W, row=2, pady=10)
Button(ui, width=20, text="Download", font=15, command=download) .grid(sticky=N, row=3, pady=10)
note = Label(ui, font=12)#we wanna give user if download is done or not
note.grid(sticky=N, pady=1, row=4)
ui.mainloop() #to make us see it
