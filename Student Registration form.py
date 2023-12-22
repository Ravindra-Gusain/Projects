from tkinter import * 
root= Tk()

def getvals():
    print("Accepted")
root.geometry("500x400")
# Heading
Label(root, text="School Registration from", font="ar 16 bold").grid(row=0,column=3)

# Field Name
name=Label(root,text="Name")
Phone=Label(root,text="Phone")
cls=Label(root,text="Class")
Bldgrp=Label(root,text="Blood Group")
dob=Label(root,text="DOB")
addate=Label(root,text="Admission Date")

# Packing Field
name.grid(row=1,column=2)
Phone.grid(row=2,column=2)
cls.grid(row=3,column=2)
Bldgrp.grid(row=4,column=2)
dob.grid(row=5,column=2)
addate.grid(row=6,column=2)

# Variable for storing data
namevalue=StringVar
Phonevalue=StringVar
clsvalue=StringVar
Bldgrpvalue=StringVar
dobvalue=StringVar
addatevalue=StringVar
checkvalue=IntVar

# Creating Entry field
nameentry=Entry(root,textvariable=namevalue)
Phoneentry=Entry(root,textvariable=Phonevalue)
clsentry=Entry(root,textvariable=clsvalue)
Bldgrpentry=Entry(root,textvariable=Bldgrpvalue)
dobentry=Entry(root,textvariable=dobvalue)
addateentry=Entry(root,textvariable=addatevalue)

# Packing entry field
nameentry.grid(row=1,column=3)
Phoneentry.grid(row=2,column=3)
clsentry.grid(row=3,column=3)
Bldgrpentry.grid(row=4,column=3)
dobentry.grid(row=5,column=3)
addateentry.grid(row=6,column=3)

# Creating check button
chekbtn=Checkbutton(text="Remember Me?",variable=checkvalue)
chekbtn.grid(row=7,column=3)

# Submit Button
Button(text="Submit",command=getvals).grid(row=8,column=3)


root.mainloop()