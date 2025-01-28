def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp:.2f}\u00b0F is equal to {celsius_temp:.2f}\u00b0C.")