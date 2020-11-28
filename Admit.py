# Importing the required package
import random
import pandas as pd 

# For data visualisation
import seaborn as sns
import matplotlib.pyplot as plt

# For machine learning model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# %matplotlib inline 

# Defining the student class
class Student:
    
    def __init__(self,name,dept,email,university,skillset): # <---- Constructor
        self.name = name
        self.dept = dept
        self.email = email
        self.university = university
        self.skillset = skillset
        self.choice = {}
    
    def get(self):
        return {'Student Name':self.name,'Department':self.dept ,'University':self.university ,'Email':self.email,'Skill set':self.skillset}
    
    def chooseIntern(self,company):
        comp = company.get()
        self.choice['Name'] = comp['Name']
        self.choice['Offer'] = random.choice(comp['Offers'])
        self.choice['Status'] = 'Waiting'
        print(self.choice)

# Defining the university class

class University:
    def __init__(self,name):
        self.name = name
        self.student_list = []
    
    def addStudent(self,student):
        self.student_list.append(student)
    
    def get(self):
        return {"University Name" : self.name,'Student List' : [i.get() for i in self.student_list]}

# Accessing the job portal

class Intern:
    def __init__(self,desc,skill,level):
        self.desc = desc
        self.skill = skill
        self.level = level
    
    def get(self):
        return {'desc':self.desc,'skill':self.skill,'Level':self.level}

class Company:
    # Getting the song object and placing it in album array 
    def __init__(self,company_name):
        self.company_name = company_name
        self.offer = [] 
    
    # Append a song to the album array
    def addIntern(self,intern):
        self.offer.append(intern)
        
    def get(self):
        temp = {'Name':self.company_name,'Offers':[]}
        for i in self.offer:
            temp['Offers'].append(i.get())
        return temp
    
class Portal:
    def __init__(self):
        self.portal = []
    
    def addComapany(self,company):
        self.portal.append(company)

    def getOffers(self):
        temp = {}
        for i in self.portal: # To display company
            comp = i.get()
            temp[comp['Name']] = []
            for j in comp['Offers']: # To dispaly the job offers
                temp[comp['Name']].append(j)
            
        return temp

# Predicting the model we upload

df = pd.read_csv('/Users/aneruthmohanasundaram/Documents/VUB/1/Advanced Programming Concepts /Project/accept.csv')
df.head()
# Removing the unwanted column in dataset
df = df.drop('Serial No.',axis=1)
    
# Performing Train test split method to train and test the data 
X = df[['University Score', 'Round 1', 'Round 2 ', 'Research','Paper Presented']]
y= df['Chance of Admit ']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
# test_size --> Spliting the test size as 60:40 ratio for train and test of our given dataset.abs
# random_state --> It'll decide the splitting of data into train and test indices in our case.(The number can be randomly described.)

# Intialising the model for our project
lr = LinearRegression()

# Model Fiting 
fit = lr.fit(X_train,y_train)

# Model Predicting
pre = lr.predict(X_test)

# Function to display all the result 

def dispaly():
    
    # Calling the student class
    student_1 = Student('Aneruth','MACS','ane1998@gmail.com','VUB',{'C' : 'Master','Python' : 'Intermediate'})
    student_2 = Student('Arun Daniel','MACS','arundanielk@gmail.com','VUB',{'C' : 'Intermediate','Python' : 'Master', 'Full stack' : 'Master'})
    # print(student_1.get())
    # print(student_2.get())

    # print('\n')

    # Calling the university class
    uni = University('Virje University of Brussels')

    uni.addStudent(student_1)
    # uni.addStudent(student_2)
    show = uni.get()
    print(show)

    # print('\n')

    # Creating a job portal
    job_1 = Intern('SDE','Python','Intermediate')
    job_2 = Intern('Back End Dev','Java','Master')
    job_3 = Intern('Senior Full Stack Dev','Full stack','Master')
    job_4 = Intern('Junior Full Stack Dev','C','Master')
    job_5 = Intern('Data Scientist Associate','Machine Learning','Beginner')

    # Assigning the job to a company
    company_1 = Company('Amazon')
    company_1.addIntern(job_1)
    company_1.addIntern(job_2)
    # print(c.get())

    print('\n')

    company_2 = Company('Tesla')
    company_2.addIntern(job_3)
    company_2.addIntern(job_4)
    company_2.addIntern(job_5)

    # Portsal class
    p = Portal()
    p.addComapany(company_1)
    p.addComapany(company_2)
    for k in p.getOffers():
        print(k,(p.getOffers()[k]),end='\n\n')

    # Student Choice
    student_1.chooseIntern(company_1)
    # student_2.chooseIntern(company_2)

    print('\n')

    # Chance of accepting the offer based on our model
    chance = [[23.5,7.5,5,1,0]] # We can change this number based on user input. By default the ML model accepts only in 2D array.
    
    ''''
    column 1 --> University Score (total out of 5)
    column 2 --> Round 1 score (total out of 5)
    column 3 --> Round 2 score (total out of 5)
    column 4 --> Research (0 -> No ; 1 -> Yes)
    column 5 --> Paper Presented (upto n numbers {a person can publish or present n number of papaers})
    '''''
    # To check if we gave the correct method of input 
    if (abs(chance[0][0])<=5) and (abs(chance[0][1])<=5) and (abs(chance[0][2])<=5): # Won't accept negative value as input
        if chance[0][3]<=1:
            pre = lr.predict(chance) # Predicting the chance of acceptance
            for i in pre: # Iterating through loop, which comes out of a list
                if (i*100).round(2) < 70: # To check if the candidate secured more than 70 
                    print('Candiate not Selected')
                elif (i*100).round(2) > 100:
                    print('You are over qualified.')
                else:
                    print(f'You are selected with {(i*100).round(2)}%')
        else:
            print('Wrong Input')
    else:
            print('Wrong Input')

dispaly()