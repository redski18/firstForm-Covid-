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


    