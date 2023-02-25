#GUI in pythonm

#use the tkinter library for GUI components
from tkinter import *

#create a window to display our widgets
window = Tk()

#we'll put the window on the screen, first determine its size
#first component:width, second component: height
window.geometry("500x600")


#the window's title
window.title('Intro to CS Widgets')


#labels are used to display text
#
label_1 = Label(window, text='Personal Information', width=30, font=('bold', 20))
#specify it's location
label_1.place(x=0, y=30)




label_2 = Label(window, text='Name', width=30, font=('bold', 15))
label_2.place(x=-50, y=80)

#next, get the entry box
#
#
userName = StringVar()
#userName.set('Type your name')
#create the entry box itself... connect the entry box to the variablr to track its contents
nameEntry = Entry(window, textvariable=userName)
#change its width
nameEntry.configure(width=40)
#put it in the window
nameEntry.place(x=165, y=85)




#create label for email entry
label_3 = Label(window, text='E-mail', width=30, font=('bold', 15))
label_3.place(x=-50, y=120)


#now create e-mail entry box
userEmail = StringVar()
#create the entry box itself... connect the entry box to the variablr to track its contents
emailEntry = Entry(window, textvariable=userEmail)
#change its width
emailEntry.configure(width=40)
#put it in the window
emailEntry.place(x=165, y=124)


#create label indicating year of study
label_4 = Label(window, text='Enter Your Academic Year', font=('italic', 18))
label_4.place(x=100, y=170)



#next deal with radio buttons
#need a variable to hold the information: this time, we are storing integer values
year = IntVar()
year.set(0)

#now, create the 1st radio button
firstButton = Radiobutton(window, text='First Year', padx=0, var=year, value=1)
firstButton.place(x=50, y=210)

#now, create the 2nd radio button
secondButton = Radiobutton(window, text='Second Year', padx=0, var=year, value=2)
secondButton.place(x=140, y=210)

#now, create the 3r radio button
thirdButton = Radiobutton(window, text='Third Year', padx=0, var=year, value=3)
thirdButton.place(x=250, y=210)

#now, create the 4th radio button
fourthButton = Radiobutton(window, text='Fourth Year', padx=0, var=year, value=4)
fourthButton.place(x=350, y=210)

#check boxes
label_5 = Label(window, text='Programming Experience', font=('italic', 18))
label_5.place(x=100, y=250)

     #create a check box: java
java = IntVar()
javaBox = Checkbutton(window, text='Java', variable=java)
javaBox.place(x=100, y=300)
     #create a check box: python
python = IntVar()
pythonBox = Checkbutton(window, text='python', variable=python)
pythonBox.place(x=200, y=300)
     #create a check box: cPlusPlus
cPlusPlus = IntVar()
cPlusPlusBox = Checkbutton(window, text='cPlusPlus', variable=cPlusPlus)
cPlusPlusBox.place(x=300, y=300)

#dropdown menu creation
#create the data for the dropdown menu choices
majorList = ['Computer Science', 'Informatics', 'Computer Engineering']

#create variable to hold selected contents
major = StringVar()
major.set('Select Your Major')
#three pieces of info: who owns the widget, which variable tracks the item selected,
#and a pointer to the list containing the options
dropDownList = OptionMenu(window, major, *majorList)
dropDownList.place(x=170, y=350)


#we will crete a button that changes a label

#first create a label
#we need a variable to keep track of label contents
buttonPressedLabelContents = StringVar()
buttonPressedLabelContents.set('')
buttonPressedLabel = Label(window, textvariable=buttonPressedLabelContents)
buttonPressedLabel.place(x=150, y=400)

#finally add a button
#but lets create the function that will dictate button's behaviour

#function counts how many times i push the button
buttonCounter = 0

def buttonPressedFunction():
    global buttonCounter 
    buttonCounter = buttonCounter + 1
    if buttonCounter > 9:
        myButton['state'] = DISABLED
        
    myString = 'You pressed the button ' + str(buttonCounter) + ' times.'
    buttonPressedLabelContents.set(myString)
    

#create the button!
myButton = Button(window, text='Press Me!', width=20, bg='red', fg='white', command=buttonPressedFunction)
myButton.place(x=163, y=450)
myButton['state']= NORMAL


    



#end you widget program with this code:
#puts the window on the screen
window.mainloop()
