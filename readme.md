# PA K11 ASD

Kalengkongan John Derby (2209116061)
Zamzam Muazam (2209116081)
Syahfi Rizqi (2209116093)

Program ini merupakan program toko workshop online sederhana yang memungkinkan pengguna untuk membeli barang dan mengecek saldonya, sedangkan administrator dapat menambah, melihat, memperbarui, mencari, dan menghapus barang.

## Prasyarat
Python 3.x
prettytable
pwinput
mysql-connector-python

## Mulai

Instal prasyarat yang tercantum di atas.
Unduh file kode program.
Jalankan program menggunakan Python.

## Cara Penggunaan
1. Saat program dimulai, pengguna dapat memilih untuk masuk sebagai pelanggan atau administrator.
2. Pelanggan dapat membeli item dan memeriksa saldo mereka.
3. Administrator dapat menambah, melihat, memperbarui, mencari, dan menghapus item.
4. Program menyimpan data dalam daftar tertaut dan database SQL.
5. Program ini juga membuat file invoice.txt untuk setiap pembelian.

## Class dan Function
**Class Barang**
Class ini mewakili item dalam inventaris. Ini memiliki atribut berikut:

- id_barang: Pengidentifikasi unik item
- nama_barang: Nama barang
- harga: Harga barang
berikutnya: Referensi ke item berikutnya dalam daftar tertaut
### Class LinkedList
Class ini mewakili inventaris sistem toko online. Ini memiliki atribut berikut:

- head : Referensi ke item pertama dalam linked list
- saldo : Saldo akun pengguna saat ini
### Ini memiliki metode berikut:

- tambah_barang: Menambahkan item baru ke inventaris
- tampilan_barang : Menampilkan tabel semua item yang ada di inventory
- update_barang: Memperbarui detail item dalam inventaris
- cari_barang: Mencari item dalam inventaris berdasarkan ID-nya
- hapus_barang: Menghapus item dari inventaris
- membeli: Memungkinkan pengguna untuk membeli item dari inventaris

### fungsi menu_user
Fungsi ini mewakili antarmuka pengguna dari sistem toko online. Ini menampilkan menu opsi untuk dipilih pengguna, termasuk membeli item dan memeriksa saldo akun mereka.

### menu_admin Fungsi
Fungsi ini mewakili antarmuka administrator dari sistem toko online. Ini menampilkan menu opsi untuk dipilih administrator, termasuk menambahkan, memperbarui, dan menghapus item dari inventaris.

### Catatan
Ini adalah program yang disederhanakan dan tidak boleh digunakan dalam situasi kehidupan nyata. Ini hanya dimaksudkan untuk tujuan pembelajaran.
