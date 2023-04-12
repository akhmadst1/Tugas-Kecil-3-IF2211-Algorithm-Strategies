# Tucil3_Stima
Tugas Kecil 3 Strategi Algoritma
# Find The Shortest Path
Disusun untuk memenuhi Tugas Kecil 3 IF2211 Strategi Algoritma "Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan terpendek"

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Requirement Program](#requirement-program)
* [Cara Menyiapkan *Environment*](#cara-menyiapkan-environment)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Cara Menggunakan Program](#cara-menggunakan-program)
* [Author](#author)

## Deskripsi Singkat Program
Algoritma UCS (*Uniform cost search*) dan A* (atau *A star*) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, akan dibuat algoritma UCS dengan bahasa python

## Requirement Program
* Python versi 3.8.5 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.
* Virtual Environment
* Flask

## Cara Menyiapkan Environment dan Menjalankan Program
1. Pastikan Python versi 3.8.5 atau lebih baru sudah terpasang pada komputer (Anda dapat mengecek versi Python dengan menjalankan command py --version pada *command prompt*).
2. Lakukan instalasi semua library yang digunakan pada program library yang digunakan adalah Virtual Environment dan Flask.
Menyiapkan virtual environment:
```bash
pip install virtualenv
python -m venv env
```

Dari directory utama repository ini, aktifkan virtual environment:
Pada UNIX
```bash
source env/Scripts/activate
```
Pada Windows
```bash
env/Scripts/activate.bat
```

Install Flask dengan command sebagai berikut:
```bash
pip install flask
```

Untuk menyalakan program, masukkan command sebagai berikut:
Pada UNIX
```bash
export FLASK_APP=src/main.py
flask run
```
Pada Windows
```bash
set FLASK_APP=src/main.py
flask run
```

## Cara Menggunakan Program
1. Upload file.txt sesuai dengan format seperti yang terdapat pada folder `test`
2. Program akan meminta input file
3. Tentukan metode pencarian antara UCS dan A*
4. Apabila input file sudah benar, akan ditampilkan list of nodes
5. Jika program tidak ingin divisualisasikan dengan Google Maps, langsung loncat ke step 8
6. Jika ingin divisualisasikan, Flask akan berjalan pada http://127.0.0.1:5000/
7. Jalankan alamat Flask tersebut pada browser
8. Masukkan start dan end node yang ingin dikunjungi
9. Kemudian, program akan menunjukkan Shortest Path yang menunjukkan rute dengan lintasan terpendek serta jaraknya, dan visualisasinya dengan Google Maps (jika dipilih divisualisasikan)

## Authors

| Nama                  | NIM      |
| --------------------- | -------- |
| Maggie Zetta Rosida S | 13521117 |
| Akhmad Setiawan | 13521164 |
