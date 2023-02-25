'''
This is the backbone for your project.  Download this file and save it using
the naming structure LastFirstProject.py.  For example, if I were re-naming
this file, I would name it SzecseiDeniseProject.py

You will upload this file with your solutions to the individual parts of the
problem.  Points will be awarded based on the number of steps that you complete
correctly.  You should not use any outside resources (tutors, CS students,
industry professionals, Chegg, StackOverflow, etc...).  The work that you submit
must be your own.  If you need to review how to incorporate various GUI components
into a progrem or script, review the Widgets example that I developed last week.  
All of the python instructions have been provided in that
example.  Using functions that I have not discussed during lecture will earn
0 points for that particular problem.  For example, there are many ways to
place widgets into a root window.  I want you to use the method that I demonstrated
in the example.  So, if you decide to use a different approach, you will earn
0 points for that component.  If you want to explore different ways to
create GUIs, that is great.  But for this assignment, I want you to stick to
what was presented in class.

If you run this script, a window should appear...it should not crash!
The script that you submit MUST run without any errors.  If it cannot run
because of syntax errors, you will get a 0 on the project.  So, make sure
that you test your code before you submit it.

WARNING: LATE WORK IS NOT ACCEPTED.  DO NOT WAIT UNTIL THE LAST MINUTE TO
SUBMIT YOUR PROJECT.  IF ICON GOES DOWN, OR YOU LOSE INTERNET, YOU WILL RECEIVE
A 0 ON THE ASSIGNMENT.  AS SOON AS YOU MAKE PROGRESS, SUBMIT A WORKING VERSION
OF YOUR INTERMEDIATE PROGRAM SO THAT YOU WON'T GET A 0 ON THE ASSIGNMENT.  THE
TA WILL GRADE THE MOST RECENT SUBMISSION.

IMPORTANT NOTES: 

WHEN THE SUBMIT BUTTON IS PRESSED, ALL ENTRY BOXES SHOULD BE CLEARED, AN 
ACKNOWLEDGEMENT IS PRESENTED, AND THE SUBMIT BUTTON IS DISABLED.

BE SURE TO OPEN THE FILE TO APPEND (NOT WRITE...THAT WILL ERASE PREVIOUS
ENTRIES).

YOUR PROGRAM SHOULD CHECK THAT THE E-MAIL ADDRESS IS CORRECT (A BASIC CHECK THAT THE 
STRING IS SEPARATED BY @, WITH ONLY ONE @ IN THE STRING)

YOUR PROGRAM SHOULD VERIFY THAT THE PHONE NUMBER IS CORRECT USING A BASIC CHECK:
STRIP NON-DIGIT CHARACTERS AND THEN MAKING SURE THAT THE LENGTH IS CORRECT

IF CLARIFICATIONS TO THIS PROJECT ARE MADE, THEY WILL BE IN A MODULE
TITLED: PROJECT CLARIFICATIONS.  CHECK IT OFTEN, IN CASE ANYTHING NEEDS
TO BE CLARIFIED.  IF YOU ARE NOT SURE ABOUT SOMETHING, ASK!

'''
#we need to import tkinter to create the GUI
from tkinter import *

#we will need a Tk() root object to create your window, and put things inside of it
root = Tk()

#perhaps we want to set the size of our window and place things in our window
#set the size of the window to be 600 units wide (the x-component) and
#1000 units high/long (the y-component)
#2 points  (CUMULATIVE POINTS: 2/100)
root.geometry("600x1000")



#create a title for the window: COVID VACCINATION INFORMATION
#2 points  (CUMULATIVE POINTS: 4/100)
root.title("COVID VACCINATION INFORMATION")



#put a label on the screen that reads: All information will be
#kept confidential.
#determine where it should go so that it has the general look of the
#window that I used in my demonstration
#2 points  (CUMULATIVE POINTS: 6/100)
label_1 = Label(root, text='All information will be kept confidential.', width=30, font=('bold', 20))
label_1.place(x=50, y=30)

#put a label/entry box combination for the name of the person
#create a variable to store the name that is entered 
#Use a StringVar() for this.
#determine where they should go so that it has the general look of
#the window that I used in my demonstration
#3 points  (CUMULATIVE POINTS: 9/100)
label_2 = Label(root, text='Name', width=30, font=('bold', 15))
label_2.place(x=-20, y=100)

myName = StringVar()
nameEntry = Entry(root, textvariable=myName)
nameEntry.configure(width=40)
nameEntry.place(x=260, y=105)



#put a label/entry box combination for the phone number of the person
#create a variable to store the name that is entered 
#Use a StringVar() for this.
#determine where it should go so that it has the general look of
#the window that I used in my demonstration
#3 points  (CUMULATIVE POINTS: 12/100)
label_3 = Label(root, text='Phone Number', width=30, font=('bold', 15))
label_3.place(x=-20, y=150)

