import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = tk.Tk()
v = tk.IntVar()

tk.Label(root, text="Full Name").grid(row=0, column = 0)
e1 = tk.Entry(root)
e1.grid(row=0, column = 1)

tk.Label(root, text="Deaprtment").grid(row=1, column = 0)
e2 = tk.Entry(root)
e2.grid(row=1, column = 1)

tk.Label(root, text="University").grid(row=2, column = 0)
e3 = tk.Entry(root)
e3.grid(row=2, column = 1)

#Submit button
def callback(): # Fuction for getting callback from user input. 
    print("Student Name:", e1.get())
    print("Department:", e2.get())
    print("University:", e3.get())
    print ("Ah shit here we go again!!")
MyButton1 = Button(root, text="Submit", width=10, command=callback)
MyButton1.grid(row=16, column=0)

root.mainloop()