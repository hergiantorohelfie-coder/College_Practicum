# dosen.py
class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        print(f"{self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}")


# Instansiasi 2 object
dosen1 = Dosen("Budi Santoso", "0012345601")
dosen2 = Dosen("Siti Rahma", "0012345602")

# Memanggil method
dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek")
dosen2.ajar_mata_kuliah("Basis Data")