myPhone = StringVar()
phoneEntry = Entry(root, textvariable=myPhone)
phoneEntry.configure(width=40)
phoneEntry.place(x=260, y=155)

#put a label/entry box combination for the email address of the person
#create a variable to store the name that is entered 
#Use a StringVar() for this.
#determine where it should go so that it has the general look of
#the window that I used in my demonstration
#3 points  (CUMULATIVE POINTS: 15/100)
label_4 = Label(root, text='E-mail', width=30, font=('bold', 15))
label_4.place(x=-20, y=200)

myEmail = StringVar()
emailEntry = Entry(root, textvariable=myEmail)
emailEntry.configure(width=40)
emailEntry.place(x=260, y=205)

#we need a drop-down menu for the three different vaccines: Pfizer, Moderna, and
#Johnson & Johnson.  The user should select one of those options.  
#Be sure to include a label to identify the dropdown menu description.  We will need
#a variable to store the option selected.  Use a StringVar() for this.  Construct
#a meaningful option for the default view (you decide).  Place the
#drop-down menu in the window
#4 points (CUMULATIVE POINTS: 19/100)
label_5 = Label(root, text='Vaccine', width=30, font=('bold', 15))
label_5.place(x=-20, y=250)

vaccineList = ['Pfizer', 'Moderna', 'Johnson & Johnson']

vaccine = StringVar()
vaccine.set('Select your manufacturer')

dropDownList = OptionMenu(root, vaccine, *vaccineList)
dropDownList.place(x= 310, y=250)



#we need a dropdown menu for the shot number in the sequence: first, second, booster
#The user should select one of those options.  
#Be sure to include a default string to identify the dropdown menu description.  We will need
#a variable to store the option selected.  Use a StringVar() for this.  Construct
#a meaningful option for the default view (you decide).  Place the
#drop-down menu in the window
#4 points (CUMULATIVE POINTS: 23/100)
label_6 = Label(root, text='Round', width=30, font=('bold', 15))
label_6.place(x=-20, y=300)

shotNumberList = ['first', 'second', 'booster']

shotNumber = StringVar()
shotNumber.set('Which Round?')

dropDownList_2 = OptionMenu(root, shotNumber, *shotNumberList)
dropDownList_2.place(x= 323, y=300)

#we need check boxes for the different side effects.  Include the following:
#Pain at injection site, Pain down arm, Fever, Headache, 
#Nausea, Rash, Hives, Swelling, Chills, Body ache, None.
#The user could select more than one of those options, but it is possible
#for none of them to be chosen.  You can arrange them in the window as you
#see fit.  your window should look nice.  We will need
#We will need to keep track of the ones that were selected 
#(using IntVar() for them).  Place these check boxes in the window
#arrange them nicely. 
#10 points (CUMULATIVE POINTS: 33/100)
PainAtInjectionSite= IntVar()
PainAtInjectionSiteBox = Checkbutton(root, text='Pain at injection site', variable=PainAtInjectionSite)
PainAtInjectionSiteBox.place(x=70, y=370)

PainDownArm = IntVar()
PainDownArmBox = Checkbutton(root, text='Pain down arm', variable=PainDownArm)
PainDownArmBox.place(x=240, y=370)

Fever = IntVar()
FeverBox = Checkbutton(root, text='Fever', variable=Fever)
FeverBox.place(x=410, y=370)

Headache = IntVar()
HeadacheBox = Checkbutton(root, text='Headache', variable=Headache)
HeadacheBox.place(x=70, y=410) 

Nausea = IntVar()
NauseaBox = Checkbutton(root, text='Nausea', variable=Nausea)
NauseaBox.place(x=240, y=410)

Rash = IntVar()
RashBox = Checkbutton(root, text='Rash', variable=Rash)
RashBox.place(x=410, y=410)

Hives = IntVar()
HivesBox = Checkbutton(root, text='Hives', variable=Hives)
HivesBox.place(x=70, y=450)

Swelling = IntVar()
SwellingBox = Checkbutton(root, text='Swelling', variable=Swelling)
SwellingBox.place(x=240, y=450)

Chills = IntVar()
ChillsBox = Checkbutton(root, text='Chills', variable=Chills)
ChillsBox.place(x=410, y=450)

BodyAche = IntVar()
BodyAcheBox = Checkbutton(root, text='Body ache', variable=BodyAche)
BodyAcheBox.place(x=70, y=490)

NonE = IntVar()
NonEBox = Checkbutton(root, text='None', variable=NonE)
NonEBox.place(x=240, y=490)


