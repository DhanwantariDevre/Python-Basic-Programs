# Create the main window in Tkinter class
# we used Tk() class #case sensitive 
# Syntax
# root = tk.Tk(screenName = None, baseName:None, className='Tk', useTk=1)    # mandatory step

#1. Screenname : specify the name
#2. Basename : base name of the application
#3. classname : we can change the name of the window by setting this parameter to the desired name
#4. useTk :  whether we have to use it or not


#mainloop() : method used to run the application once it is ready

'''
from tkinter import *

root=tk.Tk() #create an a instance
root.title('Hope GUI') #titl eof thr window
root.geometry('300x300') #length x height
root.mainloop()
'''


#Using oops create an window
#frame is a parent class
#frame class has its own init()
#mainloop() is mandatory to made the window open


'''
from tkinter import *   # mandatory step

class window (Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

root = Tk()
gui = window(root)
root.title("GUI using oops")   #title() is used to give the title
root.geometry('300x300')
root.mainloop()
'''

#Method 1
'''
from tkinter import *

def close():
    exit()

root = Tk()
root.title("GUI using oops")
b1 = Button(root, text= "Click Me",command=close)   # command argument used to perform an event on button
b1.place(x=50,y=100)
root.geometry('300x300')
root.mainloop()

'''

#Method 2 using OOPS
'''
from tkinter import *

class window(Frame):
    def __init__(self,master= None):
        Frame.__init__(self,master)
        self.master=master
        self.pack(expand=1,fill=BOTH)   #task put the zero here and check
        #pack() is used to combine root and window
        #pack the instance expand=1 means open that window
        #fill means fill both sides that is left and right
        #We are placed that window on a Frame

        b1 = Button(self, text="Click Me", command=self.close)  # command argument used to perform an event on button
        b1.place(x=50,y=100)   # coordinates to place the button

    def close(self):
        exit()

root=Tk()
gui = window(root)
root.geometry('300x300')    
root.mainloop()


'''

'''#label in GUI
#LAbels are nothing but the static text

from tkinter import *
root=Tk()
l1 = Label(root, text="Click", bg="blue", fg="red")
l1.place(x=200,y=50)
root.geometry("300x300")
root.mainloop()
'''

'''
#menubar
#It is propoerly created only by object oriented
from tkinter import *

class window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master=master

        menu=Menu(self.master)   #creating an instance
        self.master.config(menu=menu)

        Fmenu=Menu(menu)
        Fmenu.add_command(label='New File')
        Fmenu.add_command(label='Open File')
        Fmenu.add_command(label='Exit',command=self.close)
        menu.add_cascade(label='File',menu=Fmenu)  #to put the submenus under File menu for that we use cascade

    def close(self):
        exit()

root=Tk()
gui=window(root)
root.title("GUI using OOPS")
root.minsize(300,300) 
root.maxsize(500,500)
#root.geometry('400x400')
root.mainloop()
'''

'''
from tkinter import *

def call():
    a=value.get()
    print(a)

root=Tk()
l1=Label(root,text="Name")
l1.place(x=20,y=40)
b1=Button(root,text="Show Me",command=call)
b1.place(x=20,y=80)


root.title("GUI using OOPS")
root.minsize(300,300)
root.maxsize(500,500)
root.geometry('400x400')
root.mainloop()

'''
'''
#Method 1
from tkinter import *
class window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.pack(expand=1,fill=BOTH)

        #label to show static text
        label1=Label(self,text="Name").place(x=20,y=40)
        self.ans=StringVar()

        #Entry box for input
        value=Entry(self,textvariable=self.ans).place(x=70,y=40)
        b1=Button(self,text="Print",command=self.call).place(x=60,y=80)

    #defining a function to get the value
    def call(self):
        a=self.ans.get()    #to get the value we are using get()
        print(a)

root=Tk()
gui=window(root)
root.geometry('300x300')
root.mainloop()
'''

#combobox
'''
from tkinter import *
from tkinter.ttk import Combobox  #for combobox it's mandatory

root=Tk()
1=Label(root,text='Select the fruit').place(x=10,y=30)
c1=Combobox(root)
c1['values']=['Kiwi','Mango','Watermelon','Strawberry','Apple']
c1.current(1)
c1.place(x=30,y=60)
root.geometry('300x300')
root.mainloop()
'''

# Prachi done the homework
'''
import tkinter as tk
def print_name():
    name=name_entry.get()
    output_label.config(text=f"Hello,{name}!")
    print(f"User's name is {name}")

root=tk.Tk()   #instance created
root.title("User's Name ")
root.geometry('300x300')

label=tk.Label(root,text="Enter your name : ",font=("Arial",12))
label.pack()

name_entry= tk.Entry(root,font=("Arial",12))
name_entry.pack()

button = tk.Button(root,text="Submit",command=print_name)
button.pack()

output_label=tk.Label(root,text=" ",font=("Arial",12),command=print_name)
button.pack()
output_label.pack()

root.mainloop()
'''
'''
#Radiobutton
from tkinter import *
from tkinter.ttk import Radiobutton

root=Tk()
l1=Label(root, text="Select the color ").place(x=10, y=30)

r1=Radiobutton(root,text="Red",value=1).place(x=10,y=60)
r2=Radiobutton(root,text="Green",value=2).place(x=10,y=90)
r3=Radiobutton(root,text="Blue",value=3).place(x=10,y=120)
r4=Radiobutton(root,text="Yellow",value=4).place(x=10,y=150)

root.geometry('300x300')
root.mainloop()
'''

#Messagebox
'''
from tkinter import *
from tkinter import messagebox

def process():
    messagebox.showerror('Error','Invalid')

root= Tk()
b1=Button(root,text="Click Me",command=process).place(x=50,y=50)
root.geometry('300x300')
root.mainloop()

'''




'''1function to add the numbers
2 labels
window title
1 messagebox
geometry for window size
button
'''
import tkinter as tk
from tkinter import messagebox

def add_num():
    try:
        n1=int(entry1.get())
        n2=int(entry2.get())
        result=n1+n2
        messagebox.showinfo("Total Sum ",f"the result is :{result}")
    except ValueError:
        messagebox.showerror("Error Found","Please enter valid number")
    def __add__(self,n1,n2):
        return n1+n2
root=tk.Tk()
root.title("Addition")

l1=tk.Label(root,text="Enter the first number :")
l1.pack()
entry1=tk.Entry(root)
entry1.pack()

l2=tk.Label(root,text="Enter the second number :")
l2.pack()
entry2=tk.Entry(root)
entry2.pack()

b1=tk.Button(root,text="Add", command=add_num)
b1.pack()
root.geometry("400x400")
root.mainloop()















