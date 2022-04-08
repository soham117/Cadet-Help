from cgitb import text
# from curses.textpad import Textbox
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
import phonenumbers
from phonenumbers import geocoder

root = Tk()
root.title('Cadet Helps')
root.geometry("1024x495")
root.configure(background = 'sky blue')
# load = Image.open(r'Data/kdarfs.jpg')
render = ImageTk.PhotoImage(load)
background = Label(root, image = render)
background.place(x = 0, y = 0) 

logo = Image.open(r'Data/logo_jpg.jpg')
render_logo = ImageTk.PhotoImage(logo)
logo_label = Label(root, image = render_logo)
logo_label.place(x = 400, y = 350)

conn = sqlite3.connect('disaster_management.db')


#define a cursor
c = conn.cursor()
# c.execute("""CREATE TABLE disaster(
#                             Mob_Num text,
# 		Disaster_Info text)""")


def add():
    ad = Tk()
    ad.title('EMERGENCY')
    mobile_number = Label(ad, text = "Mobile Number : ", font = 10)
    mobile_number.grid(row = 0, pady = 2, sticky = W, padx = 5)
    disaster_info = Label(ad, text= "Disaster Information : ", font = 10)
    disaster_info.grid(row = 1, pady = 2, sticky=W, padx=5)



    mob_input = Entry(ad, width = 20, font = 10)
    mob_input.grid(row = 0, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    disaster_entry = Entry(ad, width = 20, font = 10)
    disaster_entry.grid(row = 1, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)

    def admit():
        if not mob_input.get():
            messagebox.showinfo("Info", "You need to enter the Mobile Number")
        else:
            if not disaster_entry.get():
                messagebox.showinfo("Info", "You need to enter the Detail")
                pass
                                        

        
            
        conn = sqlite3.connect('disaster_management.db')
        c = conn.cursor()
        c.execute("INSERT INTO disaster VALUES(:mobile_num, :dis_info)",
                        {
            'mobile_num' : mob_input.get(),
		    'dis_info' : disaster_entry.get()
	    })
        conn.commit()
        conn.close()
        mob_input.delete(0,END)
        disaster_entry.delete(0,END)
        messagebox.showinfo("Info", "Complaint Registered Successfully!")
        

    add_button = Button(ad, text = "Submit", bd = 3, width = 40, height = 2, command = admit)
    add_button.grid(row = 8, column = 0, columnspan = 2, pady = 10)

    trace_num = phonenumbers.parse(mob_input.get())


    ad.mainloop()
    



def other():
    ad = Tk()
    ad.title('EMERGENCY')
    mobile_number = Label(ad, text = "Mobile Number : ", font = 10)
    mobile_number.grid(row = 0, pady = 2, sticky = W, padx = 5)
    full_name = Label(ad, text= "Full Name : ", font = 10)
    full_name.grid(row = 1, pady = 2, sticky=W, padx=5)
    problem_desc = Label(ad, text = "Request : ", font = 10)
    problem_desc.grid(row=2, column=0, pady = 2, sticky = W, padx = 5)


    mob_input = Entry(ad, width = 20, font = 10)
    mob_input.grid(row = 0, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    disaster_entry = Entry(ad, width = 20, font = 10)
    disaster_entry.grid(row = 1, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    request_input = Text(ad, width=27, height=3)
    request_input.grid(row = 2, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)

                                        

        
            
    #     conn = sqlite3.connect('disaster_management.db')
    #     c = conn.cursor()
    #     c.execute("INSERT INTO disaster VALUES(:mobile_num, :dis_info)",
    #                     {
    #         'mobile_num' : mob_input.get(),
	# 	    'dis_info' : disaster_entry.get()
	#     })
    #     conn.commit()
    #     conn.close()
    #     mob_input.delete(0,END)
    #     disaster_entry.delete(0,END)
    # messagebox.showinfo("Info", "Complaint Registered Successfully!")
        

    add_button = Button(ad, text = "Submit", bd = 3, width = 40, height = 2)
    add_button.grid(row = 8, column = 0, columnspan = 2, pady = 10)

    ad.mainloop()


def sign():
    ad = Tk()
    ad.title('SIGN IN')
    fullmname = Label(ad, text = "Full Name : ", font = 10)
    fullmname.grid(row = 0, pady = 2, sticky = W, padx = 5)
    emailid = Label(ad, text= "Email ID : ", font = 10)
    emailid.grid(row = 1, pady = 2, sticky=W, padx=5)
    local = Label(ad, text = "Locality : ", font = 10)
    local.grid(row=2, pady = 2, sticky=W, padx=5)
    mobilenumber = Label(ad, text = "Mobile Number ", font = 10)
    mobilenumber.grid(row=3, pady = 2, sticky=W, padx=5)
    password_create = Label(ad, text= "Create Password : ", font = 10)
    password_create.grid(row=4, pady=2, sticky=W, padx=5)



    fullname_input = Entry(ad, width = 20, font = 10)
    fullname_input.grid(row = 0, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    emailid_input = Entry(ad, width = 20, font = 10)
    emailid_input.grid(row = 1, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    local_input = Entry(ad, width = 20, font = 10)
    local_input.grid(row = 2, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    mobilenumber_input = Entry(ad, width = 20, font = 10)
    mobilenumber_input.grid(row = 3, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    password_input = Entry(ad, width = 20, font = 10, show="*")
    password_input.grid(row = 4, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)

    conn = sqlite3.connect('disaster_management.db')
    c = conn.cursor()
    # c.execute("""CREATE TABLE signin(
    #                         Full_Name text,
    #                         Email_id text,
    #                         locality text,
    #                         mobile_number int,
    #                         password text)""")
    c.execute("INSERT INTO signin VALUES(:full_name, :email, :locality, :mob_number, :pass)",
                        {
            'full_name' : fullname_input.get(),
		    'email' : emailid_input.get(),
            'locality' : local_input.get(),
            'mob_number' : mobilenumber_input.get(),
            'pass' : password_input.get()
	    })

    
    conn.commit()
    conn.close()
        

    add_button = Button(ad, text = "Submit", bd = 3, width = 40, height = 2)
    add_button.grid(row = 5, column = 0, columnspan = 2, pady = 10)

    ad.mainloop()

def login():
    ad = Tk()
    ad.title('LOG IN')
    email_log = Label(ad, text= "Email ID : ", font = 10)
    email_log.grid(row = 0, pady = 2, sticky=W, padx=5)
    password_create = Label(ad, text= "Enter Password : ", font = 10)
    password_create.grid(row=1, pady=2, sticky=W, padx=5)

    email_input = Entry(ad, width = 20, font = 10)
    email_input.grid(row = 0, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)
    password_log = Entry(ad, width = 20, font = 10, show="*")
    password_log.grid(row = 1, column = 1, ipady = 5, pady = 2, padx = 8, sticky = W)

    submit_login = Button(ad, text = "Submit", bd = 3, width = 40, height = 2)
    submit_login.grid(row = 2, column = 0, columnspan = 2, pady = 10)

    
    conn = sqlite3.connect('disaster_management.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM signin WHERE password =  :passw",
                                {
                                    'passw' : password_log.get()
                                            
                                    })
        records = c.fetchall()
        conn.commit()
        conn.close()
    except:
        messagebox.showwarning("Incorrect Password", "Your Password Is Incorrect")
    else:
        messagebox.showinfo("Success", "You have successfully Logged in")



    



    ad.mainloop()






    

welcome = Label(root, text = "Cadet Helps | NCC | NDRF", font="verdana  20 bold",relief=SUNKEN,bg="blue",fg="white",padx=15)
welcome.place(x = 170, y = 10)

add_stud = Button(root, text = "EMERGENCY", bd = 3,  width = 20, height = 2, bg = 'red', fg = 'white', font = 5, command = add, activebackground = 'blue')
add_stud.place(x = 50, y = 200)

search_stud = Button(root, text = "POST-DISASTER HELP", bd = 3, width = 20, height = 2, command = other, bg = 'red', fg = 'white', font = 5)
search_stud.place(x = 300, y = 200)

sign_cadet = Button(root, text = "SIGN IN", bd = 3,  width = 20, height = 2, bg = 'red', fg = 'white', font = 5, command = sign, activebackground = 'blue')
sign_cadet.place(x = 550, y = 200)

login_cadet = Button(root, text = "LOG IN", bd = 3,  width = 20, height = 2, bg = 'red', fg = 'white', font = 5, command = login, activebackground = 'blue')
login_cadet.place(x = 800, y = 200)

conn.commit()
conn.close()

root.mainloop()