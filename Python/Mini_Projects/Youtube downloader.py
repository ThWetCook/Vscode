from tkinter import *
import pytube
from tkinter import messagebox

root=Tk()
root.geometry("500x250")
root.resizable(False,False)
root.title("YouTube Video Downloader")
root.config(bg='#D3D3D3')

def download():
    try:
        ytlink=link1.get()
        youtubelink=pytube.YouTube(ytlink)
        video=youtubelink.streams.get_highest_resolution()
        video.download()
        Result="Video Downloaded"
        messagebox.showinfo("Result",Result)
    except:
        Result="Invalid Link"
        messagebox.showerror("Result",Result)

def reset():
    link1.set("")

def Exit():
    root.destroy()

lb=Label(root,text="---YouTube Video Downlaoder---",font=('Arial,15,bold'),bg='#D3D3D3')
lb.pack(pady=15)
lb1=Label(root,text="YouTube Video URL :",font=('Arial,15,bold'),bg='#D3D3D3')
lb1.place(x=10,y=80)

link1=StringVar()
En1=Entry(root,textvariable=link1,font=('Arial,15,bold'))
En1.place(x=230,y=80)

btn1=Button(root,text="Download",font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=350,y=130)
btn2=Button(root,text="Reset",font=('Arial,10,bold'),bd=4,command=reset)
btn2.place(x=160,y=190)
btn3=Button(root,text=" Exit ",font=('Arial,10,bold'),bd=4,command=Exit)
btn3.place(x=250,y=190)

root.mainloop()
