print("---------------------------------------")
print("---------- PT DINGIN DAMAI ------------")
print("---------------------------------------")

nama_karyawan = input("Nama Karyawan              : ")
golongan_jabatan = input("Golongan Jabatan[1/2/3] : ")
pendidikan = input("Pendidikan[SMA/D1/D3/S1]      : ")
jam_kerja = int(input("Jumlah Jam Kerja           : "))
gaji_pokok = 300000

if golongan_jabatan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan_jabatan == 2:
    tunjangan_jabatan = 0.1 * gaji_pokok
else:
    tunjangan_jabatan = 0.15 * gaji_pokok

if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = 0.2 * gaji_pokok
else:
    tunjangan_pendidikan = 0.3 * gaji_pokok

tunjangan = tunjangan_jabatan + tunjangan_pendidikan

if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0
    print(" maaf! anda tidak mendapatkan gaji lembur :( ")


print("---------------------------------------")
print("-------- PROGRAM GAJI KARYAWAN --------")
print("---------------------------------------")
print("Nama Karyawan        : " +str(nama_karyawan))
print("Golongan Jabatan     : " +str(golongan_jabatan))
print("Pendidikan           : " +str(pendidikan))
print("Jumlah Jam Kerja     : ", +(jam_kerja))
print("Tunjangan Jabatan    :Rp. ", +(tunjangan_jabatan))
print("Tunjangan Pendidikan :Rp. ", +(tunjangan_pendidikan))
print("Uang Lembur          :Rp. ", +(lembur))
print("                         -------------- +")
total_gaji = gaji_pokok + tunjangan + lembur
print("Total Gaji Anda      :Rp. ", +(total_gaji))