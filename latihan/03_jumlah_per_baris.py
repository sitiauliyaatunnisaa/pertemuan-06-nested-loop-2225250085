# Loop luar menentukan nomor baris i.
# Loop dalam menghitung hasil i * j pada setiap kolom.
# Akumulator total_baris menjumlahkan hasil pada satu baris.
# total_baris direset setiap kali memasuki baris baru.
# Output menampilkan jumlah setiap baris.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")