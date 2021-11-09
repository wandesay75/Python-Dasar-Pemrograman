kode_baju = input("Masukan kode baju [PA/BS/AD]       : ")
ukuran    = input("Masukan ukuran baju [XXL/XL/L/M/S] : ")

if kode_baju == "PA" or kode_baju == "pa":
    merk = "Palm Angels"
    if ukuran == 'S' or ukuran == 's':
        harga = 550000
    elif ukuran == 'M' or ukuran == 'm':
        harga = 650000
    elif ukuran == 'L' or ukuran == 'l':
        harga = 750000
    elif ukuran == 'XL' or ukuran == 'xl':
        harga = 850000
    elif ukuran == 'XXL' or ukuran == 'xxl':
        harga = 950000
    else:
        print("maaf! ukuran tidak tersedia :( ")
elif kode_baju == "BS" or kode_baju == "bs":
    merk = "Bape Shark"
    if ukuran == 'S' or ukuran == 's':
        harga = 850000
    elif ukuran == 'M' or ukuran == 'm':
        harga = 950000
    elif ukuran == 'L' or ukuran == 'l':
        harga = 1050000
    elif ukuran == 'XL' or ukuran == 'xl':
        harga = 1150000
    elif ukuran == 'XXL' or ukuran == 'xxl':
        harga = 1250000
    else:
        print("maaf! ukuran tidak tersedia :( ")
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == 'S' or ukuran == 's':
        harga = 1050000
    elif ukuran == 'M' or ukuran == 'm':
        harga = 1150000
    elif ukuran == 'L' or ukuran == 'l':
        harga = 1250000
    elif ukuran == 'XL' or ukuran == 'xl':
        harga = 1350000
    elif ukuran == 'XXL' or ukuran == 'xxl':
        harga = 1450000
    else:
        print("maaf! ukuran tidak tersedia :( ")
else:
    print("maaf! merk tidak tersedia :( ")

print("--------------------------------------------")
print("Merk Baju  :" +str(merk))
print("Harga Baju : Rp." ,harga)