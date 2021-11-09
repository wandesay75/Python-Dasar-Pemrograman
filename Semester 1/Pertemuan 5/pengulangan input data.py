ulang=2

for a in range(ulang):
    print ("data Ke - " + str(a+1))
    nama=input("Masukkan NIM anda          : ")
    uts=int(input("Masukkan Nilai UTS anda : "))
    uas=int(input("Masukkan Nilai UAS anda : "))
    print("NIM anda adalah %s nilai UTS anda %i nilai UTS anda %i" % (nama,uts,uas))
    print("-------------------------------------\n")