def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        print("\nMenampilkan Berbagai Bilangan")
        print("1. Menampilkan Bilangan Prima")
        print("2. Menampilkan Bilangan Ganjil")
        print("3. Menampilkan Bilangan Genap")
        print("0. Keluar")
        pilihMenu = input("Pilih Menu di atas: ")
        
        if pilihMenu == "1":
            try:
                Bilgn = int(input("Masukkan Bilangan: "))
                if is_prima(Bilgn):
                    print(f"{Bilgn} adalah bilangan prima.")
                else:
                    print(f"{Bilgn} bukan bilangan prima.")
            except ValueError:
                print("Input harus berupa angka!")
        
        elif pilihMenu == "2":
            try:
                Bilgn = int(input("Masukkan Bilangan: "))
                if Bilgn % 2 != 0:
                    print(f"{Bilgn} adalah bilangan ganjil.")
                else:
                    print(f"{Bilgn} bukan bilangan ganjil.")
            except ValueError:
                print("Input harus berupa angka!")
        
        elif pilihMenu == "3":
            try:
                Bilgn = int(input("Masukkan Bilangan: "))
                if Bilgn % 2 == 0:
                    print(f"{Bilgn} adalah bilangan genap.")
                else:
                    print(f"{Bilgn} bukan bilangan genap.")
            except ValueError:
                print("Input harus berupa angka!")
        
        elif pilihMenu == "0":
            print("Anda keluar dari program. Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Jalankan program
main()
