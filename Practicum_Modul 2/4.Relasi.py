# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []      # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # Latihan f: rata-rata nilai mahasiswa
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []       # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


if __name__ == "__main__":
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")

    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # relasi association
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))

    # Latihan a: tambahkan 2 Program Studi baru ke objek universitas
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_tk = uni.buat_program("Teknik Komputer")

    # Latihan b: masing-masing Program Studi minimal 2 Mata Kuliah
    mk3 = MataKuliah("SI101", "Basis Data")
    mk4 = MataKuliah("SI102", "Analisis Sistem")
    prodi_si.tambah_matakuliah(mk3)
    prodi_si.tambah_matakuliah(mk4)

    mk5 = MataKuliah("TK101", "Rangkaian Digital")
    mk6 = MataKuliah("TK102", "Arsitektur Komputer")
    prodi_tk.tambah_matakuliah(mk5)
    prodi_tk.tambah_matakuliah(mk6)

    # Latihan c: buat 3 Mahasiswa, beberapa objek Nilai, tambahkan
    # ke mahasiswa dengan tambah_nilai()
    m3 = Mahasiswa("23003", "Andi")
    m1.tambah_nilai(Nilai("SI101", 88))
    m2.tambah_nilai(Nilai("SI102", 82))
    m2.tambah_nilai(Nilai("TK101", 76))
    m3.tambah_nilai(Nilai("TI102", 91))
    m3.tambah_nilai(Nilai("TK101", 84))
    m3.tambah_nilai(Nilai("TK102", 79))

    # Latihan d: tampilkan daftar mata kuliah setiap Program Studi
    print("=== Daftar Mata Kuliah per Program Studi ===")
    for p in uni.programs:
        print(f"{p.nama}:")
        for mk in p.daftar_matakuliah:
            print(f"   {mk.kode} - {mk.nama}")
    print()

    # Latihan e: tampilkan daftar nilai setiap mahasiswa
    print("=== Daftar Nilai per Mahasiswa ===")
    for m in (m1, m2, m3):
        print(f"{m.nim} - {m.nama}:")
        for n in m.daftar_nilai:
            print(f"   {n.kode_mk}: {n.skor}")
    print()

    # Latihan f: tampilkan rata-rata nilai setiap mahasiswa
    print("=== Rata-rata Nilai per Mahasiswa ===")
    for m in (m1, m2, m3):
        print(f"{m.nim} - {m.nama}: {round(m.rata_rata(), 2)}")
    print()

    # Latihan g: panggil report_program untuk setiap Program Studi
    def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
        print(f"Program Studi: {prodi.nama}")
        print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
        print("Mahasiswa dan rata-rata nilai:")
        for m in semua_mahasiswa:
            relevan = [n for n in m.daftar_nilai
                       if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"       {m.nim} - {m.nama}: {round(avg, 2)}")
        print("-" * 40)

    print("=== Report Program ===")
    for p in uni.programs:
        report_program(p, [m1, m2, m3])