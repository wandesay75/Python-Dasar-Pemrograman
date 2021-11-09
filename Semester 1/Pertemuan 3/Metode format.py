#menggunakan posisi default
default_order = "{}, {}, {} dan {}". format("Alvin", "Haikal", "Adit", "Raihan")
print('\n--- Urutan Default ---')
print(default_order)

#menggunakan argument posisi
positional_order = "{2}, {3}, {1} dan {0}". format("Alvin", "Haikal", "Adit", "Raihan")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)
print("\n-+-+--+-+--+-+--+-+--+-+--+-+-")

#format interger
print("{0} bila diubah jadi biner menjadi {0:b}". format(69))

#format float
print("Format eksponensial: {0:e}". format(3.14432352))

#pembulatan
print("Seperempat sama dengan: {0:.4f}". format(1/4))

#meratakan string
print("|{:<5}|{:^10}|{:>5}|". format('Aku', 'Kamu', 'Dia'))