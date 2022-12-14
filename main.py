"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama / sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata : "Pergi ke toko.')
print('Budi menjawab : "Baik, apa yang harus saya lakukan di toko."')
print('Ibu menjawab : "Beli satu botol susu, dan jika ada telor beli 6."')
print("Maka Budi berangkat ke toko.")
print("Dan mulai berbelanja.")

# Percabangan
jumlah_botol_susu = 27
jumlah_telur = 547
print(f"Jumlah botol susu di toko {jumlah_botol_susu} botol")
print(f"Jumlah telur di toko {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup.")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu.")
    else:
        print("Budi membeli 1 botol susu & 6 butir telur")
else:
    print("Budi tidak membeli 1 botol susu.")

print("Budi pulang ke rumah.")
print("Menyampaikan hasil belanja kepada Ibu.")
