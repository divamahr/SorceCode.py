# NIM/NAMA  : 16523197/Denaya Diva Insani
# Tanggal   : 2 November 2023
# Deskripsi : Membuat 2 Matirks dan Menentukan Apakah Sama Bentuk dan Isinya

# PROGRAM Menentukan Apakah 2 Matriks Sama Bentuk dan Isinya

# KAMUS
# M1, M2        = matriks of integer
# Nbrs1, Nbrs 2 = variabel baris, integer
# Nkol1, Nkol2  = variabel kolom, integer

# ALGORITMA
# Input
Nbrs1 = int(input(f'Masukkan banyaknya baris M1: '))
Nkol1 = int(input(f'Masukkan banyaknya kolom M1: '))

# Membuat dan Mengisi Matriks M1
M1 = [[0 for j in range (Nkol1)] for i in range (Nbrs1)]
for i in range (Nbrs1):
    for j in range (Nkol1):
        M1[i][j] = int(input(f'Masukkan nilai baris ke-{i+1} kolom ke-{j+1}: '))

# Mengeprint Matriks M1
print(f'Matriks M1')
for i in range (Nbrs1):
    for j in range (Nkol1):
        print (M1[i][j], end=" ")
    print()

print('='*7)        # Pemisah kedua matriks

# Input
Nbrs2 = int(input(F'Masukkan banyaknya baris M2: '))
Nkol2 = int(input(f'Masukkan banyaknya kolom M2: '))

# Membuat dan Mengisi Matriks M2
M2 = [[0 for j in range (Nkol2)] for i in range (Nbrs2)]
for i in range (Nbrs2):
    for j in range (Nkol2):
            M2[i][j] = int(input(f'Masukkan nilai baris ke-{i+1} kolom ke-{j+1}: '))

# Mengeprint Matriks M2
print(f'Matriks M2')
for i in range (Nbrs2):
    for j in range (Nkol2):
        print (M2[i][j], end=" ")
    print()

print('*'*7)        # Pemisah kedua matriks

# Output
print(f'Apakah kedua matriks sama?')
if (len(M1) != len(M2) and M1 != M2):
    print (f'Kedua matriks tidak sama.')
else:
    print(f'Kedua matriks sama.')

# Selesai