import os

filename = input("Enter the file name: ")


if os.path.isfile(filename):
    print("File exists in the current directory.",filename)
else:
   print("File not exists in the current directory.",filename)