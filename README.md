# Pertemuan 06 Nested Loop Python

**Algoritma dan Pemrograman | Pertemuan 06**

Nama: Siti Auliyaatunnisaa  
NIM: 2225250085  
Kelas: 3A  

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan

Untuk menjalankan program Tugas 3, gunakan perintah:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

Program menerima input `n` berupa bilangan bulat positif. Jika `n <= 0`, program akan meminta input kembali sampai mendapatkan nilai positif.

Loop luar digunakan untuk menentukan baris tabel perkalian dari `1` sampai `n`.

Loop dalam digunakan untuk menentukan kolom dari `1` sampai `n` dan menghitung hasil perkalian `i * j`.

Akumulator `total_baris` digunakan untuk menghitung jumlah seluruh hasil perkalian pada setiap baris. Nilainya direset menjadi `0` pada setiap awal baris.

Akumulator `total_semua` digunakan untuk menghitung jumlah seluruh hasil perkalian dalam tabel. Nilainya tidak direset pada setiap baris karena harus mencakup seluruh hasil perkalian.

Counter `count_genap` digunakan untuk menghitung banyak hasil perkalian yang bernilai genap. Counter bertambah satu apabila `hasil % 2 == 0`.

## Hasil Pengujian

### Test Case 1

**Input:**
```text
n = 1
```

**Hasil yang diharapkan:**
```text
Total semua = 1
Banyak hasil genap = 0
```

**Keluaran aktual:**
```text
1
Jumlah baris 1 = 1
Total keseluruhan = 1
Banyak hasil genap = 0
```

**Status:** Berhasil

### Test Case 2

**Input:**
```text
n = 2
```

**Hasil yang diharapkan:**
```text
Total semua = 9
Banyak hasil genap = 3
```

**Keluaran aktual:**
```text
1    2
Jumlah baris 1 = 3
2    4
Jumlah baris 2 = 6
Total keseluruhan = 9
Banyak hasil genap = 3
```

**Status:** Berhasil

### Test Case 3

**Input:**
```text
n = 3
```

**Hasil yang diharapkan:**
```text
Total semua = 36
Banyak hasil genap = 5
```

**Keluaran aktual:**
```text
1    2    3
Jumlah baris 1 = 6
2    4    6
Jumlah baris 2 = 12
3    6    9
Jumlah baris 3 = 18
Total keseluruhan = 36
Banyak hasil genap = 5
```

**Status:** Berhasil

### Ringkasan Pengujian

| Input | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status |
|---|---:|---:|---:|---|
| n = 1 | 1 | 1 | 0 | Berhasil |
| n = 2 | 4 | 9 | 3 | Berhasil |
| n = 3 | 9 | 36 | 5 | Berhasil |

## Analisis Efisiensi

Loop luar berjalan sebanyak `n` kali. Untuk setiap satu iterasi loop luar, loop dalam berjalan sebanyak `n` kali.

Dengan demikian, badan loop dalam berjalan sebanyak:

```text
n × n = n²
```

Contohnya, untuk `n = 3`, badan loop dalam berjalan sebanyak:

```text
3 × 3 = 9 kali
```

Untuk `n = 5`:

```text
5 × 5 = 25 kali
```

Jadi, semakin besar nilai `n`, semakin banyak operasi yang dilakukan. Kompleksitas waktu utama program adalah `O(n²)`.

## Refleksi

Salah satu kesalahan yang dapat terjadi dalam nested loop adalah salah menempatkan `total_baris = 0`. Jika `total_baris` diletakkan di luar loop luar, jumlah hasil perkalian dari baris sebelumnya akan ikut terbawa ke baris berikutnya.

Kesalahan tersebut diperbaiki dengan meletakkan `total_baris = 0` di dalam loop luar dan sebelum loop dalam dimulai. Dengan demikian, setiap baris memiliki perhitungan jumlah yang dimulai kembali dari `0`.

Contoh penempatan yang benar:

```python
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        total_baris += hasil
```

Dengan struktur tersebut, jumlah setiap baris dapat dihitung secara terpisah dan hasil akhirnya sesuai dengan yang diharapkan.