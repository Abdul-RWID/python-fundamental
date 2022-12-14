"""
Program perulangan membaca buku dengan while sampai paham
"""

book_count = 10
print('Ibu berkata, "Baca semua bukumu sampai paham"')

understood_count = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count} buku")

read_count = 0

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count} buku")

if understood_count == book_count:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku dipahami". Budi hanya paham {understood_count} buku')
