# Loop luar mengatur nilai i dari 1 sampai n.
# Loop dalam mengatur nilai j dari 1 sampai n.
# Kondisi memeriksa apakah i + j <= n.
# Counter count menghitung pasangan yang memenuhi kondisi.
# Output menampilkan banyak pasangan yang memenuhi syarat.

n = int(input("n: "))
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")