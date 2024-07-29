'''
                                                        Renamer
    
    This is the main file of the script, the one that will rename the files.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Libraries imports.
from os import rename, listdir
from shutil import move

# Variables definition.
option = int()
rawPath = str()

# Lowercase function.
def pathFixer(rawPath):
    lastChar = rawPath[len(rawPath) - 1]
    if lastChar == '/':
        print(rawPath)
        return(rawPath)
    else:
        path = rawPath + '/'
        print(path)
        return(path)

def lowercase(path):
    for filename in listdir(path):
        rename(path + filename, path + filename.lower())

# Uppercase function.
def uppercase(path):
    for filename in listdir(path):
        rename(path + filename, path + filename.uppercase())

def capitalize(path):
    for filename in listdir(path):
        rename(path + filename, path + filename.capitalize())

# Options selector.
print('\033[32m{}\033[0m'.format('                  Renamer'))
print('')
print('Options:')
print('1 - Uppercase.')
print('2 - Lowercase.')
print('3 - Capitalize')
print('4 - Exit.')
print('')
print('Script by Zourethe')
print('')

# Options conditions.
while True:
    try:
        option = int(input('Type the number to select the option: '))
    except:
        print('Type only numbers.')
    if option == 1:
        path = str(input('Type the path: '))
        uppercase(pathFixer(rawPath))
        break
    elif option == 2:
        rawPath = str(input('Type the path: '))
        lowercase(pathFixer(rawPath))
        break
    elif option == 3:
        rawPath = str(input('Type the path: '))
        capitalize(pathFixer(rawPath))
        break
    elif option == 4:
        quit()
    else:
        print('Incorret option, type another.')
