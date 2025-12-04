import sys

if len(sys.argv) == 3:
    print("User provided values")
    weight = float(sys.argv[1])
    height = float(sys.argv[2)
else:
    print("No input given - using default values")
    weight = 50
    height = 1.5

bmi = weight / (height * height)

print("Weight:", weight)
print("Height:", height)
print("BMI:", bmi)

if bmi < 18:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
