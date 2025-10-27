'''def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if string is the same forward and backward
    return s == s[::-1]

user_input = input("Enter a sentence: ")
if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("Not a palindrome.")
'''

#without using functions

text = input("enter a name: ")
user = text.replace(" ","").lower()
if user==user[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palinbdrome")

