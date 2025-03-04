def bmi(weight, height):
    value = weight / (height ** 2)
    if value < 18.5:
        return "Underweight"
    elif 18.5 <= value < 24.9:
        return "Normal weight"
    else:
        return "Overweight"

print(bmi(70, 1.75))  # Example usage
