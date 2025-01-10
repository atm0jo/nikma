# Script Kalkulator BMI

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

# Fungsi untuk mengkategorikan BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        return "Normal (sehat)"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

# Input data pengguna
print("=== Kalkulator BMI ===")
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (m): "))

# Hitung BMI
bmi = hitung_bmi(berat, tinggi)
kategori = kategori_bmi(bmi)

# Tampilkan hasil
print("\nHasil:")
print(f"Berat badan: {berat} kg")
print(f"Tinggi badan: {tinggi} m")
print(f"BMI Anda: {round(bmi, 2)}")
print(f"Kategori: {kategori}")





