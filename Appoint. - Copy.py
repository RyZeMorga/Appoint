
# ========================================================> Import all the necessary libraries
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import tkinter.simpledialog
import time
import sys
tries = 3

# ========================================================> Login system that locks app until password is correct
master = Tk()
master.withdraw()


def LoginWindow():
   print("Login Initiated!")
   #tk.Tk().withdraw() # HIDES MAIN APP
   global x
   x = tkinter.simpledialog.askstring("Password", "Enter password:", show = '*') # PASSWORD POP UP WINDOW
   LoginCheck()
   # IF STATEMENT FOR PASSWORD CHECK

def LoginCheck():
   global tries
   global x
   print('"' , x , '"' " was attempted") # Prints the password that was attempted!

   print(tries , "tries left")

   if tries == 0:
      print('Login Failed!') # PRINTS TO TERMINAL IF PASSWORD WRONG
      messagebox.showerror("Incorrect Password.","Your password is incorrect, you have been locked out.") # POP UP THAT TELLS YOU TO RESTART APP IF PASSWORD WRONG
      sys.exit() # CLOSES APP IF PASSWORD WRONG

   if tries <= 3:
      
      if x == 'admin': # SETS PASSWORD AS 'admin'
         print('Login Successful!') # PRINTS TO TERMINAL IF PASSWORD CORRECT
         master.deiconify()
      
      else:
         tries = tries - 1
         print('Login Failed! ') # PRINTS TO TERMINAL IF PASSWORD WRONG
         dialogue = ("Your password is incorrect, please try again. You have, " + str(tries) + " tries left")
         messagebox.showerror("Incorrect Password.", str(dialogue)) # POP UP THAT TELLS YOU TO RESTART APP IF PASSWORD WRONG
         LoginWindow()

LoginWindow()
         
# ========================================================> Making the master window + configuration

# Making the first window
# AKA the master window



# Making the title of the window
master.title("Appoint.")

# Setting the background colour of the window
master.configure(bg="black")


# Setting the resolution of the window
master.geometry('800x500')

# Changing the icon at the top of the window
master.iconbitmap ('CodeHub.ico')


# Adding a label to make the window pleasant
lbl = Label(master, text="Appoint", fg="DarkOrange1", bg="black", font=("Tw Cen MT", 50))
lbl.place(relx=0.5, rely=0.2, anchor=CENTER)


lbl1 = Label(master, text="Appointments Done", fg="DarkOrange1", bg="black", font=("Tw Cen MT", 20))
lbl1.place(relx=0.33, rely=0.3)


lbl2 = Label(master, text="Fast.", fg="white", bg="black", font=("Tw Cen MT", 20))
lbl2.place(relx=0.6, rely=0.3)

lbl3 = Label(master, text=".", fg="white", bg="black", font=("Tw Cen MT", 50))
lbl3.place(relx=0.629, rely=0.12)


# Adding a version level so it looks good
ver = Label(master, text="Version 1.5.2", font=("Arial", 12), bg="black", fg="DarkOrange1")
ver.place(relx=0.85, rely=0.98, anchor="sw")  


# ========================================================> Making the information boxes


# Define the informative button
def infoAppointments():
   messagebox.showinfo("Under Development","This is where your appointments will appear. Currently this section is under development.")

def infoSettings():
   messagebox.showinfo("Under Development","This is where your settings will appear. Currently this section is under development.")

# ========================================================> Making the colour change of buttons on hover

# Define functions for changing colour of buttons
def on_enter(e):
   btn.config(bg='DarkOrange1', fg="black")

def on_leave(e):
   btn.config(bg='grey11', fg='DarkOrange1')



def on_enter1(e):
   btn1.config(bg='DarkOrange1', fg="black")

def on_leave1(e):
   btn1.config(bg= 'grey11', fg='DarkOrange1')



def on_enter2(e):
   btn2.config(bg='DarkOrange1', fg="black")

def on_leave2(e):
   btn2.config(bg= 'grey11', fg='DarkOrange1')

# ========================================================> Making the appointments window


