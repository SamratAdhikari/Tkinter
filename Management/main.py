# Management Software                                                                                                                                                                       

from tkinter import *
from tkinter import messagebox as msg
import tkinter as tk
from tkinter import ttk
import sqlite3
import sys


# Functions

def getrow(event):
    try:
        item = trv.item(trv.focus())
        t1.set(item["values"][0])
        t2.set(item["values"][1])
        t3.set(item["values"][2])
        t4.set(item["values"][3])
        t5.set(item["values"][4])
    except Exception as e:
        msg.showerror("Operation Failed", e)


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("", "end", values=i)


def search():
    try:
        ans = q.get()
        query = "SELECT * FROM customers WHERE name LIKE '%" + ans + "%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)

    except Exception as e:
        msg.showerror("Operation Failed", e)


def show_all():
    try:
        query = "SELECT * FROM customers"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)
    except Exception as e:
        msg.showerror("Operation Failed", e)


def add_cust():
    cust_id = t1.get()
    name = t2.get()
    phone = t3.get()
    gadget = t4.get()
    problem = t5.get()

    if name.strip() == "" or problem.strip() == "":
        msg.showerror("Operation Failed", "Please Enter Customer Name and Problem")
    else:
        try:
            query = "INSERT INTO customers(id, name, phone, gadget, problem) VALUES(?, ?, ?, ?, ?)"
            cursor.execute(query, (cust_id, name, phone, gadget, problem))
            mydb.commit()
            msg.showinfo("Operation Successful", f"Customer with name {name} added !!!")
            show_all()

        except sys.exc_info()[0] as e:
            msg.showerror("Operation Failed", "ID is used by another Customer")
    reset()


def del_cust():
    cust_id = t1.get()
    ask = msg.askquestion("Confirm Delete", "Are you sure you want to delete the customer?")
    try:
        if ask == "yes":
            query = f"DELETE FROM customers WHERE id = {cust_id}"
            cursor.execute(query)
            msg.showinfo("Done", "Customer Deleted !")
            mydb.commit()
            show_all()
    except Exception as e:
        msg.showerror("Operation Failed", e)
    reset()


def up_cust():
    cust_id = t1.get()
    name = t2.get()
    phone = t3.get()
    gadget = t4.get()
    problem = t5.get()

    ask = msg.askquestion("Confirm Update", "Are you sure you want to update the data of the customer?")
    if ask == "yes":
        try:
            query = "UPDATE customers SET name = ?, phone = ?, gadget = ?, problem = ? WHERE id = ?"
            cursor.execute(query, (name, phone, gadget, problem, cust_id))
            msg.showinfo("Operation Successful", "Customer data updated successfully !")
            mydb.commit()
            show_all()
        except Exception as e:
            msg.showerror("Operation Failed", e)
    reset()


def reset():
    t2.set("")
    t3.set(0)
    t4.set("Mobile")
    t5.set("")


def set_id(rows, t1):
    t1.set(len(rows) + 1)


mydb = sqlite3.connect("manage.db")
cursor = mydb.cursor()

# Create table in database
# query = "CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT,
# phone INTEGER, gadget TEXT, problem TEXT)" cursor.execute(query)
# mydb.commit()

root = Tk()

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Data")
wrapper1.pack(fill=BOTH, expand="yes", padx=20, pady=(10, 0))
wrapper2.pack(fill=BOTH, expand="yes", padx=20, pady=(0, 10))
wrapper3.pack(fill=BOTH, expand="yes", padx=20, pady=(0, 10))

# Treeview Section
trv = ttk.Treeview(wrapper1, columns=(0, 1, 2, 3, 4), show="headings", height=6)

# trv = ttk.Treeview(root, height=5, show="headings", columns=(0, 1, 2))
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 13))

trv.column(0, width=10, anchor=CENTER)
trv.column(1, width=100, anchor=CENTER)
trv.column(2, width=50, anchor=CENTER)
trv.column(3, width=50, anchor=CENTER)
trv.column(4, width=150, anchor=CENTER)

trv.pack(fill=BOTH, padx=(5, 5))

trv.heading(0, text="ID")
trv.heading(1, text="Name")
trv.heading(2, text="Phone")
trv.heading(3, text="Gadget")
trv.heading(4, text="Problem")

trv.bind("<Double-1>", getrow)

query = "SELECT * FROM customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# vsb = Scrollbar(wrapper1, orient="vertical", command=trv.yview)
# vsb.pack(side=RIGHT, fill=Y)
# trv.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
hsb.pack(side=BOTTOM, fill=X)
trv.config(xscrollcommand=hsb.set)

# Search Section
q = StringVar()

l1 = Label(wrapper2, text="Search", font="Helvetica 15")
l1.pack(side=tk.LEFT, padx=10)

e1 = ttk.Entry(wrapper2, textvar=q, width=30)
e1.pack(side=tk.LEFT, padx=10)

b1 = Button(wrapper2, text="Search", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white",
            command=search)
b2 = Button(wrapper2, text="Show All", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white",
            command=show_all)
b1.pack(side=tk.LEFT, padx=10)
b2.pack(side=tk.LEFT, padx=10)

# User Data Section
t1 = IntVar()
t2 = StringVar()
t3 = DoubleVar()
t4 = StringVar()
t5 = StringVar()

set_id(rows, t1)

opt = ["Mobile",
       "Laptop",
       "Tablet",
       "Desktop",
       "Other"]
t4.set("Gadgets")

l1 = Label(wrapper3, text="Customer ID", font="Helvetica 13")
l2 = Label(wrapper3, text="Customer Name", font="Helvetica 13")
l3 = Label(wrapper3, text="Phone No", font="Helvetica 13")
l4 = Label(wrapper3, text="Gadget", font="Helvetica 13")
l5 = Label(wrapper3, text="Problem", font="Helvetica 13")

l1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
l3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
l4.grid(row=4, column=0, padx=5, pady=5, sticky=W)
l5.grid(row=3, column=0, padx=5, pady=5, sticky=W)

e1 = ttk.Entry(wrapper3, textvar=t1, width=30)
e2 = ttk.Entry(wrapper3, textvar=t2, width=30)
e3 = ttk.Entry(wrapper3, textvar=t3, width=30)
e5 = ttk.Entry(wrapper3, textvar=t5, width=30)

someStyle = ttk.Style()
someStyle.configure('my.TMenubutton', font='Helvetica')

e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)
drop = ttk.OptionMenu(wrapper3, t4, "Mobile", *opt, style='my.TMenubutton')
drop.grid(row=4, column=1, padx=5, pady=5, ipadx=10, ipady=10)
e5.grid(row=3, column=1, padx=5, pady=5)

insert_btn = Button(wrapper3, text="Add Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="white", command=add_cust)
update_btn = Button(wrapper3, text="Update Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="white", command=up_cust)
delete_btn = Button(wrapper3, text="Delete Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="white", command=del_cust)
reset_btn = Button(wrapper3, text="Clear", font="times 12", borderwidth=3, relief=RAISED, bg="salmon", fg="white",
                   command=reset)

insert_btn.grid(row=0, column=2, padx=35, pady=3, ipadx=19)
update_btn.grid(row=1, column=2, padx=35, pady=3, ipadx=10)
delete_btn.grid(row=2, column=2, padx=35, pady=3, ipadx=13)
reset_btn.grid(row=3, column=2, padx=35, pady=3, ipadx=48)

root.title("Customer Manager")
root.geometry("800x600")
root.resizable(False, False)
root.mainloop()
