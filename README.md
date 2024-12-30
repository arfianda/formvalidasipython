# Form Validation Program

Sebuah program Python sederhana untuk memvalidasi input form pendaftaran online. Program ini memvalidasi nama lengkap, nomor telepon, dan alamat email berdasarkan kriteria tertentu.

## 📝 Deskripsi

Program ini dibuat untuk memvalidasi input form pendaftaran dengan kriteria berikut:
- Nama lengkap hanya boleh berisi huruf
- Nomor telepon hanya boleh berisi angka
- Email harus mengandung karakter '@' dan '.'

## 🚀 Fitur

- Validasi real-time untuk setiap input
- Pesan error yang spesifik untuk setiap jenis kesalahan
- Interface konsol yang user-friendly
- Penanganan error dan exception
- Menampilkan ringkasan data setelah validasi berhasil

## 💻 Persyaratan Sistem

- Python 3.x

## 📥 Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/username/form-validation.git
```

2. Pindah ke direktori project:
```bash
cd form-validation
```

## 🎯 Cara Penggunaan

1. Jalankan program dengan perintah:
```bash
python main.py
```

2. Ikuti instruksi yang muncul di layar:
   - Masukkan nama lengkap (hanya huruf)
   - Masukkan nomor telepon (hanya angka)
   - Masukkan alamat email (harus mengandung @ dan .)

3. Program akan memvalidasi setiap input dan menampilkan pesan error jika ada kesalahan

4. Jika semua input valid, program akan menampilkan ringkasan data

## 📋 Contoh Penggunaan

![](/img/contohformvalid.png)


## 📚 Fungsi-fungsi Utama

### `validate_name(name)`
- Memvalidasi nama yang hanya boleh berisi huruf
- Parameter: `name` (string)
- Return: `True` jika valid, `False` jika tidak

### `validate_phone(phone)`
- Memvalidasi nomor telepon yang hanya boleh berisi angka
- Parameter: `phone` (string)
- Return: `True` jika valid, `False` jika tidak

### `validate_email(email)`
- Memvalidasi email yang harus mengandung karakter @ dan .
- Parameter: `email` (string)
- Return: `True` jika valid, `False` jika tidak

### `get_user_input()`
- Mengambil dan memvalidasi input dari user
- Return: Dictionary berisi data yang telah divalidasi

## ⚠️ Penanganan Error

Program ini memiliki penanganan untuk beberapa jenis error:
- Input tidak valid (pesan error spesifik)
- Interupsi program (KeyboardInterrupt)
- Error tidak terduga (Exception umum)

![](/img/contohformtdkvalid.png)




