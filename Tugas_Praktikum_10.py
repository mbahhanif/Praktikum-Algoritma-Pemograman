# Nama : Muhammad Hanif Raharjo
# NPM : 2505060074
# Rombel : 4
# Link Tugas : https://colab.research.google.com/drive/19vVKMe-rOMSpfb-2iuyJ2gze7oIrlX-y

# Latihan

# 1. Tuples
# a. buat tuple mahasiswa berisi data -> Nama, NIM, Prodi
data_tuple = ("Muhammad Hanif Raharjo", 2505060074, "Teknologi Informasi") 
print(f"NIM : {data_tuple[1]}, Prodi : {data_tuple[2]}") 
# NIM : 2505060074, Prodi : Teknologi Informasi

# 2. Dictionary
keranjang = {
  "apel": 5000,
  "pisang": 3000,
  "jeruk": 7000,
  "anggur": 15000
}
perulangan = 0
total = 0
for buah, harga in keranjang.items():
  print(f"Harga {buah} : Rp {harga}") 
  perulangan += 1
  print(f"perulangan ke {perulangan}") 
  total += harga
print(f"Harga {buah} : Rp {total}\n") 
