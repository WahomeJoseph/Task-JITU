# Write a pythionn function to check whether a string is a pangram or not. (Assume the string passed in does not have any punctuation). A pangram is a string of
# characters wich consits of all the all the alphabets at least once
# Program to check whether a string is a pangram

def ispangram(string):
  # alphabet set which contains lower case alphabet elements
  alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

  # convert the input string to lowercase
  string = string.lower()
  # input set which treats each element input individually
  input_set = set(string)
  return alphabet_set.issubset(input_set)

# main function
def main():
    user_input = input("Enter a string: ")
  # convert the string nput to lowercase
    user_input = user_input.lower()

    if ispangram(user_input):
        print("Yes!String is a pangram.")
    else:
        print("No!String is not a pangram.")

# check if program runs directly
if __name__ == "__main__":
    main()
