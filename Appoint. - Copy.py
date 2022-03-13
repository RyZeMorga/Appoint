
# ========================================================> Import all the necessary libraries
from tkinter import *
from tkinter import messagebox
import tksheet
import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.simpledialog
import time
import sys
from tkcalendar import *
tries = 3

conn = sqlite3.connect("Appoint.db")
c = conn.cursor()
# Create a database
try:
   c.execute("SELECT * FROM appointments")
except:
   c = conn.cursor()
   c.execute("""CREATE TABLE appointments (
            [id] INTEGER PRIMARY KEY,
            [firstname] TEXT NOT NULL,
            [surname] TEXT NOT NULL,
            [app_date] TEXT NOT NULL,
            [app_type] TEXT NOT NULL
            )""")
   conn.commit()
   values = [(1, "Check firstname", "Check surname", "Check app_date", "Check app_type")]
   sql = "INSERT INTO appointments VALUES (?, ?, ?, ?, ?)"
   conn.executemany(sql, values)
   conn.commit()

# Create cursor


# ========================================================> Login system that locks app until password is correct
master = Tk()
global newWindow
#newWindow = Toplevel(master)
newWindow1 = Toplevel(master)
newWindow2 = Toplevel(master)
master.withdraw()
#newWindow.title("Appointments")
#newWindow.geometry("800x500")
#newWindow.configure(bg="black")
#newWindow.iconbitmap ('CodeHub.ico')
#newWindow.withdraw()
newWindow1.withdraw()
newWindow2.withdraw()

def constant_bt(target, previous):
   rtrn = tk.Button(target, text = "⏎", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='white', command = lambda: [target.withdraw(), previous.deiconify()])
   rtrn.place(x=10, y=10)

   def on_enter(e):
        rtrn.config(bg='DarkOrange1', fg="black")

   def on_leave(e):
        rtrn.config(bg='grey11', fg='DarkOrange1')

   rtrn.bind('<Enter>', on_enter)
   rtrn.bind('<Leave>', on_leave)

#constant_bt(master)

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

