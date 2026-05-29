import hashlib
import json
import os

FILE_USER = "users.json"

# Membuat file JSON jika belum ada
if not os.path.exists(FILE_USER):
    with open(FILE_USER, "w") as f:
        json.dump([], f)

# Fungsi hashing SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load data user
def load_users():
    with open(FILE_USER, "r") as f:
        return json.load(f)

# Simpan data user
def save_users(users):
    with open(FILE_USER, "w") as f:
        json.dump(users, f, indent=4)

# Registrasi user
def register():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    hashed_password = hash_password(password)

    users = load_users()

    # Cek username
    for user in users:
        if user["username"] == username:
            print("Username sudah digunakan!")
            return

    # Simpan user baru
    users.append({
        "username": username,
        "password": hashed_password
    })

    save_users(users)

    print("\n=== Registrasi Berhasil ===")
    print("Password Asli :", password)
    print("Hash SHA-256  :", hashed_password)

# Login user
def login():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    hashed_password = hash_password(password)

    users = load_users()

    for user in users:
        if user["username"] == username:

            print("\n=== Verifikasi Login ===")
            print("Hash Input :", hashed_password)

            if user["password"] == hashed_password:
                print("Status Login : BERHASIL")
            else:
                print("Status Login : GAGAL")

            return

    print("Username tidak ditemukan!")

# Menu utama
while True:
    print("\n=== LOGIN SHA-256 ===")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        register()

    elif pilihan == "2":
        login()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")