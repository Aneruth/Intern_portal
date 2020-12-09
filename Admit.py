# Importing the required package
import random
from numpy.core.fromnumeric import sort
from numpy.lib.function_base import append
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
    
    def __init__(self,name,dept,email,university,chance): # <---- Constructor
        self.name = name
        self.dept = dept
        self.email = email
        self.university = university
        self.chance = chance
        self.choice = {}
    
    def get(self):
        return {'Student Name':self.name,'Department':self.dept ,'University':self.university ,'Email':self.email,'Chance':self.chance,'Choice':self.choice}
    

    def chooseIntern(self,company):
        comp = company.get()
        self.choice['Name'] = comp['Name']
        self.choice['Offer'] = random.choice(comp['Offers'])
        self.choice['Status'] = 'Waiting'
        # print(self.choice)

# Defining the university class

class University:
    def __init__(self,name):
        self.name = name
        self.student_list = []
        self.sort_stu = {'Accepted':{},'Waiting':{}}
    
    def addStudent(self,student):
        self.student_list.append(student)
    
    def get(self):
        return {"University Name" : self.name,'Student List' : [i.get() for i in self.student_list]}
    
    def get_sort(self):
        # print(self.sort_stu)
        temp = {}
        for i in self.sort_stu:
            temp[i] = {}
            for j in self.sort_stu[i]:
                temp[i][j] = []
                for k in self.sort_stu[i][j]:
                    temp[i][j].append(k.get())
        print(temp)
            
    
    def sort_students(self):
        for i in self.student_list:
            stu = i.get()
            if stu['Choice']['Status'] == 'Waiting':
                if self.sort_stu['Waiting'].get(stu['Choice']['Name']) == None:
                    self.sort_stu['Waiting'][stu['Choice']['Name']] = []
                self.sort_stu['Waiting'][stu['Choice']['Name']].append(i) # Adding Student to the company list inside the waiting list
            else:
                if self.sort_stu['Accepted'].get(stu['Choice']['Name']) == None:
                    self.sort_stu['Accepted'][stu['Choice']['Name']] = []
                self.sort_stu['Accepted'][stu['Choice']['Name']].append(i) # Adding Student to the company list inside the Accepted list
       # print(self.sort_stu)

# Accessing the job portal

class Intern:
    def __init__(self,desc,threshold):
        self.desc = desc
        self.threshold = threshold 
        
    
    def get(self):
        return {'desc':self.desc,'Threshold':self.threshold}

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
    
    def accept_intern(self,university):
        if self.company_name in university.sort_stu['Waiting']:
            stu_list = university.sort_stu['Waiting'][self.company_name][:]
            # print(stu_list['Waiting'][self.company_name])
            for i in stu_list:
                stu = i.get()
                threshold = stu['Choice']['Offer']['Threshold']
                chance = stu['Chance']

                pre = lr.predict(chance) # Predicting the chance of acceptance
                # # for j in pre: # Iterating through loop, which comes out of a list
                #     # print(stu_list['Waiting'][self.company_name])
                #     # print(j)
                if (pre[0]*100).round(2) < threshold: # To check if the candidate secured more than 70 
                    stu['Choice']['Status'] = 'Rejected'
                    university.sort_stu['Waiting'][self.company_name].remove(i)
                elif (pre[0]*100).round(2) > 100:
                    stu['Choice']['Status'] = 'Rejected'
                    university.sort_stu['Waiting'][self.company_name].remove(i)
                else:
                    stu['Choice']['Status'] = 'Accepted'
                    university.sort_stu['Waiting'][self.company_name].remove(i)
                    if university.sort_stu['Accepted'].get(self.company_name) == None:
                        university.sort_stu['Accepted'][self.company_name] = [] 
                    university.sort_stu['Accepted'][self.company_name].append(i) # Adding Student to the company list inside the Accepted list
                #     # print(f'You are selected with {(i*100).round(2)}%')

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

######################################### Machine Learning Model Starts 
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
######################################### Machine Learning Model Ends