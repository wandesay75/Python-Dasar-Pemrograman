pembeli = input("Masukan Nama                 : ")
no_hp   = input("Masukan No Handphone         : ")
jurusan = input("Masukan jurusan [SBY/BL/LMP] : ")

if jurusan == 'SBY' or jurusan == 'sby':
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == 'BL' or jurusan == 'bl':
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

jumlah_beli = int(input("Masukkan Jumlah beli : "))

if jumlah_beli >= 3:
    potongan = (jumlah_beli*harga)*0.1
else:
    potongan = 0

total =(jumlah_beli*harga)-potongan


print("---------------------------------------------")
print("           PENJUALAN TICKET BUS              ")
print("                 SUKAMANAH                   ")
print("---------------------------------------------")
print("Nama Pembeli              : " +str(pembeli))
print("No Handphone              : " +str(no_hp))
print("Kode Jurusan yang dipilih : " +str(jurusan))
print("Nama Kota Tujuan          : " +str(namajurusan))
print("Harga                     : ", +(harga))
print("Jumlah Beli               : ", +(jumlah_beli))
print("---------------------------------------------")
print("Potongan yang didapat     : ", +(potongan))
print("Total Bayar               : ", +(total))
kembalian = int(input("Masukan Uang Bayar : "))
uang_kembalian= kembalian-total
print("Uang Kembalian            : ", +(uang_kembalian))