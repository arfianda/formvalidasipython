def validate_name(name):
    """Validasi nama yang hanya boleh berisi huruf."""
    return name.replace(" ", "").isalpha()

def validate_phone(phone):
    """Validasi nomor telepon yang hanya boleh berisi angka."""
    return phone.isdigit()

def validate_email(email):
    """Validasi email yang harus mengandung karakter @ dan ."""
    return '@' in email and '.' in email

def get_user_input():
    """Fungsi untuk mendapatkan input dari user dan melakukan validasi."""
    print("\n=== Form Pendaftaran Online ===")
    
    # Input dan validasi nama
    while True:
        nama = input("\nMasukkan nama lengkap: ").strip()
        if validate_name(nama):
            break
        print("Error: Nama hanya boleh berisi huruf!")
    
    # Input dan validasi nomor telepon
    while True:
        telepon = input("Masukkan nomor telepon: ").strip()
        if validate_phone(telepon):
            break
        print("Error: Nomor telepon hanya boleh berisi angka!")
    
    # Input dan validasi email
    while True:
        email = input("Masukkan email: ").strip()
        if validate_email(email):
            break
        print("Error: Email harus mengandung karakter @ dan .")
    
    return {
        'nama': nama,
        'telepon': telepon,
        'email': email
    }

def main():
    """Fungsi utama program."""
    try:
        # Mendapatkan input user dengan validasi
        data = get_user_input()
        
        # Menampilkan hasil
        print("\n=== Hasil Validasi ===")
        print("Data pendaftaran valid!")
        print("\nDetail data:")
        print(f"Nama    : {data['nama']}")
        print(f"Telepon : {data['telepon']}")
        print(f"Email   : {data['email']}")
        
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    main()