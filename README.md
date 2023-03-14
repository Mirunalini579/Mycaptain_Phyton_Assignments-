# Mycaptain_Phyton_Assignments-
#Assignments of Mycaptain python workshops 
#Task 1

import math
r=float(input("Input the radius of the circle:")
area = math.pi * (radius ** 2)
print(f"The area of circle with radius {r} is:{area}')



#Task 2

fname = input("Enter filename: ")
exten= fname.split(".")[-1].lower()

if exten == "py":
    print("The file is a Python script.")
elif exten == "cpp":
    print("The file is a C++ source file.")
elif exten == "java":
    print("The file is a Java source file.")
elif exten == "txt":
    print("The file is a plain text file.")
elif exten=="pdf":
    print("The file is Pdf file")
elif exten=="doc":
    print("The file is a microsoft word file")
elif exten=="bin":
    print("The file is a Binary file")
elif exten=="ppt":
    printf("The file is a Power point file")
elif exten=="mp3":
    print("The file is a audio file")
elif exten=="zip":
    print("The file is a audio file")
else:
    print("Unknown file type.")



