# 🚨 Don't change the code below 👇


def condition_estimation(bmi: int):
    if bmi < 18.5:
        return "are underweight"
    if bmi < 25:
        return "have a normal weight"
    if bmi < 30:
        return "are slightly overweight"
    if bmi < 35:
        return "are obese"
    return "are clinically obese"


HEIGHT = float(input("enter your height in m: "))
WEIGHT = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = round(WEIGHT / (HEIGHT**2))

CONDITION = condition_estimation(BMI)

print(f"Your BMI is {BMI}, you {CONDITION}.")
