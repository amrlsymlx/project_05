import tkinter
from tkinter import ttk
from tkinter import messagebox

import sqlite3

# --------------------------------------------------------------------------------------------------------
#08 enter_data function (last part)

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
                    semNum = int(numsemesters_combobox.get())
                    regStatus = reg_status_var.get()

                    # Insert Data
                    data_insert_query = '''INSERT INTO Student_Data (title, firstname, lastname, gender, age,
                    nationality, registration_status, num_courses, num_semesters) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''
                    data_insert_tuple = (title, firstName, lastName, gender, age, nationality, regStatus, courseNum, semNum)

                    # cursor - mid-way between sqlite connection and the actual database
                    #execute all the queries and decide where everything is being inserted at what point in the database
                    cursor = conn.cursor()
                    cursor.execute(data_insert_query, data_insert_tuple)

                    conn.commit()
                    conn.close()

                    print("-------------Student Details-------------\n")
                    print("Name : "+title+" "+firstName+" "+lastName)
                    print("Gender : "+gender)
                    print("Age : "+str(age))
                    print("Nationality : "+nationality)
                    print("Registration Status : "+regStatus)
                    print("Number of Courses : "+str(courseNum))
                    print("Semester : "+str(semNum)+"\n")
                    print("--------------Data Save Success!------------")
                    tkinter.messagebox.showinfo(title="Success!", message="Data successfully recorded!")
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
# Create SQL table

conn = sqlite3.connect('data.db')
table_create_query ='''CREATE TABLE IF NOT EXISTS Student_Data
(title TEXT, firstname TEXT, lastname TEXT, gender TEXT, age INT,
nationality TEXT, registration_status TEXT, num_courses INT, num_semesters INT)
'''
conn.execute(table_create_query)

# --------------------------------------------------------------------------------------------------------
#02 Main Frame , no label, Parent = window

main_frame = tkinter.Frame(window)
# layout manager
# other layout .place() .grid()
main_frame.pack()

# --------------------------------------------------------------------------------------------------------
#03  Frame - User Info , Parent = main_frame

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
#04  Frame - Courses Info , Parent = main_frame

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
#05  Frame - Accept T&C , Parent = main_frame

terms_frame = tkinter.LabelFrame(main_frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news")

# Widgets , Parent = terms_frame
accept_var=tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                    variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

# --------------------------------------------------------------------------------------------------------
#06 Button, Parent = main_frame

button = tkinter.Button(main_frame, text="Submit", command=enter_data)
button.grid(row=3, column=0, sticky="news")

# --------------------------------------------------------------------------------------------------------
# 07
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


# run infinite number of loop so long as the app being executed
window.mainloop()