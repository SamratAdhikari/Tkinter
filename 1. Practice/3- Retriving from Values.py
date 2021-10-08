# Accepting User Input in Tkinter

# Checkbuttons and Entry Widget

from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Trivago Official")

# Heading
Label(root, text="Hotel? Trivago!", font="comicsansms 15 bold").grid(row=0, column=4)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment = Label(root, text= "Payment")

# Text for our form
name.grid(row=1, column=3)
phone.grid(row=2, column=3)
gender.grid(row=3, column=3)
emergency.grid(row=4, column=3)
payment.grid(row=5, column=3)

# variables for storing entries
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emergencyval = StringVar()
paymentval = StringVar()
foodservicevar = IntVar()

# entries for our form
nameentry = Entry(root, textvariable=nameval)
phoneentry = Entry(root, textvariable=phoneval)
genderentry = Entry(root, textvariable=genderval)
emergencyentry = Entry(root, textvariable=emergencyval)
paymententry = Entry(root, textvariable=paymentval)

# packing the entries
nameentry.grid(row=1, column=4)
phoneentry.grid(row=2, column=4)
genderentry.grid(row=3, column=4)
emergencyentry.grid(row=4, column=4)
paymententry.grid(row=5, column=4)

# Checkbox
foodservice = Checkbutton(text="Meals from Hotel", variable= foodservicevar)
foodservice.grid(row=6, column=4)

# button and assigning command
def send():
    print("Thank you for choosing us...")
    a = f"{nameval.get(),phoneval.get(),genderval.get(),emergencyval.get(),paymentval.get(), foodservicevar.get()}\n"
    print(a)
    with open("Trivago.txt", "a") as f:
        f.write(a)

Button(text="Submit", command=send).grid(row=7, column=4)

root.mainloop()
