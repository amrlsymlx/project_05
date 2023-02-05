import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
#openpyxl needed to be installed into your machine. Enter {pip install openpyxl} into your terminal/command prompt 
import openpyxl

# --------------------------------------------------------------------------------------------------------
# enter_data function

def enter_data():

    accepted=accept_var.get()

    if accepted=="Accepted":
        firstName = first_name_entry.get()
        lastName = last_name_entry.get()

        if firstName and lastName:

            title = title_combobox.get()
            gender = gender_combobox.get()
            age = int(age_spinbox.get())

            if age >= 18 and age <= 40:

                nationality = nationality_combobox.get()
                courseNum = int(numcourses_spinbox.get())

                if courseNum >= 1 and courseNum <= 60:
                    semNum = numsemesters_combobox.get()
                    regStatus = reg_status_var.get()

                    #Append data in excel
                    sheet.append([firstName, lastName, title, gender, age, nationality, courseNum, semNum, regStatus])
                    workbook.save(filepath)

                    print("-------------Student Details-------------\n")
                    print("Name : "+title+" "+firstName+" "+lastName)
                    print("Gender : "+gender)
                    print("Age : "+str(age))
                    print("Nationality : "+nationality)
                    print("Registration Status : "+regStatus)
                    print("Number of Courses : "+str(courseNum))
                    print("Semester : "+semNum+"\n")
                    print("--------------Data Save Sucess!------------")
                else:
                    tkinter.messagebox.showwarning(title="Hold on!", message="You must have atleast 1 course (Max:60)")
            else:
                tkinter.messagebox.showwarning(title="Hold on!", message="Your age must be between 18 to 40 years old.")
        else:
           tkinter.messagebox.showwarning(title="Hold on!", message="First name and last name are required.") 
    else:
        tkinter.messagebox.showwarning(title="Hold on!", message="Please accept Terms & Conditions to proceed!")


# --------------------------------------------------------------------------------------------------------
# 01 root window

window = tkinter.Tk() 
window.title("Data Entry Form")
# --------------------------------------------------------------------------------------------------------
# Create or open excel file

# Data file path. Please enter your own file path.
filepath = "D:\python_data\data_entry_form\data.xlsx"

#Create if not exist
if not os.path.exists(filepath):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    heading = ["First Name", "Last Name", "Title", "Gender", "Age", "Nationality", "# Courses", "# Semesters", "Registration Status"]
    sheet.append(heading)
    workbook.save(filepath)

#Append if exist
workbook = openpyxl.load_workbook(filepath)
sheet = workbook.active

# --------------------------------------------------------------------------------------------------------
#03 Main Frame , no label, Parent = window

main_frame = tkinter.Frame(window)
# layout manager
# other layout .place() .grid()
main_frame.pack()

# --------------------------------------------------------------------------------------------------------
#  Frame - User Info , Parent = main_frame

user_info_frame = tkinter.LabelFrame(main_frame, text="User Information")
user_info_frame.grid(row=0, column=0)

# Widgets , Parent = user_info_frame
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Ms.","Dr.","Datuk.", "Tan Sri."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=40)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Others"])
gender_label.grid(row=2, column=1)
gender_combobox.grid(row=3, column=1)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Local", "Foreign"])
nationality_label.grid(row=2, column=2)
nationality_combobox.grid(row=3, column=2)

# --------------------------------------------------------------------------------------------------------
#  Frame - Courses Info , Parent = main_frame

courses_frame = tkinter.LabelFrame(main_frame, text="Courses Information")
courses_frame.grid(row=1, column=0, sticky="news")

# Widgets , Parent = courses_frame

registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                        variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# of Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=1, to=60)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# of Semesters")
numsemesters_combobox = ttk.Combobox(courses_frame, values=[1,2,3,4,5,6,7,8,9,10,11,12])
numsemesters_label.grid(row=0, column=2)
numsemesters_combobox.grid(row=1, column=2)

# --------------------------------------------------------------------------------------------------------
#  Frame - Accept T&C , Parent = main_frame

terms_frame = tkinter.LabelFrame(main_frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news")

# Widgets , Parent = terms_frame
accept_var=tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                    variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

# --------------------------------------------------------------------------------------------------------
# Button, Parent = main_frame

button = tkinter.Button(main_frame, text="Submit", command=enter_data)
button.grid(row=3, column=0, sticky="news")

# --------------------------------------------------------------------------------------------------------

# Padding between child of main_frame
for widget in main_frame.winfo_children():
    widget.grid_configure(pady=5, padx=10)

# Padding between child of user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Padding between child of courses_frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# --------------------------------------------------------------------------------------------------------




#02 run infinite number of loop so long as the app being executed
window.mainloop()