import re
import tkinter
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image



window = tkinter.Tk()
window.title("Registration")
window.geometry('1000x600')
window.resizable(False,False)

#Database
connection = mysql.connector.connect( host='localhost',
                                      user = 'root',
                                      port = '3306',
                                      password = '1234#',
                                      database = 'carenginesystem')
c = connection.cursor()


#Background image
image_0 = Image.open('backgroundImage.jpg')
bg = ImageTk.PhotoImage(image_0)
lbl=tkinter.Label(window,image = bg)
lbl.place(x = 0,y = 0,relheight=1,relwidth=1)

#Title
registration = tkinter.Frame(bg="white")
registration.place(x=250, y=50, width=500, height=500)
tkinter.Label(registration,text ="REGISTRATION",font = ("Impact",35,"bold"),fg = "#6162FF", bg = "white").place(x = 100, y = 10)

# USERNAME
# Validation function to restrict the user's input
def validate_username():
    user_name =username_entry.get().strip()
    num_count = sum(1 for c in user_name if c.isnumeric())
    if len(user_name) < 6 or len(user_name) > 12:
        messagebox.showwarning("Warning","The Username must be of 6-12 characters")
        return False
    elif not num_count == 3:
        messagebox.showwarning("Warning","The Username must have 3 numbers")
        return False
    else:
        return True

validate_command_username = window.register(validate_username)

username = tkinter.Label(registration,text ="USERNAME:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
username.place(x = 10, y = 80)
username_entry = tkinter.Entry(registration,validate = 'focusout',font = ("Goudy old style",15,), bg = "#E7E6E6")
username_entry.place(x = 140, y = 80, width = 320, height = 30)
username_entry.config(validate="focusout",validatecommand=(validate_username))
# NAME
name = tkinter.Label(registration,text ="FULL NAME:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
name.place(x = 10, y = 120)
name_entry = tkinter.Entry(registration,font = ("Goudy old style",15,), bg = "#E7E6E6")
name_entry.place(x = 140, y = 120, width = 320, height = 30)

# PASSWORD
# Validation function to restrict the user's input
def validate_password():
    pass_word = password_entry.get().strip()
    if len(pass_word) < 6 or len(pass_word) > 18:
        messagebox.showwarning("Warning", "The Password must have 6-18 characters")
        return False
    elif not any(c.isupper() for c in pass_word):
        messagebox.showwarning("Warning", "The Password must have an uppercase")
        return False
    elif not any(c in "!@#$%^&*()-+=[{]}\|;:',<.>/?`~" for c in pass_word):
        messagebox.showwarning("Warning", "The Password must have a special key")
        return False
    elif not any(c.isdigit() for c in pass_word):
        messagebox.showwarning("Warning", "The Password must have a digit(s)")
        return False
    else:
        return True

validate_command_password = window.register(validate_password)

password = tkinter.Label(registration,text ="PASSWORD:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
password.place(x = 10, y = 160)
password_entry = tkinter.Entry(registration, show="*",font = ("Goudy old style",15,), bg = "#E7E6E6",)
password_entry.place(x = 170, y = 160, width = 290, height = 30)
password_entry.config(validatecommand = (validate_password),validate= "focusout")

# RE-PASSWORD
re_password = tkinter.Label(registration,text ="RE-PASSWORD:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
re_password.place(x = 10, y = 200)
re_pass = tkinter.Entry(registration,show="*",font = ("Goudy old style",15,), bg = "#E7E6E6")
re_pass.place(x = 180, y = 200, width = 280, height = 30)

# PHONE NUMBER
# Validation on phone number
def validate_phone_number():
    phone_no = phone_entry.get()
    pattern = r"\+254\d{9}$"
    if re.match(pattern, phone_no):
        return True
    else:
        messagebox.showwarning("Error","The Phone Should begin with +254 and the remaining 9 digits")
        return False

validate_command_phone_no = window.register(validate_phone_number)
phone_number = tkinter.Label(registration,text ="PHONE NUMBER:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
phone_number.place(x = 10, y = 280)
phone_entry = tkinter.Entry(registration,font = ("Goudy old style",15,), bg = "#E7E6E6")
phone_entry.place(x = 190, y = 280, width = 270, height = 30)
phone_entry.config(validatecommand = (validate_phone_number),validate= "focusout")


# GENDER
gender = tkinter.Label(registration,text ="GENDER:",font = ("Goudy old style",15,"bold"),fg = "Black", bg = "white")
gender.place(x = 10, y = 240)

#Radio button
gender_en = StringVar()
gender_en.set('Male')
male_radiobutton = tk.Radiobutton(registration, text ='Male', font =("Goudy old style",15,"bold"),bg = "white", fg = "Black",variable = gender_en, value='Male')
male_radiobutton.place(x = 170,y =240)
female_radiobutton = tk.Radiobutton(registration, text ='Female', font =("Goudy old style",15,"bold"),bg= "white", fg = "Black",variable = gender_en, value='Female')
female_radiobutton.place(x = 246,y =240)

def Log_in():
    window.destroy()
    import Login

def check_username(user_name):
    user_name = username_entry.get().strip()
    vals = (user_name,)
    select_query = "SELECT * FROM `user_detail` WHERE `username` = %s"
    c.execute(select_query,vals)
    user =c.fetchone()
    if user is not None:
        return True
    else:
        return False


def new_register():
    user_name = username_entry .get().strip()
    full_name = name_entry.get().strip()
    pass_word = password_entry.get().strip()
    repass_word = re_pass.get().strip()
    gnd = gender_en.get()
    phone_no = phone_entry.get()

    if len(user_name)>0 and len(full_name)>0 and len(pass_word)>0 and len(gnd)>0 and len(phone_no)>0:
        if check_username(user_name) == False:
                if pass_word == repass_word:
                   vals = (user_name,full_name,pass_word,gnd,phone_no)
                   insert_query = "INSERT INTO `user_detail`(`username`, `full_name`, `password`, `gender`, `phone_number`) VALUES(%s,%s,%s,%s,%s)"
                   c.execute(insert_query,vals)
                   connection.commit()
                   messagebox.showinfo("Register","Your account has been successfully registered")
                   window.destroy()
                   import OTP
                else:
                    messagebox.showwarning("Password", "Incorrect Password Confirmation")
        else:
            messagebox.showwarning("Duplicate Username", "The Username already Exists")
    else:
        messagebox.showwarning("Error","Incorrect Details")




#Button
register = tkinter.Button(registration,text ="REGISTER",bd = 0,cursor = "hand2",font = ("Goudy old style",20,"bold"),fg = "#6162FF", bg = "black",command =new_register)
register.place(x = 150, y =350 ,width = 200,height = 40 )

login_in = tkinter.Button(registration,text ="Already have an account? Log In",bd = 0,cursor = "hand2",font = ("Goudy old style",15,"bold"),fg = "#6162FF", bg = "white", command = Log_in)
login_in.place(x = 90, y = 400)

window.mainloop()




