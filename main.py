from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")
win = Tk()
win.title("Employee Management System")
win.geometry("1920x1080+0+0")
win.config(bg="#2c3e50")
win.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

#Entries Frame
ef = Frame(win, bg="pink")
ef.pack(side=TOP, fill=X)
title = Label(ef, text="Employment Management System", font=("Calibri", 18, "bold"), bg="pink")
title.grid(row=0, columnspan=2,padx=10,pady=20)

lblName= Label(ef,text="Name",font=("Calibri",16),bg="pink")
lblName.grid(row=1,column=0,padx=15,pady=15)
txtName=Entry(ef,textvariable=name,font=("Calibri",16),width=25)
txtName.grid(row=1,column=1,padx=15,pady=15)

lblAge= Label(ef,text="Age",font=("Calibri",16),bg="pink")
lblAge.grid(row=1,column=3,padx=15,pady=15)
txtAge=Entry(ef,textvariable=age,font=("Calibri",16),width=25)
txtAge.grid(row=1,column=4,padx=15,pady=15)

lblDoj= Label(ef,text="Date of Joining",font=("Calibri",16),bg="pink")
lblDoj.grid(row=2,column=0,padx=15,pady=15)
txtDoj=Entry(ef,textvariable=doj,font=("Calibri",16),width=25)
txtDoj.grid(row=2,column=1,padx=15,pady=15)


lblEmail= Label(ef,text="E-Mail",font=("Calibri",16),bg="pink")
lblEmail.grid(row=2,column=3,padx=15,pady=15)
txtEmail=Entry(ef,textvariable=email,font=("Calibri",16),width=25)
txtEmail.grid(row=2,column=4,padx=15,pady=15)

lblGender= Label(ef,text="Gender",font=("Calibri",16),bg="pink")
lblGender.grid(row=3,column=0,padx=10,pady=10)
comboGender=ttk.Combobox(ef,font=("Calibri",16),width=29,textvariable=gender,state='readonly')
comboGender['values']=("Male","Female")
comboGender.grid(row=3,column=1,sticky='e')

lblcontact= Label(ef,text="Contact",font=("Calibri",16),bg="pink")
lblcontact.grid(row=3,column=3,padx=15,pady=15)
txtcontact=Entry(ef,textvariable=contact,font=("Calibri",16),width=25)
txtcontact.grid(row=3,column=4,padx=15,pady=15)

lblAddress= Label(ef,text="Address",font=("Calibri",16),bg="pink")
lblAddress.grid(row=4,column=0,padx=10,pady=10)
txtAddress=Text(ef,width=85,height=5,font=("Calibri",16))
txtAddress.grid(row=5,columnspan=6,padx=10,pady=10,sticky='w')

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def display():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def addemp():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtcontact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clremp()
    display()

def editemp():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtcontact.get(),
              txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clremp()
    display()

def delemp():
    db.remove(row[0])
    clremp()
    display()

def clremp():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)

bf=Frame(ef,bg="pink")
bf.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd=Button(bf,command=addemp,text="Add Details",width=16,font=("Calibri",16),bg="red",bd=0,fg="white").grid(row=0,column=0,padx=10)
btnEdit=Button(bf,command=editemp,text="Update Details",width=16,font=("Calibri",16),bg="green",bd=0,fg="white").grid(row=0,column=1,padx=10)
btnDel=Button(bf,command=delemp,text="Delete Details",width=16,font=("Calibri",16),bg="blue",bd=0,fg="white").grid(row=0,column=2,padx=10)
btnClr=Button(bf,command=clremp,text="Clear Details",width=16,font=("Calibri",16),bg="orange",bd=0,fg="white").grid(row=0,column=3,padx=10)

#Tree Frame
tf=Frame(win,bg="white")
tf.place(x=0,y=528,width=1400,height=250)
style=ttk.Style()
style.configure("mystyle.Treeview", font=('calibri',12),rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))

tv=ttk.Treeview(tf,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=3)
tv.heading("4",text="DOJ")
tv.column("4",width="25")
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width="25")
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

display()
win.mainloop()
