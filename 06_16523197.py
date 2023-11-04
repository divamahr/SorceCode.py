# NIM/NAMA  : 16523197/Denaya Diva Insani
# Tanggal   : 2 November 2023
# Deskripsi : Menentukan Aapakah Seluruh Value pada Array Bernilai Positif

# No.6
# PROGRAM Menentukan Seluruh Nilai Array Bernilai Positif

# KAMUS
# TI      = array
# i       = integer
# positif = inisialisasi i yag positif
# negatif = inisialisasi i yang negatif

# ALGORITMA
# Input pengisian array yang sudah dibuat
TI = 0
TI = [i for i in range (101)]
for i in range (10):                                     # Asumsi elemen array sudah 100 dan hanya 10 angka
    TI[i] = int(input(f'Masukkan elemen array ke-{i}: ')) # yang di-input

# Mengeprint Gambar Array TI
print (TI)

# Mencari elemen positif dan negatif
positif = 0
negatif = 0
for i in range (101):
    if (TI[i] >= 0):
        positif +=1
    else:
        negatif +=1

# Output
print(f'Banyaknya elemen positif: {positif}')
print(f'Banyaknya elemen negatif: {negatif}')

print('='*35)       # Pemisah kedua hasil print

print(f'Apakah semua elemen array positif?')
if (positif == 101):
    print(f'Semua elemen array positif.')
else:
    print(f'Tidak semua elemen array positif.')

# Selesai