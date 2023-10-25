from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
from stegano import lsb
import os

root = Tk()
root.title("Stenography - Hide a Scret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    filename = filedialog.askopenfile(initialdir=os.getcwd(), title='Select Image File', filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All File", ".txt")))
    img = Image.open(filename, errors='ignore')
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img

def Hide():
    print("")

def Show():
    print("")

def save():
    print("")

Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# First Fame
f = Frame(root,bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Second Frame
f2 = Frame(root, bd=3, width=340, height=280,bg="white", relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=160, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=160, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
