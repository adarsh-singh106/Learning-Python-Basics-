# 6. Write a python function which converts inches to cms.
# Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54  # Applying the conversion formula

# Taking user input
inches = float(input("Enter length in inches: "))

# Calling the function and displaying the result
print(f"{inches:.2f} inches is equivalent to {inches_to_cm(inches):.2f} cm")

