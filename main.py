from tkinter import *
from pytube import YouTube


PATH = 'C:\\Users\\WSA\\PycharmProjects\\YouTube_Downloader\\'


root = Tk()
root.geometry('500x250')
root.resizable(False, False)

bg = PhotoImage(file = PATH + "images\\back.png")
canvas1 = Canvas(root, width=500, height=250)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

image_icon = PhotoImage(file= PATH + "images\\logo.png")
root.iconphoto(False, image_icon)
root.title('YouTube Video Downloader')

link = StringVar()

Label(root, text = 'Insert your link:', font='Helvetica 20 bold', bg='#f44033').place(x=145, y= 20)

link_enter = Entry(root, width=60,textvariable=link,justify=CENTER).place(x=32, y=120)


def Download():
    url = YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(PATH + 'videos\\')


Button(root, text = 'DOWNLOAD', font='Helvetica 16 bold', bg='#f44033', padx=2, command=Download).place(x=170, y=200)

root.mainloop()