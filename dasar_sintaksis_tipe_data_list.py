daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print(daftar_buku)

print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematik Kelas 5')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list daftar_buku')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print(f'\nBuku yang diambil tadi adalah {buku}')

print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.pop(-3)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

