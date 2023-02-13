weight = float(input(''))
height = float(input(''))
BMI=round(weight / (height * height), 2)
print('%.2f'%BMI)
if BMI <18.5:
    print('Underweight')
elif 18.5<=BMI<25:
    print('Normal')
elif 25<=BMI<30:
    print('Overweight')
else:
    print('Obese')