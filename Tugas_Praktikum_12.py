# Nama : Muhammad Hanif Raharjo
# NPM : 2505060074
# Rombel : 4
# Link Tugas :

# Latihan

# a. Luas persegi panjang
def luas_persegi_panjang():
  print("menghitung luas persegi panjang")
  panjang = int(input("Panjang\t:"))
  lebar = int(input("Lebar\t:"))
  return panjang * lebar

# b. Volume balok
def volume_balok():
  print("menghitung volume balok")
  panjang = int(input("Panjang\t:")) 
  lebar = int(input("Lebar\t:"))
  tinggi = int(input("Tinggi\t:"))
  return panjang * lebar * tinggi

# c. Luas lingkaran
def luas_lingkaran():
  print("menghitung luas lingkaran")
  jari_jari = int(input("Jari-jari\t:"))
  return 3.14 * jari_jari**2

# d. Volume bola
def volume_bola():
  print("menghitung volume bola")
  jari_jari = int(input("Jari-jari\t:"))
  return .75 * 3.14 * jari_jari**3

print(luas_lingkaran())
