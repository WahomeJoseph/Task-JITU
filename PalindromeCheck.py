# Write a python function to that checks whether a word or phrase is a palindrome or note. Palindrome is a word or phrase that reads the same backward and forward
def is_palindrome(string):

    # remove whitespaces and convert the string to lowercase
    cleaned = string.replace(" ", "").lower()
    
    # check if the original input and its reverse are equal
    return cleaned == cleaned[::-1]

# Prompt user to enter the string
user_input = input("Enter a string: ")

# Check if the input is a palindrome by calling the is_palindrome function
if is_palindrome(user_input):
    # If the function returns True, the input is a palindrome
    print("Yes. String is a palindrome!.")
else:
    # If the function returns False, the input is not a palindrome
    print("No String is not a palindrome!.")
