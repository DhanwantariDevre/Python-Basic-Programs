
# Create a GUI : tkinter
# Database : mysql.connector
# exception handling : No need to insert the package

# Create a GUI
'''two labels : one for username and one for password
 button : for clicking
 messagebox'''

#Exception Handling
'''
  To handle the exception of user credentials
  '''

#Create a function
'''
Submit function : to get the data
authorization : to check wether the user is valid or not
'''


from tkinter import *
from tkinter import messagebox   #for GUI
import mysql.connector    #for database

def submit():
    user_name=s_val.get()  # get () method returns the value
    pass_word=p_val.get()
    auth(user_name,pass_word)

def auth(u,p):
    try:
        db=mysql.connector.connect(host='localhost',user=u,password=p)
        messagebox.showinfo('login Successful',"Logged In")
    except:
        messagebox.showerror("Error","Invalid Credentials")


root=Tk()

l3=Label(root,text="Database Login Software",bg='red', fg='white').place(x=75,y=8)

l1 = Label(root,text="Username").place(x=10,y=40)
s_val=StringVar()
user=Entry(root,textvariable=s_val).place(x=80,y=40)

l2 = Label(root,text="Password").place(x=10,y=70)
p_val=StringVar()
password=Entry(root,textvariable=p_val,show="*").place(x=80,y=70)

b1= Button(root,text="Submit",bg="green", fg="white",command=submit).place(x=100,y=100)
root.geometry('300x200')
root.title("Login")
root.mainloop()



















