# Nama = Muhammad Hanif Raharjo
# NPM = 2505060074
# Rombel = 4

# Latihan

# 1. Buah buahan
buah = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang']

# a. Tambahkan 'semangka' di akhir list
buah.append('semangka') 
print(buah) 
# ['apel', 'mangga', 'jeruk', 'anggur', 'pisang', 'semangka']

# b. Sisipkan 'durian' di antara 'jeruk' dan 'anggur'
buah.insert(3, 'durian') 
print(buah) 
# ['apel', 'mangga', 'jeruk', 'durian', 'anggur', 'pisang', 'semangka']

# c. Hapus 'mangga' dari list
buah.remove('mangga') 
print(buah) 
# ['apel', 'jeruk', 'durian', 'anggur', 'pisang', 'semangka']

# d. Ubah 'pisang' menjadi 'nanas'
buah[-2] = 'nanas'
print(buah) 
# ['apel', 'jeruk', 'durian', 'anggur', 'nanas', 'semangka']

# e. Tampilkan 3 buah pertama
print(buah[:3]) # ['apel', 'jeruk', 'durian']

# 2. Mengurutkan angka
angka = [45, 12, 78, 23, 56, 89, 34]

# a. Urutkan secara ascending
angka.sort() 
print(angka) # [12, 23, 34, 45, 56, 78, 89]

# b. Urutkan secara descending
angka.reverse()
print(angka) # [89, 78, 56, 45, 34, 23, 12]
