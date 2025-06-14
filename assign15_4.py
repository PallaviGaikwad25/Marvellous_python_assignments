
import sys

if len(sys.argv) != 3:
    print(" python compare_files.py file1 file2")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]
f1 = open(file1, "r")
f2 = open(file2, "r")


data1 = f1.read()
data2 = f2.read()


f1.close()
f2.close()



if data1 == data2:
        print("Both files have the same contents.")
else:
        print("Files have different contents.")

