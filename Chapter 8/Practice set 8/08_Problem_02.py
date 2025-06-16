# 2. Write a python program using function to convert Celsius to Fahrenheit.
 
# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32  # Applying the formula

# Taking user input
celsius = float(input("Enter temperature in Celsius: "))

# Calling the function and displaying the result
fahrenheit = convert_to_fahrenheit(celsius)
print(f"{celsius:.1f}°C is equivalent to {fahrenheit:.1f}°F")
