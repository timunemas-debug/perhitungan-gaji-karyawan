class Karyawan:
    def __init__(self):
        self.nama = input("Masukan Nama Karyawan: ")
        self.golongan = input("Golongan Karyawan(1,2,3): ")
        self.pendidikan = input("Pendidikan Karyawan(SMA,D1,D3,S1): ")
        self.lembur = int(input("Masukan Jam Kerja Lembur Anda: "))
        self.gaji_pokok = int(input("Masukan Gaji Pokok: "))

    def hitung_gaji_golongan(self):
        tunjangan_golongan = {"1": 0.05, "2": 0.1, "3": 0.15}
        return self.gaji_pokok * tunjangan_golongan.get(self.golongan, 0)
    
    def hitung_gaji_pendidikan(self):
        tunjangan_pendidikan = {"SMA": 0.025, "D1": 0.05, "D3": 0.2, "S1": 0.3}
        return self.gaji_pokok * tunjangan_pendidikan.get(self.pendidikan, 0)
    
    def hitung_upah_lembur(self):
        if self.lembur < 0:
            raise ValueError("Masukan dengan benar!")
        return self.lembur * 3500
        
    def total_gaji_semuanya(self):
        gaji_pokok = self.gaji_pokok
        total = gaji_pokok + self.penghitungan_gaji_golongan() + self.perhitungan_gaji_pendidikan() + self.jam_lembur()
        return total
    
    def output(self):
        print("\n=== Rincian Gaji Karyawan ===")
        print(f"Nama Karyawan     : {self.nama}")
        print(f"Golongan          : {self.golongan}")
        print(f"Pendidikan        : {self.pendidikan}")
        print(f"Jam Lembur        : {self.lembur}")
        print(f"Gaji Pokok        : {self.gaji_pokok}")
        print(f"Tunjangan Golongan: {self.hitung_gaji_golongan()}")
        print(f"Tunjangan Pendidikan: {self.hitung_gaji_pendidikan()}")
        print(f"Upah Lembur      : {self.hitung_upah_lembur()}")
        print(f"Total Gaji        : {self.total_gaji_semuanya()}")
        print("================================")

karyawan1 = Karyawan()
karyawan1.output()