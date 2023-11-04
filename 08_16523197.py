# NIM/NAMA  : 16523197/Denaya Diva Insani
# Tanggal   : 2 November 2023
# Deskripsi : Menentukan Apakah Panjang Array TI1 dan TI2 sama dan Mengisi Array 

# PROGRAM Panjang Array TI1 dan TI2 dan Mengisi Array

# KAMUS LOKAL
# BacaArray = nama prosedur
# arr       = parameter
# i         = integer

# Pendefinisian Prosedur
def BacaArray (arr):
    for i in range (10):
        arr[i] = int(input(f'Masukkan elemen array ke-{i}: '))  # Asumsikan elemen ada 100, dan di sini hanya 10-
                                                                # angka yang di-input

# KAMUS
# TI_1, TI_2 = Array of integer
# TI1 = variabel yang akan menghitung banyak elemen

# ALGORITMA
TI_1 = [i for i in range (101)]
TI_2 = [i for i in range (101)]

# Output
print("Masukkan elemen Array TI_1")
BacaArray (TI_1)
print("="*30)       # Pemisah kedua Input rrayA
print("Masukkan elemen Array TI_2")
BacaArray (TI_2)

print("Array TI_1")
print(TI_1)
print("="*30)       # Pemisah kedua Array
print("Array TI_2")
print(TI_2)

print("*"*30)       # Pemisah hasil print
if (TI_1 != TI_2):
    print(f'Array tidak sama.')
else:
    print(f'Array sama.')

# Selesai