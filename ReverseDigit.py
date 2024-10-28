# Write a python program that takes an integer as input and returns an integer with reversed digit ordering
def reverse_integer(n):
    # Check if the number is negative
    negative = n < 0
    
    # Convert the absolute value of the integer to a string
    num_str = str(abs(n))
    
    # Initialize an empty string to store the reversed digits
    reversed_str = ""
    
    # Use a for loop to iterate over the string in reverse order
    for char in num_str[::-1]:
        reversed_str += char
    
    # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)
    
    # If the original number was negative, make the reversed number negative
    if negative:
        reversed_int = -reversed_int
    
    return reversed_int

# Prompt user to enter an integer
user_input = int(input("Enter an integer: "))

# Get the reversed integer
reversed_number = reverse_integer(user_input)

# Print the reversed integer
print("Reversed integer:", reversed_number)
