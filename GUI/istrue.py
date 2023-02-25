
def verifyDaString(bruh):
    isTrue = False

    myphone = StringVar()
    myphone.set(bruh)
    phone = myphone.get()
    
    if phone == 'boo':
        isTrue = True

    return isTrue
