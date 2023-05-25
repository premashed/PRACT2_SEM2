import os
import shutil

def create_directory(currentPath, name):
    path = os.path.join(currentPath, name)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print('Directory already exists')

def delete_directory(currentPath, name):
    path = os.path.join(currentPath, name)
    if os.path.exists(path):
        os.rmdir(path)
    else:
        print('Directory does not exist')

def create_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if not os.path.exists(filename):
        open(filename, 'a').close()
    else:
        print('File already exists')

def write_file(currentPath, name, words):
    filename = os.path.join(currentPath, name)
    if not os.path.exists(filename):
        print('New file created')
    file = open(filename, 'a')
    text = ''
    for word in words:
        text += str(word)
    file.write(text)
    file.close()

def read_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if os.path.exists(filename):
        file = open(filename, 'r')
        text = file.read()
        file.close()
        print(text)
    else:
        print('File does not exist')

def delete_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print('File does not exist')

def copy_file(currentPath, name, destination):
    sourcePath = os.path.join(currentPath, name)
    destinationPath = os.path.join(rootDirectory, destination)
    if os.path.exists(sourcePath) and os.path.exists(destinationPath):
        shutil.copy(sourcePath, destinationPath)
    else:
        print('Invalid path')

def move_file(currentPath, name, destination):
    sourcePath = os.path.join(currentPath, name)
    destination = os.path.join(rootDirectory, destination)
    destinationPath = os.path.join(destination, name)
    if os.path.exists(sourcePath) and os.path.exists(destination):
        os.replace(sourcePath, destinationPath)
    else:
        print('Invalid path')

def rename_file(currentPath, name, newName):
    oldPath = os.path.join(currentPath, name)
    newPath = os.path.join(currentPath, newName)
    if os.path.exists(oldPath):
        os.rename(oldPath, newPath)
    else:
        print('Invalid path')


rootDirectory = os.path.dirname(os.path.abspath(__file__))
dirName = 'root'
rootDirectory = os.path.join(rootDirectory, dirName)
if not os.path.exists(rootDirectory):
    os.mkdir(rootDirectory)

currentdir = rootDirectory
rootlength, depth = len(rootDirectory), 0
print('Please enter a command! To check commands list write "commands"')

command = input(currentdir[rootlength:] + '> ')

while command != 'quit':
    if command == 'changedir':
        print('Enter desired path')
        path = input('> ')
        new_path = os.path.join(currentdir, path)
        if os.path.exists(new_path):
            currentdir = new_path
            depth += 1
        else:
            print('This directory does not exist')
    elif command == 'commands':
        print('changedir, quit, up, makedir, deldir, make, write, read, del, move, rename')
    elif command == 'up':
        if depth:
            currentdir = os.path.dirname(currentdir)
            depth -= 1
        else:
            print('You are currently in the root directory')
    elif command == 'makedir':
        print('Enter directory name')
        dir_name = input('> ')
        create_directory(currentdir, dir_name)
    elif command == 'deldir':
        print('Enter directory name')
        dir_name = input('> ')
        delete_directory(currentdir, dir_name)
    elif command == 'make':
        print('Enter file name')
        file_name = input('> ')
        create_file(currentdir, file_name)
    elif command == 'write':
        print('Enter file name')
        file_name = input('> ')
        print('Enter file content')
        content = input('> ')
        write_file(currentdir, file_name, content)
    elif command == 'read':
        print('Enter file name')
        file_name = input('> ')
        read_file(currentdir, file_name)
    elif command == 'delete':
        print('Enter file name')
        file_name = input('> ')
        delete_file(currentdir, file_name)
    elif command == 'copy':
        print('Enter file name')
        file_name = input('> ')
        print('Enter new file name')
        new_name = input('> ')
        copy_file(currentdir, file_name, new_name)
    elif command == 'move':
        print('Enter file name')
        file_name = input('> ')
        print('Enter new directory')
        file_dir = input('> ')
        move_file(currentdir, file_name, file_dir)
    elif command == 'rename':
        print('Enter file name')
        file_name = input('> ')
        print('Enter new file name')
        new_name = input('> ')
        rename_file(currentdir, file_name, new_name)
    else:
        print("You have used an incorrect command! Write 'commands' to see the list")
    command = input(currentdir[rootlength:] + '> ')
