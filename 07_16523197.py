# NIM/NAMA  : 16523197/Denaya Diva Insani
# Tanggal   : 2 November 2023
# Deskripsi : Menentukan Nilai Maksimum dan Minimum

# PROGRAM Menentukan Nilai Maksimum dan Minimum melalui Input dari User

# KAMUS
# TI   = array
# i    = integer
# maks = inisialisasi i terbesar
# min  = inisialisasi i terkecil

# ALGORITMA
# Input pengisian array yang sudah dibuat
TI = 0
TI = [i for i in range (101)]                           
for i in range (10):                                      # Asumsi elemen array sudah 100 dan hanya 10 angka
    TI [i] = int(input(f'Masukkan elemen array ke-{i}: ')) # yang di-input

# Mengeprint Gambar Array
print(TI)

# Mencari nilai maksimum dan Minimium
maks = TI [0]
min = TI [0]
for i in range (101):
    if (TI[i] > maks):
        maks = TI [i]
    if (TI[i] < min):
        min = TI [i]

# Output
# Memberi pilihan kepada user
print (f'pilihlah angka berikut {0}, {1}, {2}!')
a = int(input(f'angka yang dipilih: '))

if (a == 0):
    print (f'nilai maksimumnya adalah {str(maks)} dan nilai minimumnya adalah {str(min)}.')
elif (a == 1):
    print (f'Nilai maksimumnya adalah {str(maks)}.')
elif (a == 2):
    print (f'nilai minimumnya adalah {str(min)}.')

# Selesai