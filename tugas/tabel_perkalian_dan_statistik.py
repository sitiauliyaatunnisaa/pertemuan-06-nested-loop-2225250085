print("Tabel Perkalian dan Statistik")

# Validasi input agar n harus berupa bilangan bulat positif.
n = int(input("n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# total_semua menyimpan jumlah seluruh hasil perkalian.
# count_genap menghitung banyak hasil perkalian yang genap.
total_semua = 0
count_genap = 0

# Loop luar mengatur baris tabel.
for i in range(1, n + 1):
    # Reset jumlah baris untuk setiap baris baru.
    total_baris = 0

    # Loop dalam mengatur kolom tabel.
    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        # Menambahkan hasil ke jumlah baris dan total keseluruhan.
        total_baris += hasil
        total_semua += hasil

        # Menghitung banyak hasil yang genap.
        if hasil % 2 == 0:
            count_genap += 1

    print()
    print(f"Jumlah baris {i} = {total_baris}")

# Menampilkan statistik setelah seluruh tabel selesai.
print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")