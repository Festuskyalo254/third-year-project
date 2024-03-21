import tkinter
import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login")
window.geometry('1000x600')
window.resizable(False,False)

# connection to the Database
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


# Title
Frame_login = tkinter.Frame(bg="white")
Frame_login.place(x=250, y=100, width=500, height=400)
tkinter.Label(Frame_login,text =" Login ",font = ("Impact",35,"bold"),fg = "#6162FF", bg = "white").place(x = 180, y = 30)


# Username
def username_enter(e):
    username_entry.delete(0,'end')
def username_leave(e):
    if username_entry.get()=='':
           username_entry.insert(0,'Username')
lbu_user = tkinter.Label(Frame_login,text ="Username",font = ("Goudy old style",15,"bold"),fg = "grey", bg = "white")
lbu_user.place(x = 90, y = 140)
username_entry = tkinter.Entry(Frame_login,font = ("Goudy old style",15,), bg = "#E7E6E6")
username_entry.insert(0,"Username")
username_entry.bind("<FocusIn>",username_enter)
username_entry.bind("<FocusOut>",username_leave)
username_entry.place(x = 90, y = 170, width = 320, height = 35)

# Password
def password_enter(e):
    password_entry.delete(0,'end')
def password_leave(e):
    if password_entry.get()=='':
        password_entry.insert(0,'Password')

lbp_user = tkinter.Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
lbp_user.place(x=90, y=210)
password_entry = tkinter.Entry(Frame_login,show = "*", font=("Goudy old style", 15,), bg="#E7E6E6")
password_entry.insert(0,"Password")
password_entry.bind("<FocusIn>",password_enter)
password_entry.bind("<FocusOut>",password_leave)
password_entry.place(x=90, y=240, width = 320, height = 35)


def login_user():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username,password,)
    select_query = "SELECT * FROM `user_detail` WHERE `username` = %s and `password` = %s"
    c.execute(select_query,vals)
    user =c.fetchone()


    if user is not None:
        messagebox.showinfo("Welcome","Successfully LogIn")
        window.destroy()
        import dbInstead
    else:
        messagebox.showwarning("Error","Invalid Username or Password")

def forget():
    window.destroy()
    import OTP_2


# Button
forget_button = tkinter.Button(Frame_login,text ="Forget Password?",bd = 0,cursor = "hand2",font = ("Goudy old style",12,"bold"),fg = "#6162FF", bg = "white", command = forget)
forget_button.place(x = 90, y = 280)

login_button = tkinter.Button(Frame_login,cursor = "hand2",text ="Login",bd = 0,font = ("Goudy old style",15,),bg = "#6162FF", fg = "white",command = login_user)
login_button.place(x = 150, y = 320, width = 200, height = 40)

window.mainloop()