# Mengambil input dari pengguna
nama = input("Masukkan nama lengkap: ")
umur = input("Masukkan umur: ")
alamat = input("Masukkan alamat: ")
hobi = input("Masukkan hobi: ")

# Menampilkan hasil menggunakan format()
output = "Nama saya adalah {}, saya berumur {} tahun, tinggal di {}, dan hobi saya adalah {}."
print(output.format(nama, umur, alamat, hobi))
