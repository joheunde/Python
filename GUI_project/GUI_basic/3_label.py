from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

lable1 = Label(root, text="안녕하세요")
lable1.pack()

photo = PhotoImage(file="gui_basic/img.png")
lable2 = Label(root, image=photo)
lable2.pack()

def change():
    lable1.config(text="또 만나요")
    
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    lable2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()