# Write a Program to extract each digit from an integer in the reverse order.

# Pseudocode

# convert integer to string then reverse
def extract_reverse(number):
    reversed = str(number)[::-1]
# extract digit
    for digit_str in reversed:
        number = int(digit_str)
# print
        print(number)  
# user input code
user_input = int(input("please provide a number: "))
extract_reverse(user_input)