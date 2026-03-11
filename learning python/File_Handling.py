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



