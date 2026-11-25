"""Program OOP Perpustakaan Sederhana
Praktikum PBO - Modul 2: Encapsulation & Access Modifier

Relasi antar class:
- Buku <-> Peminjaman          : association  (Peminjaman mengenal/menunjuk Buku)
- Anggota <-> Peminjaman       : aggregation  (Anggota punya daftar_peminjaman)
- Perpustakaan <-> Buku        : composition  (Perpustakaan yang membuat Buku)
"""
from datetime import date


class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul                 # public
        self.penulis = penulis             # public
        self.kode_buku = kode_buku         # public
        self._stok = stok                  # protected
        self.__lokasi_rak = lokasi_rak     # private

    # Getter & setter lokasi rak (private)
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        if not lokasi_baru:
            raise ValueError("Lokasi rak tidak boleh kosong.")
        self.__lokasi_rak = lokasi_baru

    # Pengelolaan stok (protected, diubah lewat method)
    def get_stok(self):
        return self._stok

    def tambah_stok(self, jumlah=1):
        if jumlah <= 0:
            raise ValueError("Jumlah tambah stok harus positif.")
        self._stok += jumlah

    def kurangi_stok(self, jumlah=1):
        if jumlah <= 0:
            raise ValueError("Jumlah kurang stok harus positif.")
        if jumlah > self._stok:
            raise ValueError(f"Stok buku '{self.judul}' tidak mencukupi.")
        self._stok -= jumlah

    def info_buku(self):
        return (f"[{self.kode_buku}] {self.judul} - {self.penulis} | "
                f"Stok: {self._stok} | Rak: {self.__lokasi_rak}")


class Peminjaman:
    def __init__(self, buku, tanggal_pinjam):
        self.buku = buku                       # association ke Buku
        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = None            # diisi saat buku dikembalikan
        self.status = "Dipinjam"

    def info_peminjaman(self):
        kembali = self.tanggal_kembali if self.tanggal_kembali else "-"
        return (f"{self.kode_buku} ({self.buku.judul}) | "
                f"Pinjam: {self.tanggal_pinjam} | Kembali: {kembali} | "
                f"Status: {self.status}")


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota           # public
        self.nama = nama                       # public
        self._maks_pinjam = maks_pinjam        # protected
        self.__status_aktif = True             # private
        self.daftar_peminjaman = []            # aggregation: Peminjaman

    # Getter & setter status (private)
    def get_status(self):
        return self.__status_aktif

    def set_status(self, aktif):
        if not isinstance(aktif, bool):
            raise ValueError("Status harus bernilai True atau False.")
        self.__status_aktif = aktif

    def jumlah_pinjaman_aktif(self):
        return sum(1 for p in self.daftar_peminjaman if p.status == "Dipinjam")

    def pinjam_buku(self, buku, tanggal):
        if not self.__status_aktif:
            raise ValueError(f"Anggota {self.nama} tidak aktif.")
        if self.jumlah_pinjaman_aktif() >= self._maks_pinjam:
            raise ValueError(f"{self.nama} sudah mencapai batas pinjam.")
        buku.kurangi_stok()
        peminjaman = Peminjaman(buku, tanggal)
        self.daftar_peminjaman.append(peminjaman)
        return peminjaman

    def kembalikan_buku(self, kode_buku, tanggal):
        for p in self.daftar_peminjaman:
            if p.kode_buku == kode_buku and p.status == "Dipinjam":
                p.tanggal_kembali = tanggal
                p.status = "Dikembalikan"
                p.buku.tambah_stok()
                return p
        raise ValueError(f"Tidak ada peminjaman aktif untuk buku {kode_buku}.")

    def info_anggota(self):
        status = "Aktif" if self.__status_aktif else "Tidak aktif"
        return (f"[{self.id_anggota}] {self.nama} | Status: {status} | "
                f"Maks pinjam: {self._maks_pinjam} | "
                f"Pinjaman aktif: {self.jumlah_pinjaman_aktif()}")


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []                  # composition: Buku dibuat di sini

    def tambah_buku(self, judul, penulis, kode_buku, stok, lokasi_rak):
        buku = Buku(judul, penulis, kode_buku, stok, lokasi_rak)
        self.daftar_buku.append(buku)
        return buku


if __name__ == "__main__":
    # --- Instansiasi ---
    perpus = Perpustakaan("Perpustakaan STITEK Bontang")

    # 1. Buat 3 buku
    b1 = perpus.tambah_buku("Pemrograman Python", "Budi Raharjo", "B001", 3, "A-01")
    b2 = perpus.tambah_buku("Struktur Data", "Rinaldi Munir", "B002", 2, "A-02")
    b3 = perpus.tambah_buku("Basis Data", "Abdul Kadir", "B003", 1, "B-01")

    # 2. Buat 2 anggota
    a1 = Anggota("A001", "Helfie", maks_pinjam=3)
    a2 = Anggota("A002", "Siti", maks_pinjam=2)

    # 3. Anggota 1 pinjam 2 buku
    a1.pinjam_buku(b1, date(2026, 11, 20))
    a1.pinjam_buku(b2, date(2026, 11, 20))

    # 4. Anggota 2 pinjam 1 buku
    a2.pinjam_buku(b3, date(2026, 11, 21))

    # --- Demonstrasi sebelum pengembalian ---
    print("=" * 60)
    print("KONDISI SETELAH PEMINJAMAN")
    print("=" * 60)
    print("\n1. Informasi Buku dan Stok:")
    for b in perpus.daftar_buku:
        print("  ", b.info_buku())

    print("\n2. Informasi Anggota:")
    for a in (a1, a2):
        print("  ", a.info_anggota())

    print("\n3. Daftar Peminjaman:")
    for a in (a1, a2):
        print(f"   {a.nama}:")
        for p in a.daftar_peminjaman:
            print("     -", p.info_peminjaman())

    # 5. Pengembalian buku
    a1.kembalikan_buku("B001", date(2026, 11, 24))
    a2.kembalikan_buku("B003", date(2026, 11, 25))

    # --- Demonstrasi setelah pengembalian ---
    print("\n" + "=" * 60)
    print("KONDISI SETELAH PENGEMBALIAN")
    print("=" * 60)
    print("\n1. Informasi Buku dan Stok:")
    for b in perpus.daftar_buku:
        print("  ", b.info_buku())

    print("\n2. Informasi Anggota:")
    for a in (a1, a2):
        print("  ", a.info_anggota())

    print("\n3. Daftar Peminjaman:")
    for a in (a1, a2):
        print(f"   {a.nama}:")
        for p in a.daftar_peminjaman:
            print("     -", p.info_peminjaman())

    # --- Uji getter/setter & validasi ---
    print("\n" + "=" * 60)
    print("UJI GETTER/SETTER DAN VALIDASI")
    print("=" * 60)
    b1.set_lokasi_rak("C-05")
    print("Lokasi rak B001 (setelah diubah):", b1.get_lokasi_rak())
    a2.set_status(False)
    print("Status Siti aktif?", a2.get_status())
    try:
        a2.pinjam_buku(b2, date(2026, 11, 25))
    except ValueError as e:
        print("Pinjam gagal (anggota nonaktif):", e)
    try:
        b3.kurangi_stok(10)
    except ValueError as e:
        print("Kurangi stok gagal:", e)
