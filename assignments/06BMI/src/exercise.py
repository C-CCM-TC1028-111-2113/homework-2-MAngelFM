#The BMI IF ELSE
print("Give me a Weight ")
Weight=float(input())
print("Give me a Height ")
Height=float(input())

if Weight == 0:
    print("Revisa tus datos, alguno de ellos es erroneo")
elif Height == 0:
    print("Revisa tus datos, alguno de ellos es erroneo")
bmi = Weight / (Height ** 2)

if 0 < bmi < 20 :
    print("PESO BAJO")
elif 20 <= bmi < 25:
    print("PESO NORMAL")
elif 25 <= bmi < 30:
    print("SOBREPESO")
elif 30 <= bmi < 40:
    print("OBESIDAD")
elif bmi >= 25:
    print("OBESIDAD MORBIDA")
