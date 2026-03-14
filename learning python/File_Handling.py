'''
File Handling in Python

    - File Handling is used to read, write, and manage files.
    - It helps store data permanently.
    - Python provides built-in functions for file operations.
'''


'''
Steps of File Handling

1) Open the file
2) Perform operations (read / write)
3) Close the file
'''




# 1) Opening and Reading a File

print("READ FILE")

file = open("demo.txt", "w")
file.write("Hello Python\n")
file.write("Welcome to File Handling\n")
file.write("This is a demo file\n")
file.close()

file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()





# 2) readline() Example


print("\nREAD LINE BY LINE")

file = open("demo.txt", "r")
print(file.readline())
print(file.readline())
file.close()






# 3) readlines() Example


print("\nREAD ALL LINES USING LIST")

file = open("demo.txt", "r")
lines = file.readlines()

for line in lines:
    print(line)

file.close()





# 4) Writing to a File (Overwrite)

print("\nWRITE FILE")

file = open("demo.txt", "w")
file.write("File overwritten successfully\n")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()





# 5) Append Data to File


print("\nAPPEND FILE")

file = open("demo.txt", "a")
file.write("This line is appended\n")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()




# 6) Using WITH Statement

print("\nUSING WITH STATEMENT")

with open("demo.txt", "r") as file:
    data = file.read()
    print(data)





# 7) Check File Exists


print("\nCHECK FILE EXISTENCE")

import os

if os.path.exists("demo.txt"):
    print("File exists")
else:
    print("File not found")

