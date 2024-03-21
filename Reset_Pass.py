import tkinter
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image



window = tkinter.Tk()
window.title("Reset Password")
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


# Entry
# Username
def username_enter(e):
    username_entry.delete(0,'end')
def username_leave(e):
    if username_entry.get()=='':
        username_entry.insert(0,'Username')
lbu_username = tkinter.Label(text ="USERNAME: ",font = ("Goudy old style",15,"bold"),fg = "Blue", bg = "black")
lbu_username.place(x = 90, y = 150)
username_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
username_entry.insert(0,"Username")
username_entry.bind("<FocusIn>",username_enter)
username_entry.bind("<FocusOut>",username_leave)
username_entry.place(x = 240, y = 150, width = 320, height = 30)

# Password
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

def pass_enter(e):
    password_entry.delete(0,'end')
def pass_leave(e):
    if password_entry.get()=='':
           password_entry.insert(0,'Password')
lbu_password = tkinter.Label(text ="PASSWORD: ",font = ("Goudy old style",15,"bold"),fg = "Blue", bg = "black")
lbu_password.place(x = 90, y = 200)
password_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
password_entry.insert(0,"Password")
password_entry.bind("<FocusIn>",pass_enter)
password_entry.bind("<FocusOut>",pass_leave)
password_entry.place(x = 240, y = 200, width = 320, height = 30)
password_entry.config(validatecommand = (validate_password),validate= "focusout")

#Re-Password
def repass_enter(e):
    re_password_entry.delete(0,'end')
def repass_leave(e):
    if re_password_entry.get()=='':
           re_password_entry.insert(0,'Password')
re_password = tkinter.Label(text ="RE PASSWORD",font = ("Goudy old style",15,"bold"),fg = "Blue", bg = "black")
re_password.place(x = 90, y = 250)
re_password_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
re_password_entry.insert(0,"Re-Password")
re_password_entry.bind("<FocusIn>",repass_enter)
re_password_entry.bind("<FocusOut>",repass_leave)
re_password_entry.place(x = 250, y = 250, width = 320, height = 30)

def rest():
    password = password_entry.get()
    password2 = re_password_entry.get()
    if password == password2:
        username = username_entry.get().strip()
        vals = (username,)
        select_query = "SELECT * FROM `user_detail` WHERE `username` = %s "
        c.execute(select_query, vals)
        user = c.fetchone()
        if user is not None:
            password = password_entry.get().strip()
            val=(password,username)
            select_query_password = "UPDATE `user_detail` set `password`= %s WHERE `username` = %s"
            c.execute(select_query_password,val)
            c.fetchone()
            connection.commit()
            messagebox.showinfo("Accepted", "Successfully")
            window.destroy()
            import Login
        else:
            messagebox.showwarning("Error", "Invalid Username")
    else:
        messagebox.showwarning("Incorrect","The password entered doesn't match")

def back():
    window.destroy()
    import Login

# Button
Okay = tkinter.Button(text="CONFIRM", bd=0, cursor="hand2", font=("Goudy old style", 20, "bold"), fg="#6162FF",bg="black", command = rest)
Okay.place(x=350, y=320, width=200, height=40)

bck = tkinter.Button(cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
bck.place(x = 90, y = 400, width = 100, height = 40)

window.mainloop()