# This removes the option to maximize the window
master.resizable(0,0)


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
    global newWindow
    newWindow = Toplevel(master)
    newWindow.title("Appointments")
    newWindow.geometry("800x500")
    newWindow.configure(bg="black")
    newWindow.iconbitmap ('CodeHub.ico')
    newWindow.resizable(0,0)
    constant_bt(newWindow, master)


    def my_upd(): # Triggered on Button Click
       show_date.config(text=cal.get_date()) # Read and display date

    # Calendar picker for date

    cal = Calendar(newWindow, selectmode = 'day', year = 2022, month= 3)
    cal.place(relx= 0.65, rely= 0.5)


    # Getting the date

    def grab_date():
       date.config(text= cal.get_date())

    

    show_date=tk.Label(newWindow,text='Pick a date.',bg='yellow')  # Label to display date
    show_date.place(relx= 0.65, rely= 0.2)

    get_date=tk.Button(newWindow,text='Read', command=lambda:my_upd())
    get_date.place(relx= 0.65, rely= 0.3)
    
    
    # A Label widget to show in toplevel
    Lbl1 = Label(newWindow, text ="Appointments", fg="DarkOrange1", bg="black", font=("Tw Cen MT", 40))
    Lbl1.place(relx=0.5, rely=0.12, anchor= CENTER)

    # A button to close the window
    close = Button(newWindow, text = "Close", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=newWindow.destroy)
    close.place(relx=0.5, rely=0.9, anchor=CENTER)

    # A button to display the appointments
    display = Button(newWindow, text = "Display Appointments", fg= "DarkOrange1", bg= "grey11", relief= "groove", font= ("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = lambda: [newWindow.withdraw(), openNewWindow2()])
    display.place(relx=0.5, rely=0.8, anchor=CENTER)

    # A button to display information
    myInfo = Button(newWindow, text = "Information", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=infoAppointments)
    myInfo.place (relx=0.85, rely=0.02)
     

    # ========================================================> Making the submit function for the submit button
     
    def submit():




        # Create a database
        conn = sqlite3.connect("Appoint.db")

        # Create cursor
        global c
        c = conn.cursor()

        print(firstname.get(), len(surname.get()), app_date.get(), app_type.get())

        if len(firstname.get()) == 0 or len(surname.get()) == 0 or len(app_date.get()) == 0 or len(app_type.get()) == 0:
           messagebox.showinfo("Appoint - Sponsored by EasiStock | Error", "Please enter a value.")
           return 0
        

        # Insert into table
        #try:
        c.execute("INSERT INTO appointments VALUES (?, ?, ?, ?, ?)", [None, firstname.get(), surname.get(), app_date.get(), app_type.get()])
        messagebox.showinfo("Appoint - Sponsored by EasiStock", "Data has been succesfully added.")
           #return 1
        #except:
           #messagebox.showerror("Appoint - Sponsored by EasiStock | Error", "Unknown Error.")
           #return 0



        # Commit changes
        conn.commit()

        # Close Connection        
        
        # Clear the text boxes
        firstname.delete(0, END)
        surname.delete(0, END)
        app_date.delete(0, END)
        app_type.delete(0, END)

        

    # ========================================================> Making the database

       
    # Creating text boxes
    global firstname
    firstname = Entry(newWindow, width=30)
    firstname.place (relx=0.5, rely=0.3, anchor=CENTER)

    global surname
    surname = Entry(newWindow, width=30)
    surname.place (relx=0.5, rely=0.4, anchor=CENTER)

    global app_date
    app_date = Entry(newWindow, width=30)
    app_date.place (relx=0.5, rely=0.5, anchor=CENTER)

    global app_type
    app_type = Entry(newWindow, width=30)
    app_type.place (relx=0.5, rely=0.6, anchor=CENTER)

    # Creating text box labels

    firstname_label = Label(newWindow, text ="First Name", fg="DarkOrange1", bg="black", font=("Arial", 12))
    firstname_label.place (relx=0.331, rely=0.3, anchor=CENTER)
    
    surname_label = Label(newWindow, text ="Surname", fg="DarkOrange1", bg="black", font=("Arial", 12))
    surname_label.place (relx=0.336, rely=0.4, anchor=CENTER)

    app_date_label = Label(newWindow, text ="Appointment Date", fg="DarkOrange1", bg="black", font=("Arial", 12))
    app_date_label.place (relx=0.3, rely=0.5, anchor=CENTER)

    app_type_label = Label(newWindow, text ="Appointment Type", fg="DarkOrange1", bg="black", font=("Arial", 12))
    app_type_label.place (relx=0.3, rely=0.6, anchor=CENTER)

    # Creating submit button

    submit_btn = Button (newWindow, text="Add Record to Database", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground="#ba722d", activeforeground="white",  command=submit)
    submit_btn.place (relx=0.5, rely=0.7, anchor=CENTER)

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

openNewWindow()
newWindow.withdraw()
# ========================================================> Making the settings window

def openNewWindow1():
     
    newWindow1 = Toplevel(master)
    newWindow1.title("Settings")
    newWindow1.geometry("800x500")
    newWindow1.configure(bg="black")
    newWindow1.iconbitmap ('CodeHub.ico')
    newWindow1.resizable(0,0)
    constant_bt(newWindow1, master)
     
    Lbl1 = Label(newWindow1, text ="Settings", font=("Tw Cen MT", 40), fg="DarkOrange1", bg="black")
    Lbl1.place(relx=0.5, rely=0.1, anchor= CENTER)

    def credit():
       crd = Tk()
       #crd.geometry("500x300")
       crd.overrideredirect(True)

       w = 500
       h = 300 
       ws = crd.winfo_screenwidth() # width of the screen
       hs = crd.winfo_screenheight() # height of the screen
       x = (ws/2) - (w/2)
       y = (hs/2) - (h/2)
       crd.geometry('%dx%d+%d+%d' % (w, h, x, y))
       crd.config(bg = "white")
       crd_frame = Frame(crd, bg = "black", height=298, width = 498, relief = "groove")
       crd_frame.place(x=1,y=1)
       
       Lbl1 = Label(crd_frame, text ="Credits", font=("Tw Cen MT", 24), fg="DarkOrange1", bg="black")
       Lbl1.place(x = 210, y = 5)

       EG = Label(crd_frame, text ="Emanuel Gasco - Main Code", font=("Tw Cen MT", 20), fg="DarkOrange1", bg="black")
       EG.place(x = 100, y = 80)

       JD = Label(crd_frame, text ="Jason Dedgjonaj / Easi Studios -  Data Retrieval, window \nfocusing and more TBD.", font=("Tw Cen MT", 14), fg="DarkOrange1", bg="black")
       JD.place(x = 40, y = 120)

       close = Button(crd_frame, text = "Exit", font = ("Tw Cen MT", 18), fg = "DarkOrange", bg = "black", command = lambda: [crd.destroy()])
       close.place(x = 230, y = 220)

       def on_enter(e):
        close.config(bg='DarkOrange1', fg="black")

       def on_leave(e):
        close.config(bg='grey11', fg='DarkOrange1')

       # Button binds for changing colours
       close.bind('<Enter>', on_enter)
       close.bind('<Leave>', on_leave)
       
    creds = Button(newWindow1, text = "Credits", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='white', command= lambda:[credit()])
    creds.place(relx=0.5, rely=0.5, anchor=CENTER)

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

    def on_enter2(e):
        creds.config(bg='DarkOrange1', fg="black")

    def on_leave2(e):
        creds.config(bg='grey11', fg='DarkOrange1')


    # Button binds for changing colours
    myInfo.bind('<Enter>', on_enter)
    myInfo.bind('<Leave>', on_leave)

    close.bind('<Enter>', on_enter1)
    close.bind('<Leave>', on_leave1)

    creds.bind('<Enter>', on_enter2)
    creds.bind('<Leave>', on_leave2)
    

def query_db(val, out):
   try:
      
      if out == "firstname":
         c.execute('''SELECT * FROM appointments WHERE id = ?''', [val])
         firstname = str(c.fetchone()[1])
         return firstname

      if out == "sname":
         c.execute('''SELECT * FROM appointments WHERE id = ?''', [val])
         surname = str(c.fetchone()[2])
         return surname

      if out == "app":
         c.execute('''SELECT * FROM appointments WHERE id = ?''', [val])
         app = str(c.fetchone()[4])
         return app

      if out == "dt":
         c.execute('''SELECT * FROM appointments WHERE id = ?''', [val])
         app_dt = str(c.fetchone()[3])
         return app_dt

      if out == "id":
         c.execute('''SELECT * FROM appointments WHERE id = ?''', [val])
         iD = str(c.fetchone()[0])
         return iD
   except:
      val = val + 1
      query_db(val)

def openNewWindow2():
    global c
    # New window configuration
    newWindow2 = Toplevel(master)
    newWindow2.title("Query")
    newWindow2.geometry("800x500")
    newWindow2.configure(bg="black")
    newWindow2.iconbitmap ('CodeHub.ico')
    #t_frame = tk.Frame(newWindow2, bg = "red", height = 460, width = 750)
    #t_frame.pack(side = RIGHT, fill = BOTH)#, padx=10, pady=10)
    rtrn = tk.Button(newWindow2, text = "⏎", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='white', command = lambda: [newWindow2.withdraw(), newWindow.deiconify()])
    rtrn.place(relx=0.02, rely=0.9)

    def on_enter(e):
        rtrn.config(bg='DarkOrange1', fg="black")

    def on_leave(e):
        rtrn.config(bg='grey11', fg='DarkOrange1')

    rtrn.bind('<Enter>', on_enter)
    rtrn.bind('<Leave>', on_leave)

    newWindow2.deiconify()
    print("should have deiconified")

    t_scroll = tk.Scrollbar(newWindow2)
    t_scroll.pack(side=RIGHT, fill = Y)

    t_view = ttk.Treeview(newWindow2, show = 'headings', columns = ('Appointment ID', 'First Name', 'Surname', 'Appointment Date', 'Appointment Type', ), yscrollcommand = t_scroll)
    s=ttk.Style()
    s.configure('Treeview',rowheight = 30)
    t_view.pack(side = TOP, padx= 2)

    t_scroll.config(command = t_view.yview)
    t_view.config(yscrollcommand = t_scroll.set)

    t_view['columns'] = ("id", "firstname", "sname", "dt", "typ")
    t_view.column("#0", width = 120, minwidth = 25)
    t_view.column("id", anchor = W, width = 50)
    t_view.column("firstname", anchor = W, width = 120)
    t_view.column("sname", anchor = CENTER, width = 80)
    t_view.column("typ", anchor = CENTER, width = 80)
    t_view.column("dt", anchor = CENTER, width = 80)

    t_view.heading("#0", text = "Label", anchor = W)
    t_view.heading("id", text = "ID Code", anchor = W)
    t_view.heading("firstname", text = "First Name", anchor = W)
    t_view.heading("sname" , text = "Surname", anchor = CENTER)
    t_view.heading("typ", text = "Appointment Type", anchor = W)
    t_view.heading("dt" , text = "Appointment Date", anchor = CENTER)
    #t_view.heading("id", text = "ID Code", anchor = W)

    c.execute("SELECT * FROM appointments")
    leng = len(c.fetchall())
    val = 0

    for x in range(0, leng):
       val = val + 1
       idDee = query_db(val, "id")
       fname = query_db(val, "firstname")
       sname = query_db(val, "sname")
       dte = query_db(val, "dt")
       appo = query_db(val, "app")
       t_view.insert('', tk.END, values = (idDee, fname, sname, dte, appo))

    t_view.pack(fill = BOTH, padx = 10, pady=10)

    #d_frame = tk.LabelFrame(newWindow2, text="Record")
    #d_frame.pack(fill = X, expand = "yes", padx = 20)


    def query():
       conn = sqlite3.connect("Appoint.db")
       c = conn.cursor()

       c.execute("SELECT *, oid FROM appointments")
       records = c.fetchall()
       records = str(records) + "\n"


       
          
       print(records)

    query()


 
   


   
# ========================================================> Making the buttons that open the other windows

# Making the buttons and what they do
btn = Button(master, text="Quit", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command=master.destroy)

btn1 = Button(master , text="Settings", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = lambda: [master.withdraw(), openNewWindow1()])

btn2 = Button(master, text ="Appointments", fg="DarkOrange1", bg="grey11", relief="groove", font=("Arial", 15), activebackground='#ba722d', activeforeground='grey11', command = lambda: [master.withdraw(), openNewWindow()])



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
