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

# Lowercase function.
def lowercase(path):
    for filenames in listdir(path):
        rename('{}\{}'.format(path, filenames), filenames.lower())
        move(filenames.lower(), path)

# Uppercase function.
def uppercase(path):
    for filenames in listdir(path):
        rename('{}\{}'.format(path, filenames), filenames.upper())
        move(filenames.upper(), path)

# Options selector.
print('\033[32m{}\033[0m'.format('                  Renamer'))
print('')
print('Options:')
print('1 - Uppercase.')
print('2 - Lowercase.')
print('3 - Exit.')
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
        uppercase(path)
        break
    elif option == 2:
        path = str(input('Type the path: '))
        lowercase(path)
        break
    elif option == 3:
        quit()
    else:
        print('Incorret option, type another.')
