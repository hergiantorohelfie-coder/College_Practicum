class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode                # public
        self._ketua = ketua             # protected
        self.__anggaran = 500000000     # private

    def get_ketua(self):
        return self._ketua

    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    def get_anggaran(self):
        return self.__anggaran

    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


# Latihan a: class Mahasiswa (nim, nama public; semester protected; IPK private)
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    def get_semester(self):
        return self._semester

    def set_semester(self, nilai):
        self._semester = nilai

    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, nilai):
        self.__ipk = nilai


def tampilkan(m):
    print(f"NIM      : {m.nim}")
    print(f"Nama     : {m.nama}")
    print(f"Semester : {m.get_semester()}")
    print(f"IPK      : {m.get_ipk()}")
    print("-" * 30)


if __name__ == "__main__":
    ps = ProgramStudi("TI", "Pak Wayan")
    print("Kode:", ps.kode)
    print("Ketua Prodi:", ps.get_ketua())
    print("Anggaran:", ps.get_anggaran())
    ps.set_ketua("Bu Diah")
    print("Ketua Prodi (baru):", ps.get_ketua())
    ps.kurangi_anggaran(100000000)
    print("Anggaran Tersisa:", ps.get_anggaran())

    # Latihan b: buat 2 objek Mahasiswa dan tampilkan datanya
    print("\n=== Latihan b: data awal ===")
    mhs1 = Mahasiswa("23001", "Budi", 3, 3.20)
    mhs2 = Mahasiswa("23002", "Siti", 5, 3.75)
    tampilkan(mhs1)
    tampilkan(mhs2)

    # Latihan c: ganti semester dan IPK
    print("\n=== Latihan c: setelah diubah ===")
    mhs1.set_semester(4)
    mhs1.set_ipk(3.40)
    mhs2.set_semester(6)
    mhs2.set_ipk(3.90)
    tampilkan(mhs1)
    tampilkan(mhs2)