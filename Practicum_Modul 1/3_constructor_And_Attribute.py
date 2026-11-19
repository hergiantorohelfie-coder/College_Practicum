# kendaraan.py
class Kendaraan:
    # Class attribute: dimiliki bersama oleh semua object
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        # Instance attribute: unik untuk tiap object
        self.merk = merk
        self.warna = warna
        self.tahun = tahun


# Membuat 2 object
mobil = Kendaraan("Toyota", "Merah", 2020)
motor = Kendaraan("Honda", "Hitam", 2022)

# Akses instance attribute (nilainya berbeda tiap object)
print("=== Instance Attribute ===")
print(f"Mobil: {mobil.merk}, {mobil.warna}, {mobil.tahun}")
print(f"Motor: {motor.merk}, {motor.warna}, {motor.tahun}")

# Akses class attribute (bisa lewat class maupun object)
print("\n=== Class Attribute ===")
print(f"Lewat class  : {Kendaraan.bahan_bakar}")
print(f"Lewat mobil  : {mobil.bahan_bakar}")
print(f"Lewat motor  : {motor.bahan_bakar}")

# Mengubah class attribute lewat class: berlaku untuk semua object
Kendaraan.bahan_bakar = "Pertalite"
print("\n=== Setelah class attribute diubah lewat class ===")
print(f"Mobil: {mobil.bahan_bakar}")
print(f"Motor: {motor.bahan_bakar}")

# Mengubah lewat object: hanya membuat instance attribute baru di object itu
mobil.bahan_bakar = "Solar"
print("\n=== Setelah mobil.bahan_bakar diubah ===")
print(f"Mobil     : {mobil.bahan_bakar}")
print(f"Motor     : {motor.bahan_bakar}")
print(f"Kendaraan : {Kendaraan.bahan_bakar}")