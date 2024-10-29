# Write a program that accepts a string as input, capitalizes the first letter of each word in the string
# function
def capitalize_first_letters(input_string):
    return input_string.title()

# prompt the user to enter a string
input_string = input("Enter a string: ")

# call the function to capitalize the first letter of each word
capitalized_string = capitalize_first_letters(input_string)

# Print the result
print("Capitalized string:", capitalized_string)
