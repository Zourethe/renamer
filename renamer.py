'''
                                                        Renamer
    
    This is the main file of the script, the one that will rename the files.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Libraries import.
from os import rename, listdir
from shutil import move

# Variables definition.
option = int()

# Lowercase function definition.
def lowercase(path):
    for filenames in listdir(path):
        # TODO: this will rename the files to their original name, but in lowercase, the renamed files will appear in the folder that
        # the script is located.
        rename('{}\{}'.format(path, filenames), filenames.lower())
        # TODO: this will move the files from the folder that the script is located to their original path.
        move(filenames.lower(), path)

# Uppercase function definition.
def uppercase(path):
    for filenames in listdir(path):
        # TODO: this will rename the files to their original name, but in uppercase, the renamed files will appear in the folder that 
        # the script is located.
        rename('{}\{}'.format(path, filenames), filenames.upper())
        # TODO: this will move the files from the folder that the script is located to their original path.
        move(filenames.upper(), path)

# Options selection menu.
print('Options:')
print('1 - Uppercase.')
print('2 - Lowercase.')
print('3 - Exit.')

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
