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
lable.grid(row=0,column=0,columnspan=4)

list_images=[]
list_texts=[]

for i in range(2, 6):
    list_texts.append(data(f"{i}.txt"))
    image_path=None
    if(os.path.exists(f"{i}.jpg")):
        image_path=f"{i}.jpg"
    elif(os.path.exists(f"{i}.webp")):
        image_path=f"{i}.webp"
    image = Image.open(image_path)
    image = image.resize((150, 150))
    list_images.append(ImageTk.PhotoImage(image))

for i in range(len(list_images)):
    if(i==3):
        row_frame = Frame(root)
        Label(row_frame, image=list_images[i] ).pack()
        Label(row_frame, text=list_texts[i], justify=CENTER, wraplength=400 ).pack()
        row_frame.grid(row=1, column=1, sticky="ne", padx=15, pady=15)
    else:
        row_frame = Frame(root)
        Label(row_frame, image=list_images[i] ).pack()
        Label(row_frame, text=list_texts[i], justify=CENTER, wraplength=400 ).pack(padx=10)
        row_frame.grid(row=i+1, column=0, sticky="w", padx=20, pady=15)


root.mainloop()

