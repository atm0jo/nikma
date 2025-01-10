# Script Olah Data Nilai Siswa

# Data nilai siswa
nilai_siswa = [78, 85, 92, 88, 76, 95, 89, 73, 84, 91]

# 1. Hitung rata-rata nilai
def hitung_rata_rata(data):
    return sum(data) / len(data)

# 2. Cari nilai maksimum
def cari_nilai_maksimum(data):
    return max(data)

# 3. Cari nilai minimum
def cari_nilai_minimum(data):
    return min(data)

# 4. Hitung jumlah siswa dengan nilai di atas rata-rata
def hitung_siswa_di_atas_rata_rata(data):
    rata_rata = hitung_rata_rata(data)
    return len([nilai for nilai in data if nilai > rata_rata])

# Menampilkan hasil
rata_rata = hitung_rata_rata(nilai_siswa)
nilai_maks = cari_nilai_maksimum(nilai_siswa)
nilai_min = cari_nilai_minimum(nilai_siswa)
jumlah_di_atas_rata_rata = hitung_siswa_di_atas_rata_rata(nilai_siswa)

print("Rata-rata nilai siswa:", round(rata_rata, 2))
print("Nilai maksimum:", nilai_maks)
print("Nilai minimum:", nilai_min)
print("Jumlah siswa dengan nilai di atas rata-rata:", jumlah_di_atas_rata_rata)
