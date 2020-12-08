import pandas as pd 

from tkinter import *
from Admit import *

root = Tk()
v = IntVar()

root.title('Internship Portal')
Label(root, text="Full Name",fg='red').grid(row=0, column = 0)
e1 = Entry(root)
e1.grid(row=0, column = 1)

Label(root, text="Deaprtment",fg='red').grid(row=1, column = 0)
e2 = Entry(root)
e2.grid(row=1, column = 1)

Label(root, text="Email",fg='red').grid(row=2, column = 0)
e3 = Entry(root)
e3.grid(row=2, column = 1)

Label(root, text="University",fg='red').grid(row=3, column = 0)
e4 = Entry(root)
e4.grid(row=3, column = 1)

Label(root, text="University Score",fg='red').grid(row=4, column = 0)
e5 = Entry(root)
e5.grid(row=4, column = 1)

Label(root, text="Round 1 Score",fg='red').grid(row=5, column = 0)
e6 = Entry(root)
e6.grid(row=5, column = 1)

Label(root, text="Round 2 Score",fg='red').grid(row=6, column = 0)
e7 = Entry(root)
e7.grid(row=6, column = 1)

Label(root, text="Research (0 -> No ; 1 -> Yes)",fg='red').grid(row=7, column = 0)
e8 = Entry(root)
e8.grid(row=7, column = 1)

Label(root, text="Paper Presented",fg='red').grid(row=8, column = 0)
e9 = Entry(root)
e9.grid(row=8, column = 1)

''''
    column 1 --> University Score (total out of 5)
    column 2 --> Round 1 score (total out of 5)
    column 3 --> Round 2 score (total out of 5)
    column 4 --> Research (0 -> No ; 1 -> Yes)
    column 5 --> Paper Presented (upto n numbers {a person can publish or present n number of papaers})
'''''

def callback(): # Fuction for getting callback from user input. 
    print("Student Name:", e1.get())
    print("Department:", e2.get())
    print("Email:", e3.get())
    print("University:", e4.get())
    # print('Score:',e4.get())
    # print('Round 1 Score:',e5.get())
    # print('Round 2 Score:',e6.get())
    # print('Research:',e7.get())
    # print('Paper Presented:',e8.get())
    aList = []
    aList.append(e5.get())
    aList.append(e6.get())
    aList.append(e7.get())
    aList.append(e8.get())
    aList.append(e9.get())
    aList = list(map(float,aList))
    aList=[aList]
    print('Acceptance Mark:',aList)
    if (aList[0][0])<=5 and (aList[0][1])<=5 and (aList[0][2])<=5: # Won't accept negative value as input
        if aList[0][3]<=1:
            pre = lr.predict(aList) # Predicting the chance of acceptance
            for i in pre: # Iterating through loop, which comes out of a list
                if (i*100).round(2) < 70: # To check if the candidate secured more than 70 
                    print(f'Candiate not Selected with {(i*100).round(2)}%')
                elif (i*100).round(2) > 100:
                    print('You are over qualified.')
                else:
                    print(f'You are selected with {(i*100).round(2)}%')
        else:
            print('Wrong Input')
    else:
        print('Wrong Input')
    print('\n') # <---- To sepearate the students 

def res():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)


# Close button 
def close_window(): 
    root.destroy()

command= lambda: [f() for f in [callback, res]]

# Submit button
MyButton1 = Button(root, text="Submit", width=10, command=command)
MyButton1.grid(row=16, column=0)


# Quit Button
button = Button (root, text = "Good-bye.", command = close_window)
button.grid(row=16, column=1)

root.mainloop()