# NIM/NAMA  : 16523197/Denaya Diva Insani
# Tanggal   : 2 November 2023
# Deskripsi : Apakah Matriks Segitiga Atas atau Bukan

# No.10
# PRGORAM Menentukan Matriks Segitiga Atas

# KAMUS
# M    = matriks of integer
# i, j = integer
# m, n = kolom, baris, integer

# ALGORITMA
# Input
Nbrs = int(input(f'Masukkan panjang baris: '))
Nkol = int(input(f'Masukkan panjang kolom: '))

# Proses
# Membuat Matriks
M = [[0 for j in range (Nkol)] for i in range (Nbrs)]
for i in range (Nbrs):
    for j in range (Nkol):
        M[i][j] = int(input(f'Masukkan nilai baris ke-{i+1} kolom ke-{j+1}: '))

# Mengeprint Gambar Matriks
for i in range (Nbrs):
    for j in range (Nkol):
        print (M[i][j], end=" ")
    print()

# Mengecek Panjang Baris dan Kolom
idle = True
if (Nbrs != Nkol):
    idle = False
else:
    idle = True

# Membuat Segitiga Atas
c = 0
for i in range (Nbrs):
    for j in range (Nkol):
        if (i > j and M[i][j] != 0):
            c = 1

# Output
if (c == 1 and idle == True):
    print (f'Matriks bukan matriks segitiga atas.')
elif (c == 1 or idle == False):
    print (f'Matriks bukan matriks segitiga atas.')
else:
    print (f'Matriks adalah matriks segitiga atas.')

# Selesai