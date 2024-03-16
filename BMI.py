weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal Weight")
elif bmi >= 25 and bmi <= 29.9:
    print("OverWight")
elif bmi >= 30 and bmi <= 34.9:
    print("Obesity")
elif bmi >= 35 and bmi <= 39.9:
    print("Extreme Obesity")
