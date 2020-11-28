import tkinter 
from tkinter import *

# Designing the main window
top = tkinter.Tk()

# Name Input feild 
Label(top, text='First Name').grid(row=0) 
name = Entry(top)
name.grid(row=0, column=1)

top.mainloop()