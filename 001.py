# Pastikan Anda menginstal pustaka praytimes terlebih dahulu dengan perintah:
# pip install praytimes

from praytimes import PrayTimes

# Inisialisasi metode perhitungan waktu sholat (Umumnya metode MWL)
pray_times = PrayTimes('MWL')

# Input lokasi
latitude = float(input("Masukkan latitude (lintang lokasi Anda): "))
longitude = float(input("Masukkan longitude (bujur lokasi Anda): "))
timezone = float(input("Masukkan timezone lokasi Anda (contoh: +7 untuk WIB): "))

# Dapatkan waktu sholat untuk hari ini
from datetime import date
today = date.today()
waktu_sholat = pray_times.getTimes((today.year, today.month, today.day), (latitude, longitude), timezone)

# Tampilkan hasil
print("\n--- Waktu Sholat ---")
print("Subuh   :", waktu_sholat['fajr'])
print("Dzuhur  :", waktu_sholat['dhuhr'])
print("Ashar   :", waktu_sholat['asr'])
print("Maghrib :", waktu_sholat['maghrib'])
print("Isya    :", waktu_sholat['isha'])









