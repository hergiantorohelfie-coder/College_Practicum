class Mahasiswa:
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        print(f"Halo, nama saya {self.nama}, NIM {self.nim}, jurusan {self.jurusan}, "
              f"mahasiswa {Mahasiswa.universitas} dengan IPK {self.ipk:.2f}.")

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} diperbarui menjadi {self.ipk:.2f}")

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


mhs1 = Mahasiswa("Andi Pratama", "2201001", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Siti Aisyah", "2201002", "Sistem Informasi", 3.20)
mhs3 = Mahasiswa("Budi Santoso", "2201003", "Teknik Informatika")

for i, mhs in enumerate([mhs1, mhs2, mhs3], start=1):
    print(f"=== Mahasiswa {i} ===")
    mhs.perkenalan_diri()
    print(f"Predikat: {mhs.predikat_kelulusan()}\n")

print("=== Update IPK Mahasiswa 3 ===")
mhs3.update_ipk(2.60)
print(f"Predikat setelah update: {mhs3.predikat_kelulusan()}")