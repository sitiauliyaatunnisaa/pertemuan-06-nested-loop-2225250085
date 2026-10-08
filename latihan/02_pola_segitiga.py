# Loop luar menentukan jumlah baris.
# Loop dalam mencetak simbol * sebanyak nomor baris.
# Kondisi tidak digunakan karena jumlah simbol ditentukan oleh range.
# Counter tidak diperlukan.
# Output berupa pola segitiga bintang.

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()