# Define functions for new window
def openNewWindow():

    # New window configuration
    newWindow = Toplevel(master)
    newWindow.title("Appointments")
    newWindow.geometry("800x500")
    newWindow.configure(bg="black")
    newWindow.iconbitmap ('CodeHub.ico')
 
    # A Label widget to show in toplevel
    Lbl1 = Label(newWindow, text ="Appointments", fg="DarkOrange1", bg="black", font=("Tw Cen MT", 40))
    Lbl1.place(relx=0.5, rely=0.12, anchor= CENTER)

    # A button to close the window
    close = Button(newWindow, text = "Close", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=newWindow.destroy)
    close.place(relx=0.5, rely=0.7, anchor=CENTER)

    # A button to display the appointments
    display = Button(newWindow, text = "Display Appointments", fg= "DarkOrange1", bg= "grey11", relief= "groove", font= ("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = openNewWindow2)
    display.place(relx=0.5, rely=0.6, anchor=CENTER)

    # A button to display information
    myInfo = Button(newWindow, text = "Information", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=infoAppointments)
    myInfo.place (relx=0.85, rely=0.02)
     


    # ========================================================> Making the database & connection


    # Create a database
    conn = sqlite3.connect("Appoint.db")

    # Create cursor
    c = conn.cursor()


    #If I need to create the table again in the database I can just remove all of the #'s and it will create a database
    # Create table
    ###c.execute("""CREATE TABLE appointments (
            ###app text,
            ###app_date text
            ###)""")
                                                                                                                                                                                                               





    # ========================================================> Making the submit function for the submit button
     
    def submit():




        # Create a database
        conn = sqlite3.connect("Appoint.db")

        # Create cursor
        c = conn.cursor()
        


        # Insert into table
        c.execute("INSERT INTO appointments VALUES (:app, :app_date)",
              {
                    'app': app.get(),
                    'app_date': app_date.get()
                })



        # Commit changes
        conn.commit()

        # Close Connection
        conn.close()
        
        
        # Clear the text boxes
        app.delete(0, END)
        app_date.delete(0, END)

        

    # ========================================================> Making the database

    

    
    # Creating text boxes

    app = Entry(newWindow, width=30)
    app.place (relx=0.5, rely=0.3, anchor=CENTER)

    app_date = Entry(newWindow, width=30)
    app_date.place (relx=0.5, rely=0.4, anchor=CENTER)

    # Creating text box labels

    app_label = Label(newWindow, text ="Appointment", fg="DarkOrange1", bg="black", font=("Arial", 12))
    app_label.place (relx=0.3, rely=0.3, anchor=CENTER)

    app_date_label = Label(newWindow, text ="Appointment Date", fg="DarkOrange1", bg="black", font=("Arial", 12))
    app_date_label.place (relx=0.3, rely=0.4, anchor=CENTER)

    # Creating submit button

    submit_btn = Button (newWindow, text="Add Record to Database", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground="#ba722d", activeforeground="white",  command=submit)
    submit_btn.place (relx=0.5, rely=0.5, anchor=CENTER)

    def on_enter(e):
        submit_btn.config(bg='DarkOrange1', fg="black")

    def on_leave(e):
        submit_btn.config(bg='grey11', fg='DarkOrange1')


    submit_btn.bind('<Enter>', on_enter)
    submit_btn.bind('<Leave>', on_leave)
    


    # Define function for changing the colour of the button
    def on_enter(e):
        myInfo.config(bg='DarkOrange1', fg="black")

    def on_leave(e):
        myInfo.config(bg='grey11', fg='DarkOrange1')
        
    
    def on_enter1(e):
        close.config(bg='DarkOrange1', fg="black")

    def on_leave1(e):
        close.config(bg='grey11', fg='DarkOrange1')


    def on_enter2(e):
       display.config(bg='DarkOrange1', fg="black")

    def on_leave2(e):
       display.config(bg='grey11', fg='DarkOrange1')

   

    # Button binds for changing colours
    myInfo.bind('<Enter>', on_enter)
    myInfo.bind('<Leave>', on_leave)
    
    close.bind('<Enter>', on_enter1)
    close.bind('<Leave>', on_leave1)

    display.bind('<Enter>', on_enter2)
    display.bind('<Leave>', on_leave2)


# ========================================================> Making the settings window

def openNewWindow1():
     
    newWindow1 = Toplevel(master)
    newWindow1.title("Settings")
    newWindow1.geometry("800x500")
    newWindow1.configure(bg="black")
    newWindow1.iconbitmap ('CodeHub.ico')
     
    Lbl1 = Label(newWindow1, text ="Settings", font=("Tw Cen MT", 40), fg="DarkOrange1", bg="black")
    Lbl1.place(relx=0.5, rely=0.3, anchor= CENTER)

    close = Button(newWindow1, text = "Close", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='white', command=newWindow1.destroy)
    close.place(relx=0.5, rely=0.6, anchor=CENTER)

    myInfo = Button(newWindow1, text = "Information", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground="#ba722d", activeforeground="white", command=infoSettings)
    myInfo.place (relx=0.85, rely=0.02)


    
    # Define function for changing the colour of the button
    def on_enter(e):
        myInfo.config(bg='DarkOrange1', fg="black")

    def on_leave(e):
        myInfo.config(bg='grey11', fg='DarkOrange1')
    

    def on_enter1(e):
        close.config(bg='DarkOrange1', fg="black")

    def on_leave1(e):
        close.config(bg='grey11', fg='DarkOrange1')

    # Button binds for changing colours
    myInfo.bind('<Enter>', on_enter)
    myInfo.bind('<Leave>', on_leave)

    close.bind('<Enter>', on_enter1)
    close.bind('<Leave>', on_leave1)


def openNewWindow2():

    # New window configuration
    newWindow2 = Toplevel(master)
    newWindow2.title("Query")
    newWindow2.geometry("800x500")
    newWindow2.configure(bg="black")
    newWindow2.iconbitmap ('CodeHub.ico')


    def query():
       conn = sqlite3.connect("Appoint.db")
       c = conn.cursor()

       c.execute("SELECT *, oid FROM appointments")
       records = c.fetchall()
       records = str(records) + "\n"
       

       #for record in records:
          
       print(records)

       query_label = Label (newWindow2, font=("Arial Bold", 8), bg="black", fg="DarkOrange1" , text= records)
       query_label.place (relx=0.5, rely=0.3, anchor= CENTER)
       print("Query success")
       
       
       

       conn.commit()
       conn.close()

    query()


 
   


   
# ========================================================> Making the buttons that open the other windows

# Making the buttons and what they do
btn = Button(master, text="Quit", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=master.destroy)

btn1 = Button(master , text="Settings", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = openNewWindow1)

btn2 = Button(master, text ="Appointments", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = openNewWindow)



# Button binds for changing colours
btn.bind('<Enter>', on_enter)
btn.bind('<Leave>', on_leave)

btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', on_leave1)

btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', on_leave2)



# Button placement
btn.place(relx=0.5, rely=0.75, anchor=CENTER)
btn1.place(relx=0.5, rely=0.65, anchor=CENTER)
btn2.place(relx=0.5, rely=0.55, anchor=CENTER)



master.mainloop()
