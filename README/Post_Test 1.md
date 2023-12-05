# Post test

## Soal
Buatlah package berisi perhitungan luas dan volume, dan lengkapi lah script main.py sehingga bisa memenuhi input dan output, gunakan skema yang telah dipelajari pada pertemuan ini.
Hanya boleh menambah 1 Class pada main.py

main.py
```python
# import package

if __name__ == "__main__":
    # lengkapi sesuai kebutuhan, memerlukan import dari package
    tipe = input('Pilihlah Jenis Perhitungan (luas, volume): ')
    jenis_bentuk = {} 
    print("Opsi Bentuk >>", jenis_bentuk)
    bentuk = input('Pilihlah Jenis Bentuk: ')

    # input sisi atau panjang tertentu berdasarkan bentuk, tipe float, maksimal input-output 2 digit dibelakang koma

    # output result, ganti param sesuai tipe dan bentuk 
    print(f"{tipe} {bentuk} dengan {param}: {result}")
```

## Sample
sample 1:
```
Pilihlah Jenis Perhitungan (luas, volume): luas
Opsi Bentuk >> lingkaran, persegi, segitiga
Pilihlah Jenis Bentuk: persegi
Sisi pertama: 5
Sisi kedua: 5

Luas Persegi dengan sisi 5 dan 5: 25
```

sample 2:
```
Pilihlah Jenis Perhitungan (luas, volume): volume
Opsi Bentuk >> bola, kubus, silinder
Pilihlah Jenis Bentuk: bola
Radius: 49 


Volume Bola dengan radius 44: 4188.79
```

## Catatan
Semakin banyak implemantasi dari materi hari ini, nilai akan semakin maksimum




