
import sys

sfile = sys.argv[1]
dfile = "Demo.txt"

f1 = open(sfile, "r")

f2 = open(dfile, "w")

for line in f1:
    f2.write(line)

f1.close()
f2.close()

# ✅ Show the copied content on screen
f3 = open("Demo.txt", "r")
print("Contents copied to COPIED.txt:")
print(f3.read())
f3.close()
