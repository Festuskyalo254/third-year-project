import random
import tkinter
from tkinter import *
from PIL import ImageTk,Image
from twilio.rest import Client
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("450x500")
window.title("Verification")
window.resizable(False, False)
n = random.randint(1000,9999)


# Label
OTP_no = Label(text = "Verification",bd = 0,font = ("Goudy old style",20,"bold"),fg = "#6162FF", bg = "black")
OTP_no.grid(row=0,column=6,columnspan=2,pady=10,padx=10)


#Entry OTP
def otp_enter(e):
    OTP_number.delete(0,'end')
def otp_leave(e):
    if OTP_number.get()=='':
       OTP_number.insert(0,'Username')
OTP_number = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
OTP_number.insert(0,"OTP NUMBER")
OTP_number.bind("<FocusIn>",otp_enter)
OTP_number.bind("<FocusOut>",otp_leave)
OTP_number.grid(row=1,column=6,columnspan=2,pady=10,padx=10)

#Your Twilio phone number,Twilio Account SID and Auth Token
twilio_phone_number = +15076906258
account_sid = "AC424d8ff44ab9c210969c62c7c5848ff6"
auth_token = "b16a65e3b5a51038fd8abefb7990d7ec"
verify_sid = "VAb8ee0fe41d61fefdc45b781b6ee5199c"
verified_number = "+254114755673"
client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)



def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[random.randint(0,9)]
    return OTP

otp = generate_otp()


#Send OTP via SMS using Twilio
def resendOTP():
    client.messages.create(
         body  = 'Your OTP is ' + otp,
         from_ = +15076906258,
         to    = "+254114755673")


def checkOTP():
    userInput = OTP_number.get()
    if userInput == otp:
       messagebox.showinfo("showinfo", "Verification Success")
       window.destroy()
       import Reset_Pass
    else:
       messagebox.showwarning("showinfo", "wrong OTP")


def back():
    window.destroy()
    import Login


#submit button
submitButton = Button(text ="submit",border = 0,font=("Goudy old style",20,"bold"),fg = "White", bg = "#6162FF",command = checkOTP)
submitButton.grid(row=4,column =6,columnspan=2 ,pady=10,padx=10)

#back button
bck = tkinter.Button(cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
bck.place(x = 90, y = 460, width = 100, height = 40)
# Print the OTP
print('OTP:', otp)

window.mainloop()
