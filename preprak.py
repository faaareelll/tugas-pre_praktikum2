# 1. 
# Fungsi untuk menambahkan pengeluaran baru ke dalam list expenses
def add_expense(expenses, date, description, amount):
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    updated_expenses = expenses + [new_expense]  # Membuat list baru dengan menambahkan pengeluaran baru
    return updated_expenses  # Mengembalikan list pengeluaran yang sudah diperbarui

# 2. 
# Lambda expression untuk menghitung total pengeluaran harian
calculate_total_expenses = lambda expenses: sum(expense['jumlah'] for expense in expenses)
# menghitung jumlah pengeluaran dari list pengeluaran

# 3.
#  Fungsi untuk menyaring pengeluaran berdasarkan tanggal tertentu Menggunakan list comprehension
def get_expenses_by_date(expenses, date):
    return [expense for expense in expenses if expense['tanggal'] == date] 
# bisa dibilang jika pengeluaran berada di dalam list dan sesuai dengan tanggal maka data akan ditampilkan

# 4.
#  Fungsi generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string
def generate_expenses_report(expenses):
    for expense in expenses:
        yield f"Tanggal: {expense['tanggal']}, Deskripsi: {expense['deskripsi']}, Jumlah: Rp {expense['jumlah']}"
# Generator menghasilkan nilai secara bertahap saat dipanggil dan lebih cepat daripada list comprehension

# Lambda function untuk mendapatkan input dari pengguna
get_user_input = lambda command: int(input(command))

# Fungsi untuk menambahkan pengeluaran secara interaktif
def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    return add_expense(expenses, date, description, amount)  # Memanggil fungsi add_expense

# Fungsi untuk melihat pengeluaran berdasarkan tanggal
def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)  # Memanggil fungsi get_expenses_by_date
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")

# Fungsi untuk melihat laporan pengeluaran harian
def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)  # Memanggil fungsi generate_expenses_report
    for entry in expenses_report: # maka dari itu menggunakan perulangan for untuk menampilkan seluruh datanya
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

# Fungsi utama
def main():
    global expenses  # Variabel global untuk menyimpan pengeluaran
    expenses = [  # Inisialisasi pengeluaran
        {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
        {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
        {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
    ]

    while True:
        display_menu()  
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")  
        if choice == 1:
            expenses = add_expense_interactively(expenses)  
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)  
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)  
        elif choice == 4:
            view_expenses_report(expenses)  
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break  
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()  
