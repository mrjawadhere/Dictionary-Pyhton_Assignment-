# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
squares = {x: x**2 for x in range(1, 6)}
print(squares) 
#My Code is BElow:
# Take input from the user
number = int(input("Enter a number to find its square: "))

# Calculate the square
square = number ** 2

# Output the result
print(f"The square of {number} is {square}.")
