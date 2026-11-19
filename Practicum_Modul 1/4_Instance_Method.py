# manajer_inventori.py
class ManajerInventori:
    def __init__(self):
        # Instance attribute: menyimpan data barang {nama: stok}
        self.inventori = {}

    # Instance method: menambah barang baru atau menambah stok
    def tambah_barang(self, nama, jumlah):
        if nama in self.inventori:
            self.inventori[nama] += jumlah
            print(f"Stok {nama} bertambah {jumlah}. Total sekarang: {self.inventori[nama]}")
        else:
            self.inventori[nama] = jumlah
            print(f"Barang baru ditambahkan: {nama} ({jumlah})")

    # Instance method: mengurangi stok, atau menghapus barang jika habis
    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            print(f"Barang {nama} tidak ditemukan.")
        elif jumlah > self.inventori[nama]:
            print(f"Stok {nama} tidak cukup. Tersisa: {self.inventori[nama]}")
        else:
            self.inventori[nama] -= jumlah
            print(f"Stok {nama} berkurang {jumlah}. Sisa: {self.inventori[nama]}")
            if self.inventori[nama] == 0:
                del self.inventori[nama]
                print(f"{nama} habis dan dihapus dari inventori.")

    # Instance method: menampilkan seluruh inventori
    def lihat_inventori(self):
        print("\n=== Daftar Inventori ===")
        if not self.inventori:
            print("Inventori kosong.")
        else:
            for nama, stok in self.inventori.items():
                print(f"- {nama}: {stok}")
        print()


# Demonstrasi semua method
manajer = ManajerInventori()

manajer.tambah_barang("Buku", 20)
manajer.tambah_barang("Pensil", 50)
manajer.tambah_barang("Buku", 5)       # menambah stok barang yang sudah ada
manajer.lihat_inventori()

manajer.hapus_barang("Pensil", 10)     # pengurangan stok
manajer.hapus_barang("Buku", 100)      # stok tidak cukup
manajer.hapus_barang("Penggaris", 1)   # barang tidak ada
manajer.lihat_inventori()

manajer.hapus_barang("Pensil", 40)     # stok habis, barang dihapus
manajer.lihat_inventori()