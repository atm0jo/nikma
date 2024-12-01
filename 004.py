# To-Do List sederhana menggunakan Python
# Data disimpan dalam file `tasks.txt`

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Memuat daftar tugas dari file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file]

def save_tasks(tasks):
    """Menyimpan daftar tugas ke file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Menampilkan daftar tugas."""
    if not tasks:
        print("\nTidak ada tugas saat ini.\n")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Menambahkan tugas baru."""
    task = input("Masukkan tugas baru: ").strip()
    if task:
        tasks.append(task)
        print(f"Tugas '{task}' berhasil ditambahkan!\n")
    else:
        print("Tugas tidak boleh kosong!\n")

def delete_task(tasks):
    """Menghapus tugas berdasarkan nomor."""
    try:
        display_tasks(tasks)
        num = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            print(f"Tugas '{removed_task}' berhasil dihapus!\n")
        else:
            print("Nomor tugas tidak valid!\n")
    except ValueError:
        print("Harap masukkan nomor yang valid!\n")

def main():
    """Fungsi utama."""
    tasks = load_tasks()
    while True:
        print("=== Aplikasi To-Do List ===")
        print("1. Tampilkan daftar tugas")
        print("2. Tambah tugas baru")
        print("3. Hapus tugas")
        print("4. Keluar")
        choice = input("Pilih menu (1-4): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.\n")

if __name__ == "__main__":
    main()
