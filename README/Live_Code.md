# Live Code

## Petunjuk
1. Silahkan gunakan env masing-masing untuk menguji hasil
2. Tolong buat branch baru terlebih dahulu sebelum melakukan save file.
3. Tolong Dikerjakan di masing-masing folder yang telah disediakan, dan jangan menyentuh folder milik org lain
4. Jika sudah selesai bisa melakukan push


## Soal 1
Tolong Buat 1 script yang bisa menyelesaikan perhitungan harga barang dengan jika diinput menu barang sebagai berikut.

```json
"juice": 10000,
"soft_drink": 15000,
"chicken": 30000,
"beef": 45000,
"tea": 10000,
"desert": 25000
```

Contoh Input:
```
juice, tea, chicken, chicken, desert, tea, soft_drink
```

Contoh Output:
```
List Belanja:
    1 Juice @ 10000 = 10000
    2 Tea @ 10000 = 20000
    2 Chicken @ 30000 = 60000
    1 Desert @ 25000 = 25000
    1. Soft Dring @ 15000 = 15000

Total Harga: 130000
```
Ketentuan
- Code soal A: gunakan Decorator pada script
- Code soal B: gunakan Class pada script


## Soal 2
hasil fungsi harus positif dan tidak boleh error dalam return apapun.

Info: setiap fungsi memiliki attribute __name__

```python
def decorator():
    # Lengkapi

@decorator
def substract_between_number(num1, num2):
    selisih = num2 - num1 # selalu positif
    print(f"{num2} - {num1} = {selisih}")

def div_between_number(num1, num2):
    pembagian = num2 / num1 # selalu > 1
    print(f"{num2} / {num1} = {pembagian}")

div_between_number(5,4)
substract_between_number(5,4)

div_between_number(10,88)
substract_between_number(10,88)

div_between_number(87,50)
substract_between_number(87,50)

div_between_number(1,0)
substract_between_number(-1,0)
```


## Soal 3
Kamu memiliki object berupa seorang siswa dengan tiga atribut yang menggambarkan:
- Nama
- Nilai
- Absen

Seorang siswa akan dianggap lulus jika:
- Nilainya sama dengan atau lebih dari 75
- Jumlah absennya kurang dari 4 kali

Buatlah algoritma untuk:
1. input nama, nilai dan absen pada setiap siswa
2. menampilkan status setiap siswa (lulus atau tidak), beserta penyebabnya
3. menampilkan jumlah siswa yang lulus dan berapa yang tidak lulus
