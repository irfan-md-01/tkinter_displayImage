from tkinter import *
from PIL import ImageTk, Image 
import os 

def data(x):
    f = open(f"{x}", "r")
    s=f.read()
    return s 

root = Tk()

root.geometry("1080x600")
root.title("My InfoGUI --From tkinter_practise")

lable = Label(text="According to our sources we came to know that --> ", anchor="center", bg="lightblue", font=("Arial", 16, "bold") ,height=2 )
lable.pack(fill=X,pady=15)


row_frame = Frame(root)
photo = Image.open("2.jpg")
img = ImageTk.PhotoImage(photo.resize((150, 150)))
image_frame = Frame(row_frame)
label = Label(image_frame, image=img )
label.pack()
image_frame.pack()

description_frame = Frame(row_frame)
description_frame.pack()
description_label = Label(description_frame, text=data("2.txt"),justify=CENTER, wraplength=500 )
description_label.pack(padx=10)
row_frame.pack(pady=15)
# ----------------------------------------

row_frame = Frame(root)
photo = Image.open("3.jpg")
img3 = ImageTk.PhotoImage(photo.resize((150, 150)))
image_frame = Frame(root)
image_frame.pack(padx=10)
label = Label(image_frame, image=img3 )
label.pack()

description_frame = Frame(root)
description_frame.pack()
description_label = Label(description_frame, text=data("3.txt"),justify=CENTER, wraplength=500 )
description_label.pack(padx=15)
row_frame.pack(pady=10)

root.mainloop()

