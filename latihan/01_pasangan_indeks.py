# Loop luar mengatur nilai i dari 1 sampai 3.
# Loop dalam mengatur nilai j dari 1 sampai 4 untuk setiap i.
# Counter count menghitung banyak seluruh pasangan (i, j).
# Output menampilkan setiap pasangan dan jumlah pasangan.

count = 0

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")