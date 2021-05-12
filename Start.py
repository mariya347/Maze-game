import tkinter as tk
import os

def callback():
     win.destroy()
     filename="Title1.py"
     os.system(filename)

win=tk.Tk()
win.title("A MAZE GAME")
#win.configure(bg="black")

image=tk.PhotoImage(file="Main_title.gif")
win.geometry("700x700")

label1=tk.Label(win,image=image)
label1.pack(side="top",fill="both",expand="yes")

button=tk.Button(label1,command=callback,text="PLAY",bd=30,bg="purple",font="helvitica 16 bold italic")
button.pack(side="bottom",pady=100)
label1.image=image

win.mainloop()
