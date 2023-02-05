import tkinter
from tkinter import ttk


# --------------------------------------------------------------------------------------------------------
# 01 root window

window = tkinter.Tk() 
window.title("Data Entry Form")

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
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Others"])
gender_label.grid(row=2, column=1)
gender_combobox.grid(row=3, column=1)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
natinality_combobox = ttk.Combobox(user_info_frame, values=["Local", "Foreign"])
nationality_label.grid(row=2, column=2)
natinality_combobox.grid(row=3, column=2)

# --------------------------------------------------------------------------------------------------------
#  Frame - Courses Info , Parent = main_frame

courses_frame = tkinter.LabelFrame(main_frame, text="Courses Information")
courses_frame.grid(row=1, column=0, sticky="news")

# Widgets , Parent = courses_frame

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# of Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# of Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="12")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

# --------------------------------------------------------------------------------------------------------
#  Frame - Accept T&C , Parent = main_frame

terms_frame = tkinter.LabelFrame(main_frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news")

# Widgets , Parent = terms_frame

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions")
terms_check.grid(row=0,column=0)

# --------------------------------------------------------------------------------------------------------
# Button, Parent = main_frame

button = tkinter.Button(main_frame, text="Submit")
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