# import tkinter as tk
import pandas as pd
from tkinter import *
# from tkinter import tk
# from tkinter.ttk import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

root = Tk()
v = IntVar()

root.title('Internship Portal')
Label(root, text="Full Name",fg='red').grid(row=0, column = 0)
e1 = Entry(root)
e1.grid(row=0, column = 1)

Label(root, text="Deaprtment",fg='red').grid(row=1, column = 0)
e2 = Entry(root)
e2.grid(row=1, column = 1)

Label(root, text="University",fg='red').grid(row=2, column = 0)
e3 = Entry(root)
e3.grid(row=2, column = 1)

Label(root, text="Score",fg='red').grid(row=3, column = 0)
e4 = Entry(root)
e4.grid(row=3, column = 1)

''''
Machine Learning Model
'''''
df = pd.read_csv('/Users/aneruthmohanasundaram/Documents/VUB/1/Advanced Programming Concepts /Project/accept.csv')
df.head()
# Removing the unwanted column in dataset
df = df.drop('Serial No.',axis=1)
    
# Performing Train test split method to train and test the data 
''''
test_size --> Spliting the test size as 60:40 ratio for train and test of our given dataset.abs
random_state --> It'll decide the splitting of data into train and test indices in our case.(The number can be randomly described.)
'''''
X = df[['University Score', 'Round 1', 'Round 2 ', 'Research','Paper Presented']]
y= df['Chance of Admit ']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Intialising the model for our project
lr = LinearRegression()

# Model Fiting 
fit = lr.fit(X_train,y_train)

# Model Predicting
pre = lr.predict(X_test)

''''
Machine Learning Model Ends here
'''''

#Submit button
def callback(): # Fuction for getting callback from user input. 
    print("Student Name:", e1.get())
    print("Department:", e2.get())
    print("University:", e3.get())
    print('Score:',e4.get())
    # chance = [[3.5,3.5,3.5,1,4]] # User Manually enters the input for a student, it may change to hardcode values 
    # if (abs(chance[0][0])<=5) and (abs(chance[0][1])<=5) and (abs(chance[0][2])<=5): # Won't accept negative value as input
    #     if chance[0][3]<=1:
    #         pre = lr.predict(chance) # Predicting the chance of acceptance
    #         for i in pre: # Iterating through loop, which comes out of a list
    #             if (i*100).round(2) < 70: # To check if the candidate secured more than 70 
    #                 print('Candiate not Selected')
    #             elif (i*100).round(2) > 100:
    #                 print('You are over qualified.')
    #             else:
    #                 print(f'You are selected with {(i*100).round(2)}%')
    #     else:
    #         print('Wrong Input')
    # else:
    #     print('Wrong Input')
    # print ("Ah shit here we go again!!")

# Reset feature after inout entered 
def res():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


# Close button 
def close_window(): 
    root.destroy()

command= lambda: [f() for f in [callback, close_window]]

# Submit button
MyButton1 = Button(root, text="Submit", width=10, command=command)
MyButton1.grid(row=16, column=1)


# # Quit Button
# button = Button (root, text = "Good-bye.", command = close_window)
# button.grid(row=16, column=2)

root.mainloop()