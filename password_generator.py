import random

print("welcome to theh password generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

number = input("Enter the number of passwords to generate: ")
number = int(number)

length = input("Enter the length of each password: ")
length = int(length)

print("\nhere are your passwords:")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(characters)
    print(password)