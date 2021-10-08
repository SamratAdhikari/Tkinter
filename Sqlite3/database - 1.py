# Create a database with sqlite3

from tkinter import *
import sqlite3

root = Tk()

# Create a database if not exists
mydb = sqlite3.connect("address_book.db")
cursor = mydb.cursor()

# Create a table
cursor.execute("CREATE TABLE addresses(first_name text, last_name text, address text, city text, "
               "state text, zipcode integer)")


# commit changes
mydb.commit()

# close connection
mydb.close()



root.title("Create a database")
root.geometry("400x400")
root.mainloop()