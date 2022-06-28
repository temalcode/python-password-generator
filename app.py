import random

def passwordGenerator(passwordLength, needCharacters, needNumbers):
    password = ''
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    characters = '!@#$%^&*()'
    
    allChars = letters
    if(needCharacters):
        allChars += characters
    if(needNumbers):
        allChars += numbers
        
    for char in range(passwordLength):
        password += random.choice(allChars)
    
    print('\nGenerated password: ' + password)

passwordLength = int(input('Enter the password length: '))
needCharacters = input('Do you want Characters (t/f): ')
if(needCharacters == 't' or needCharacters == 'T'):
    needCharacters = True
else:
    needCharacters = False
needNumbers = input('Do you want numbers (t/f): ')
if(needNumbers == 't' or needNumbers == 'T'):
    needNumbers = True
else:
    needNumbers = False

passwordGenerator(passwordLength, needCharacters, needNumbers)
