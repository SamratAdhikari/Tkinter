# Update a record in Database


from tkinter import *
import sqlite3
from tkinter import messagebox as msg


# Functions
def query():
    mydb = sqlite3.connect("address_book.db")
    cursor = mydb.cursor()

    # Query the DataBase
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print_records = ""
    for item in records:
        print_records += f"{str(item[0])} {str(item[1])}\t{str(item[6])}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=14, column=0, columnspan=2)
    mydb.commit()
    mydb.close()


def clear():
    # Clear the test boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def submit():
    mydb = sqlite3.connect("address_book.db")
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {
                       "f_name": f_name.get(),
                       "l_name": l_name.get(),
                       "address": address.get(),
                       "city": city.get(),
                       "state": state.get(),
                       "zipcode": zipcode.get()
                   }
                   )
    clear()
    msg.showinfo("Done", "Client Added to the Database!")
    mydb.commit()
    mydb.close()


def delete():
    mydb = sqlite3.connect("address_book.db")
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())
    mydb.commit()
    mydb.close()


def update():
    mydb = sqlite3.connect("address_book.db")
    cursor = mydb.cursor()

    record_id = delete_box.get()
    query = "UPDATE addresses SET first_name = :first, last_name = :last, address = :address, city = :city, state = :state, zipcode = :zipcode" \
            "WHERE oid = :oid"
    cursor.execute(query, {
        "first":f_edit.get(),
        "last":l_edit.get(),
        "address":add_edit.get(),
        "city":city_edit.get(),
        "state":state_edit.get(),
        "zipcode":zip_edit.get()
        "oid":record_id
    })


    mydb.commit()
    mydb.close()



def edit():
    editor = Tk()

    mydb = sqlite3.connect("address_book.db")
    cursor = mydb.cursor()

    record_id = delete_box.get()

    # Query the DataBase
    cursor.execute("SELECT * FROM addresses WHERE oid = " + str(record_id))
    records = cursor.fetchall()

    f_name_label = Label(editor, text="First Name")
    l_name_label = Label(editor, text="Last Name")
    address_label = Label(editor, text="Address")
    city_label = Label(editor, text="City")
    state_label = Label(editor, text="State")
    zipcode_label = Label(editor, text="Zipcode")
    delete_label = Label(editor, text="ID number")
    f_name_label.grid(row=0, column=0, pady=(10, 0), sticky=W)
    l_name_label.grid(row=1, column=0, sticky=W)
    address_label.grid(row=2, column=0, sticky=W)
    city_label.grid(row=3, column=0, sticky=W)
    state_label.grid(row=4, column=0, sticky=W)
    zipcode_label.grid(row=5, column=0, sticky=W)

    # Entries
    global f_edit
    global l_edit
    global add_edit
    global city_edit
    global state_edit
    global zip_edit

    f_edit = Entry(editor, width=30)
    l_edit = Entry(editor, width=30)
    add_edit = Entry(editor, width=30)
    city_edit = Entry(editor, width=30)
    state_edit = Entry(editor, width=30)
    zip_edit = Entry(editor, width=30)
    f_edit.grid(row=0, column=1, pady=(10, 0), padx=20)
    l_edit.grid(row=1, column=1, padx=20)
    add_edit.grid(row=2, column=1, padx=20)
    city_edit.grid(row=3, column=1, padx=20)
    state_edit.grid(row=4, column=1, padx=20)
    zip_edit.grid(row=5, column=1, padx=20)

    edit_btn = Button(editor, text="Save", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    for record in records:
        f_edit.insert(0, record[0])
        l_edit.insert(0, record[1])
        add_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zip_edit.insert(0, record[5])




        mydb.commit()
        mydb.close()
    editor.title("Update a Record")
    editor.geometry("400x600")
    editor.mainloop()

root = Tk()

# Labels
f_name_label = Label(root, text="First Name")
l_name_label = Label(root, text="Last Name")
address_label = Label(root, text="Address")
city_label = Label(root, text="City")
state_label = Label(root, text="State")
zipcode_label = Label(root, text="Zipcode")
delete_label = Label(root, text="ID number")
f_name_label.grid(row=0, column=0, pady=(10, 0), sticky=W)
l_name_label.grid(row=1, column=0, sticky=W)
address_label.grid(row=2, column=0, sticky=W)
city_label.grid(row=3, column=0, sticky=W)
state_label.grid(row=4, column=0, sticky=W)
zipcode_label.grid(row=5, column=0, sticky=W)
delete_label.grid(row=9, column=0)

# Entries
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)
delete_box = Entry(root, width=30)
f_name.grid(row=0, column=1, pady=(10, 0), padx=20)
l_name.grid(row=1, column=1, padx=20)
address.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
state.grid(row=4, column=1, padx=20)
zipcode.grid(row=5, column=1, padx=20)
delete_box.grid(row=9, column=1)

# Submit button
submit_btn = Button(root, text="Add Record", font="times 15", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

# Create a Query Button
query_btn = Button(root, text="Show Records", font="times 15", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

# Create a delete button
delete_btn = Button(root, text="Delete Record", font="times 15", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10)

# Create an Update Button
edit_btn = Button(root, text="Update Record", font="times 15", command=edit)
edit_btn.grid(row=11, column=0, columnspan=3, pady=10, padx=10)

root.title("Create a database")
root.geometry("400x600")
root.mainloop()
