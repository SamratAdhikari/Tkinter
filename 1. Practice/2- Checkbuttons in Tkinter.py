# Checkbuttons and Entry Widget

from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Trivago Official")

# Heading
Label(root, text="Hotel? Trivago!", font="comicsansms 13 bold").grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment = Label(root, text= "Payment")

# Text for our form
name.grid(row=1, column=2, sticky=W)
phone.grid(row=2, column=2, sticky=W)
gender.grid(row=3, column=2, sticky=W)
emergency.grid(row=4, column=2, sticky=W)
payment.grid(row=5, column=2, sticky=W)

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
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# Checkbox
foodservice = Checkbutton(text="Meals from Hotel", variable= foodservicevar)
foodservice.grid(row=6, column=3)

# button and assigning command
def send():
    print("Thank you for choosing us...")
Button(text="Submit", command=send).grid(row=7, column=3)

root.mainloop()
