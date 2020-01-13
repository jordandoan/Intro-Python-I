# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even(num: int) -> str:
    return ("Even!" if not num % 2 else "Odd")
# YOUR CODE HERE
print(is_even(num))
