class MataKuliah:

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    # Latihan a: method jumlah_mahasiswa()
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# Latihan b: 2 mata kuliah dan 3 mahasiswa
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Struktur Data")

m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Daftarkan mahasiswa ke masing-masing mata kuliah
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)

# Latihan c: tampilkan daftar mahasiswa dan jumlahnya
for mk in (mk1, mk2):
    print(f"Mata Kuliah : {mk.kode} - {mk.nama}")
    print("Mahasiswa   :", mk.daftar_mahasiswa())
    print("Jumlah      :", mk.jumlah_mahasiswa())
    print("-" * 40)
