import os

fname = input("Enter the file name: ")

if os.path.exists(fname):
    file = open(fname, 'r')
    contents = file.read()
    print("Contents of the file:")
    print(contents)
    file.close()
else:
    print("File does not exist. Creating the file...")
    file = open(fname, 'w')
    content = input("Enter content to write into the new file: ")
    file.write(content)
    file.close()
    print("created successfully with your content.",fname)