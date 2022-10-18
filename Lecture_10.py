# converting to uppercase

st = input("Enter a string: ")
codes = []

for ch in st:
    print(ch, "=", ord(ch))
    codes.append(ord(ch))

for e in codes:
    print(e, "=", chr(e))

name = input("Enter a name:")
upper = ""

for ch in name:
    if ord(ch) > ord("a") and ord(ch) <= ord("z"):
        upper += chr(ord(ch) - 32) # "a", ord("a") = 97, 97 - 32 = 65, chr(65)
    else:
        upper += ch
    
print("The name in all upper case is:", upper)


# Easier way of doing it in Python

print(name.upper()) # Function to turn all letters to upper case letters
print(name.lower()) # Function to turn all letters to lower case 


# Different part of the lecture


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

x = str2.find(str1.trim())
print(x)

x = str2.find(str1.strip())
print(x)

words = str2.split()
print(words)


n = int(input("Enter the number of files: "))
files = []

for i in range(0, n):
    print("Enter the name of the file", i + 1, end = ": ")
    filename = input(" ")
    files.append(filename)
