import tkinter as tk
from tkinter.constants import END
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Admit import *

class internship_portal(tk.Tk):
    def __init__(self, * args,** kwargs):
        tk.Tk.__init__(self,* args,** kwargs)
        global block
        block = tk.Frame(self)
        block.pack(side="top",fill="both",expand=True)
        block.grid_rowconfigure(0,weight=1)
        block.grid_columnconfigure(0,weight=1)
        self.frames = {}
        for F in (IntroPage,FirstPage):
            frame = F(block,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(IntroPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    
class IntroPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
    
        self.student_name = tk.Entry(self,width=30)
        self.student_name.grid(row=0,column=1,padx=10)
        self.student_name_label = tk.Label(self,text="Student Name:")
        self.student_name_label.grid(row=0,column=0)

        self.university_name = tk.Entry(self,width=30)
        self.university_name.grid(row=1,column=1,padx=10)
        self.university_name_label = tk.Label(self,text="University:")
        self.university_name_label.grid(row=1,column=0)

        self.department_name = tk.Entry(self,width=30)
        self.department_name.grid(row=2,column=1,padx=10)
        self.department_name_label = tk.Label(self,text="Department:")
        self.department_name_label.grid(row=2,column=0)

        self.email_address = tk.Entry(self,width=30)
        self.email_address.grid(row=3,column=1,padx=10)
        self.email_address_label = tk.Label(self,text="Email-ID:")
        self.email_address_label.grid(row=3,column=0)

        com = lambda: [f() for f in [self.callback,self.reset]] # This merge two functions print and reset the input feild.
        com2 = lambda: [f1() for f1 in [com,lambda : controller.show_frame(FirstPage)]]

        submit_button = tk.Button(self,text="Submit",command=com2)
        submit_button.grid(row=4,column=1)

        exit_button = tk.Button(self,text="Exit",command=self.quit)
        exit_button.grid(row=4,column=2)

    def callback(self): # Fuction for getting callback from user input. 
        print("Student Name:", self.student_name.get())
        print("University Name:", self.university_name.get())
        print("Department Name:", self.department_name.get())
        print("Email Address:", self.email_address.get())
        
    def reset(self):
        self.student_name.delete(0,END)
        self.university_name.delete(0,END)
        self.department_name.delete(0,END)
        self.email_address.delete(0,END)
    
    def callFunction(self):
        self.callback()

    def callReset(self):
        self.reset()    

class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        univ_score = tk.Entry(self,width=30)
        univ_score.grid(row=0,column=1,padx=10)
        univ_score_label = tk.Label(self,text="University Score:")
        univ_score_label.grid(row=0,column=0)

        apt_1 = tk.Entry(self,width=30)
        apt_1.grid(row=1,column=1,padx=20)
        apt_1_label = tk.Label(self,text="Aptitude-1:")
        apt_1_label.grid(row=1,column=0)

        apt_2 = tk.Entry(self,width=30)
        apt_2.grid(row=2,column=1,padx=20)
        apt_2_label = tk.Label(self,text="Aptitude-2:")
        apt_2_label.grid(row=2,column=0)

        research = tk.Entry(self,width=30)
        research.grid(row=3,column=1,padx=20)
        research_label = tk.Label(self,text="Research(No:0,Yes:1):")
        research_label.grid(row=3,column=0)

        paper_pres = tk.Entry(self,width=30)
        paper_pres.grid(row=4,column=1,padx=20)
        paper_pres_label = tk.Label(self,text="Paper-Presented:")
        paper_pres_label.grid(row=4,column=0)  

        def callback(): # Fuction for getting callback from user input. 
            print("University Score:", univ_score.get())
            print("Aptitude 1:", apt_1.get())
            print("Aptitude 2:", apt_2.get())
            print("Research:", research.get())
            print("Paper Presented:", paper_pres.get())

            aList = []
            aList.append(univ_score.get())
            aList.append(apt_1.get())
            aList.append(apt_2.get())
            aList.append(research.get())
            aList.append(paper_pres.get())
            aList = list(map(float,aList))
            aList=[aList]
            # print(aList)

            class1 = IntroPage(parent,controller)
            # student_1 = Student(class1.student_name.get(),class1.university_name.get(),class1.department_name.get(),class1.email_address.get(),aList)
            student_1 = Student(aList)

            # Calling the university class
            uni = University('VUB')
            uni.addStudent(student_1)

            
            # Creating a job portal
            job_1 = Intern('SDE',80)
            job_2 = Intern('Back End Dev',75)
            job_3 = Intern('Senior Full Stack Dev',90)
            job_4 = Intern('Junior Full Stack Dev',69)
            job_5 = Intern('Data Scientist Associate',88)

            # Assigning the job to a company
            company_1 = Company('Amazon')
            company_1.addIntern(job_1)
            company_1.addIntern(job_2)

            company_2 = Company('Tesla')
            company_2.addIntern(job_3)
            company_2.addIntern(job_4)
            company_2.addIntern(job_5)

            # Portal class
            p = Portal()
            p.addComapany(company_1)
            p.addComapany(company_2)

            # # Student Choice
            student_1.chooseIntern(company_1) 
            # student_2.chooseIntern(company_2) 
            uni.sort_students()
            uni.get_sort()
            # print('\n')
            company_1.accept_intern(uni)
            company_2.accept_intern(uni)
            uni.get_sort()
            # print('\n')
            print(student_1.get())
            # print(student_2.get())
            show = uni.get()
            print(show)

            if (aList[0][0])<=5 and (aList[0][1])<=5 and (aList[0][2])<=5: # Won't accept negative value as input
                if aList[0][3]<=1:
                    pre = lr.predict(aList) # Predicting the chance of acceptance
                    for i in pre: # Iterating through loop, which comes out of a list
                        if (i*100).round(2) < 70: # To check if the candidate secured more than 70 
                            print(f'Candiate not Selected with {(i*100).round(2)}%')
                        elif (i*100).round(2) > 100:
                            print('You are over qualified.')
                        else:
                            print(f'Selction accuracy is {(i*100).round(2)}%')
                else:
                    print('Wrong Input')
            else:
                print('Wrong Input')
        print('\n')

        
        def reset():
            univ_score.delete(0)
            apt_1.delete(0)
            apt_2.delete(0)
            research.delete(0)
            paper_pres.delete(0)
        
        com = lambda: [f() for f in [callback,reset]] # This merge two functions print and reset the input feild.
        # com2 = lambda: [f1() for f1 in [com,lambda : controller.show_frame(SecondPage)]]
        com2 = lambda: [f1() for f1 in [com,lambda : controller.show_frame(IntroPage)]]
        com3 = lambda: [f1() for f1 in [com,com2]]

        # previous_button = tk.Button(self,text="Previous",command=lambda: controller.show_frame(IntroPage))
        # previous_button.grid(row=5,column=0)

        submit_button = tk.Button(self,text="Submit",command=com2) 
        submit_button.grid(row=5,column=0)

        submit_button = tk.Button(self,text="Exit",command=self.quit)
        submit_button.grid(row=5,column=1)

''''
def create_plot():
    sns.set(style="white")

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 9))

    # Draw the heatmap with the mask and correct aspect ratio
    plt.title('Data Visualisation for Students points from Round 1 with Research',fontsize=15)
    sns.histplot(data=df,x='Round 1',hue='Research')
    return fig

    
class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.fig = create_plot()
        self.root = lambda:controller.show_frame(SecondPage)

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.root)  # A tk.DrawingArea.
        self.canvas.show()
        self.canvas.get_tk_widget().pack()
        self.submit_button = tk.Button(self,text="Exit",command=self.quit)
        self.submit_button.pack()

    def create_plot(self):
        sns.set(style="white")

        # Set up the matplotlib figure
        plt.figure(figsize=(10,8))
        # Draw the heatmap with the mask and correct aspect ratio
        plt.title('Data Visualisation for Students points from Round 1 with Research',fontsize=15)
        return sns.histplot(data=df,x='Round 1',hue='Research') 
'''''

app = internship_portal()
app.mainloop()