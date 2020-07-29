import random
from tkinter import *

# function to center the tkinter window in the middle of the screen
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#fill the 3 tables with the correct characters
def fillTab():
    #1
    #Uppercase characters
    for i in range(65, 91): 
        optionOneChar.append(chr(i))

    #Lowercase characters
    for i in range(97, 123): 
        optionOneChar.append(chr(i))

    #2
    #Numbers
    for i in range(10):
        optionTwoChar.append(str(i))

    #3
    #all other symbols
    for i in range(33, 48):
        optionThreeChar.append(chr(i)) 
    for i in range(58, 65):
        optionThreeChar.append(chr(i)) 
    for i in range(91, 97):
        optionThreeChar.append(chr(i)) 
    for i in range(123, 127):
        optionThreeChar.append(chr(i)) 


def genPassword():
    save = choice.get()
    if(save==listeOptions[0]):
        password = ""

        for i in range(passwordLength.get()):
            password += random.choice(optionOneChar)
        passwordVar.set(password)

    elif(save==listeOptions[1]):
        password = ""

        length = passwordLength.get()
        nbNumbers = int(length//2)
        nbLetters = length - nbNumbers 
        
        for i in range(length):
            x = random.randint(1, 2)
            if(x == 1 and nbLetters > 0):
                password += random.choice(optionOneChar)
                nbLetters -= 1
            else:
                if(nbLetters == 0 or (x == 2 and nbNumbers > 0)):
                    password += random.choice(optionTwoChar)
                    nbNumbers -= 1
                else:
                    password += random.choice(optionOneChar)
                    nbLetters -= 1

        passwordVar.set(password)

    else:
        password = ""

        length = passwordLength.get()
        nbSymbols = int(length//3)
        nbNumbers = int(length//3)
        nbLetters = length - (nbNumbers + nbSymbols)      
        print(nbLetters, nbNumbers, nbSymbols)
        i = 0
        while (i < length):
            x = random.randint(1, 3)
            if(x==1 and nbLetters > 0):
                password += random.choice(optionOneChar)
                i += 1

            elif(x==2 and nbNumbers > 0):
                password += random.choice(optionTwoChar)
                i += 1

            elif(x==3 and nbSymbols > 0):
                i += 1
                password += random.choice(optionThreeChar)
        
        passwordVar.set(password)


optionOneChar = []
optionTwoChar = []
optionThreeChar = []
fillTab()
len1  = len(optionOneChar)
len2 = len(optionTwoChar)
len3 = len(optionThreeChar)



window = Tk()              
window.title("Password Generator") 
window.geometry("500x500")
center(window)

labelChar = Label(text="Choose the characters to include")
labelChar.pack()
listeOptions = ('Lowercase and uppercase characters only', 
                'Lowercase and uppercase characters, numbers', 
                'Lowercase and uppercase characters,numbers and all other symbols')
choice = StringVar()
choice.set(listeOptions[0])
om = OptionMenu(window, choice, *listeOptions)
om.pack()

labelLength = Label(text="Choose the length of the password")
labelLength.pack()
passwordLength = Scale(window, from_=5, to=25,
                             orient=HORIZONTAL)
passwordLength.set(15)
passwordLength.pack()

result = Label(text="PassWord :")
result.pack()

passwordVar = StringVar()
toCopy = Entry(window, textvariable=passwordVar, width=35)
toCopy.pack()

generateButton = Button(window, text="Generate", command=genPassword)
generateButton.pack()



window.mainloop()
