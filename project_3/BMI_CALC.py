def bmi_calc():
    weight = int(input("Enter your weight (kg): "))
    height = int(input("Enter your height (cm): "))
    bmi = (weight / (height * height)) * 10000
    return f"Your BMI is: {round(bmi, 2)}"

def bmi_interpreter():
    bmi = float(input("Enter your bmi: "))
    interpretation = ""
    if bmi <= 18.5:
        interpretation = "underweight"
    elif 18.5 <= bmi <= 24.9:
        interpretation = "normal"
    elif 25 <= bmi <= 29.9:
        interpretation = "overweight"
    else:
        interpretation = "obese"
    return f"You are {interpretation}!"


print(bmi_calc())
print(bmi_interpreter())