#!usr/bin/python 2.6
#-*- coding:UTF-8 -*-
import Tkinter as tk

#case
root=tk.Tk()

#title
root.title("Liu Yan Ban")

#label
label1=tk.Label(root,text="Hello!")
label2=tk.Label(root,text="Welcome to RC180603!")
label1.pack()
label2.pack()

#input your case
entry=tk.Entry(root,text=None,font=("Arial", 18))
entry.pack()

#frame
frame=tk.Frame(root)

#button2 def qingchu
def qingchu():
    entry.delete(0,100)

#button3 def guanbi
def guanbi():
    frame.pack_forget()

#button def fasong
def fasong():
    ai=entry.get()
    frame.pack()
    label3=tk.Label(frame,text=ai)
    label3.pack() 
   
#button
button2=tk.Button(root,text="Clear",command=qingchu)
button2.pack()
button=tk.Button(root,text="Send",command=fasong)
button.pack()
button3=tk.Button(root,text="Close",command=guanbi)
button3.pack()

#loop
root.mainloop()
