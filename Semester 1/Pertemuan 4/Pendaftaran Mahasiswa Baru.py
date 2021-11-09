print("Selamat datang pada laman pendaftaran mahasiswa baru!")
print("           silahkan isi data berikut!                ")

nis = input("Masukan Nomor Induk Sekolah           : ")
nama = input("Masukan Nama Anda                    : ")
jurusan = input("Masukan Jurusan Anda [SI/SIA]     : ")

if jurusan == 'SI' or jurusan == 'si':
    namajurusan = "Sistem Informasi"
    harga = 2400000
else:
    namajurusan = "Sistem Informasi Akutansi"
    harga = 2000000

print("------------------------------------------------------")
print("          UNIVERSITAS BINA SARANA INFORMATIKA         ")
print("------------------------------------------------------")
print("Nomor Induk Sekolah      : " +str(nis))
print("Nama Mahasiswa           : " +str(nama))
print("Jurusan                  : " +str(namajurusan))
print("biaya yang harus dibayar : ", +(harga))