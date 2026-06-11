berat = int(input("Masukkan berat badan (kg): "))
tinggi = int(input("Masukkan tinggi badan (cm): "))
bmi = berat / ((tinggi / 100) ** 2)
print("Berat:", berat, "kg")
print("Tinggi:", tinggi, "cm")
print("BMI:", round(bmi, 2))
if bmi < 18.5:
    print("Kategori: Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Kategori: Normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Kategori: Overweight")
else:
    print("Kategori: Obesity")