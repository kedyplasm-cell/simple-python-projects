string = input("enter a word: ")
reversed_string = string[::-1]

if string == reversed_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

# print(f"wow, {string} is a stupid name" )
# print(f"your name reversed is {reversed_string}")