#we will now create the function that checks that the phone number is valid
#This function should return the valid phone number extracted from the user
#input for a valid phone number, and return the Boolean False if it is not.  
#We will simply check if the user entered ten digits, and ignore any other characters.  
#This function should create a new string by iterating through the input string, 
#character by character, checking to see if a character is a digit.  if so, 
#put it in the new string.  When finished, check the length of the new string.  
#If the length is ten, we have a valid phone number, so return that valid string.
#Otherwise, it should return False.
#10 points (CUMULATIVE POINTS: 43/100)
def validPhoneNumber(number):
    newNumber = ''
    number = str(number)
    for num in number:
        if num.isdigit():
            newNumber = newNumber + num
            number = '' 
            number = number + newNumber
            
    if (len(number) == 10) and number.isdigit():
        return newNumber
    else:
        return False
    pass

#we will now create the function that checks that the email address is valid
#This function should return the e-mail address for a valid entry,
#and return the Boolean False if it is not.  
#We will simply check if there is only one @ symbol, with caracters on both sides
#of the @ symbol.  This function should return the input string if it is a valid
#email address, and return False if it is not.  HINT: use the split function to split
#the string by the @ symbol, and check the number of pieces the string was split into.
#also, check the length of each of the pieces.
#10 points (CUMULATIVE POINTS: 53/100)
def validEmail(email):
    email = str(email)
    counter = 0
    for i in email:
        if i == '@':
            counter = counter + 1
    if counter == 1:
        if '@' != email[-1] and '@' != email[0]:
            if len(email.split('@')) == 2:
                return email    
            else:
                return False
        else:
            return False        
    else:
        return False    
    pass



#Create a label for after the user submits the information, and place it
#in the window.  Since this will change when the user submits their information,
#we will need a StringVar() to set its value
#HINT: if you want the feedback to be invisible at any point
#set its contents to be the empty string.
#4 points    (CUMULATIVE POINTS: 57/100)

submitPressedLabelContents = StringVar()
submitPressedLabelContents.set('')
submitPressedLabel = Label(root, textvariable=submitPressedLabelContents)
submitPressedLabel.place(x=240, y=600)



#This is where the fun begins!

#now we can deal with our buttons.  Remember that we have two buttons to handle:
#a submit button and a start/clear button.  The Start/Clear button should clear
#all information from the entry boxes, reset the drop-down menu to the default
#option, clear all check boxes, and enable the Submit button to be active (or to do things).

#The submit button will check that the information is correct:

#name provided (not the empty string)
#phone number provided (valid phone number)
#email address provided (valid e-mail address)
#vaccine manufacturer provided
#vaccine number is selected
#if no check box is selected, we need to enter None when we write to the file

#if the data is complete, the data file, named 'ShotReactions.txt' will be opened to append, and the
#information will be written to the file. one line for each category (all of the check boxes
#selected will be on one line, separated by ; and if none are selected, None will be written
#to the file.

#for every user, the following 5 lines must be added, in this order:
#name
#phone number
#email
#vaccine manufacturer
#vaccine number
#reactions

#once the data is written to the file, we will close the file, clear out the contents of the
#entry boxes, reset the choice for the drop-down menu to the default value, 
#clear the check boxes, inactivate the submission button, and present a thank you message in the
#feedback label:  Thank you for your submission.
#the submit button should remain inactive until the user presses the Start/Clear button, to avoid
#submitting the same information multiple times.
#If the data is not complete, the feedback label will reflect that with a simple message:
#All information must be provided.
#Follow the logic in the comments to complete these functions.  Some of the things I have
#have done for you (and specified the variable names...so don't change them!).

