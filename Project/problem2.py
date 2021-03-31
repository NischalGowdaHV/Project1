"""
Problem2

Function that checks if a given word is a palindrome. Character case should be ignored.
Palindrome is a string which is read same from forward and reverse ex: MaaM
"""
given_string = 'MALAyalam'

# casefold is used for caseless comparision.
given_string = given_string.casefold()

# reverse the string
reversed_string = given_string[::-1]

# check if the string is equal to reverse of the string
if reversed_string == given_string:
   print("The given string is a palindrome.")
else:
   print("The given string is not a palindrome.")