#you will fill in the details for a submitPressed function to associate with the button
#make sure you understand how to complete each step
#24 points   (CUMULATIVE POINTS: 81/100)
submitCounter = 0
def submitPressed():
    global submitCounter
    submitCounter = submitCounter + 1
    if submitCounter >= 1:
        submitButton['state'] = DISABLED
    #we will have a Boolean for whether or not the user can submit
    canSubmit = True
    #here is the outline of what you need to do; any failure should change
    #the submission Boolean
    
    
    #verify that the name is not the empty string (1 point)
    name = myName.get()
    myName.get()
    if name == '':
        canSubmit = False
    
    #verify that the phone number is valid: use your helper function! (1 point)
    number = myPhone.get()
    myPhone.get()
    validPhoneNumber(number)
    if validPhoneNumber(number) == False:
        canSubmit = False
    
    #verify that the e-mail address is valid: use your helper function! (1 point)
    email = myEmail.get()
    myEmail.get()
    validEmail(email)
    if validEmail(email) == False:
        canSubmit = False
    
    
    #verify that a vaccine manufacturer has been selected.  (2 points)
    vaccination = vaccine.get()
    vaccine.get()
    if vaccination == 'Select your manufacturer':
        canSubmit = False
        
    shoty = shotNumber.get()
    shotNumber.get()
    if shoty == 'Which Round?':
        canSubmit = False
        
        
    #build the string for the reactions: For example, if pain at injection site
    #and rash were selected, generate the string 'pain at injection site; rash'
    #if any of these checks failed, present the feedback reflecting that there is a problem
    #5 points
    symptomString = ''
    
    if PainAtInjectionSite.get() == 1:
        symptomString = symptomString + 'Pain at injection site; '
    
    if PainDownArm.get() == 1:
        symptomString = symptomString + 'Pain down arm; '
    
    if Fever.get() == 1:
        symptomString = symptomString + 'Fever; '
    
    if Headache.get() == 1:
        symptomString = symptomString + 'Headache; '
    
    if Nausea.get() == 1: 
        symptomString = symptomString + 'Nausea; '
    
    if Rash.get() == 1:
        symptomString = symptomString + 'Rash; '        
    
    if Hives.get() == 1:
        symptomString = symptomString + 'Hives; '        
    
    if Swelling.get() == 1:
        symptomString = symptomString + 'Swelling; '        
    
    if Chills.get() == 1:
        symptomString = symptomString + 'Chills; '        
    
    if BodyAche.get() == 1:
        symptomString = symptomString + 'Body ache; '        
    
    if NonE.get() == 1:
        symptomString = symptomString + 'None'
        
    if len(symptomString) == 0:
        symptomString = symptomString + 'None'
        
    #5 points for this block
    #if all checks pass, open the file named 'ShotReactions.txt' to append
    if canSubmit == True:
        file = open('ShotReactions.txt', 'a') 
    
        #write the 5 lines of data to the file, in the correct order
        file.write(str(name)+'\n')
        file.write(str(validPhoneNumber(number))+'\n')
        file.write(str(email)+'\n')
        file.write(str(vaccination)+'\n')
        file.write(str(shoty)+'\n')
        
        file.write(str(symptomString)+'\n')
        
        
        #close the file
        file.close()
    
    
    #reset the variables/contents of the widgets (7 points)
    if canSubmit == True:
        myName.set('')
        myPhone.set('')
        myEmail.set('')
        vaccine.set('Select your manufacturer')
        shotNumber.set('Which Round?')
        
        PainAtInjectionSite.set(0)
        PainDownArm.set(0)
        Fever.set(0)
        Headache.set(0)
        Nausea.set(0)
        Rash.set(0)
        Hives.set(0)
        Swelling.set(0)
        Chills.set(0)
        BodyAche.set(0)
        NonE.set(0)
    #present the Thank you message (2 points)
    if canSubmit == False:
        submitPressedLabelContents.set('All information must be provided.')
    else:
        submitPressedLabelContents.set('Thank you for your submission.')
        
    
    #python hates an empty function
    return


#you will fill in the details for a startPressed function to associate with the button
#11 points   (CUMULATIVE POINTS: 92/100) 

def startPressed():
    submitButton['state']= NORMAL
    
    #this is a new submission, or a clearing of any information in the window

    #clear the contents of the name, phone number, e-mail entry boxes, as well
    #as the gratitude label (use empty strings to make things simple)  (4 points)
    myName.set('')
    myPhone.set('')
    myEmail.set('')    
    #clear the check boxes (4 points)
    PainAtInjectionSite.set(0)
    PainDownArm.set(0)
    Fever.set(0)
    Headache.set(0)
    Nausea.set(0)
    Rash.set(0)
    Hives.set(0)
    Swelling.set(0)
    Chills.set(0)
    BodyAche.set(0)
    NonE.set(0)    
    #reset the manufacturer selection (3 points)
    vaccine.set('Select your manufacturer')
    shotNumber.set('Which Round?')
    
    submitPressedLabelContents.set('')
    return

    
            
#create a new button and put it on the left of the screen.  The
#text should read 'Start/Clear'...you may choose colors to customize your button (if you want)
#or you can go with the default view, or the black/white combination.  If the text is not
#clear (i.e. your color combination is bad from a user experience, you may lose a point...
#keep in mind that some users might be color blind! think about accessibility!).  Be sure
#to connect the functionality to the appropriate function created above.
#4 points   (CUMULATIVE POINTS: 96/100)

startClear = Button(root, text= 'Start/Clear', width= 20, command= startPressed)
startClear.place(x=65, y=550)



#create a submit button and put it at the same level in the window, and to the
#right of the Start/Clear button.  The text should read 'Submit'
#you may choose colors to customize your button (if you want)
#be sure to connect the functionality to the appropriate function created above!
#4 points   (CUMULATIVE POINTS: 100/100)

submitButton = Button(root, text= 'Submit', width=20, command=submitPressed)
submitButton.place(x=320, y=550)

#that's all that you need to do!
#this line of code will run your function and create the window for you
root.mainloop()
