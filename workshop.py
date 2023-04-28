from prettytable import PrettyTable
import pwinput
import mysql.connector


class Barang:
    def __init__(self, id_barang, nama_barang, harga):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.saldo = 20000000

    def tambah_barang(self, id_barang,  nama_barang, harga):
        new_barang = Barang(id_barang,  nama_barang, harga)

        if not self.head:
            self.head = new_barang
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_barang

    def tampilan_barang(self):
        if not self.head:
            print("Tidak ada data barang yang terdaftar.")
        else:
            aa = 1
            current = self.head 
            table = PrettyTable(["NO","ID", "Nama", "Harga"])
            while current is not None:
                table.add_row([aa,current.id_barang,current.nama_barang, current.harga])
                aa += 1
                current = current.next
            print(table)

    def update_barang(self, id_barang,  nama_barang, harga):
        barang = self.cari_barang(id_barang)
        if barang:
            barang.id_barang = id_barang
            barang.nama_barang = nama_barang
            barang.harga = harga
            print("Data barang berhasil diupdate!")
        else:
            print("Barang dengan ID barang tersebut tidak ditemukan")

    def cari_barang(self, id_barang):
        current = self.head
        if self.head is None:  # cek apakah list kosong
            return None
        while current is not None:
            if current.id_barang == id_barang:
                return current
            current = current.next
        return None


    def hapus_barang(self, id_barang):
        current = self.head
        if current and current.id_barang == id_barang:
            self.head = current.next
            current = None
            print("Data barang berhasil dihapus")
            return
        prev = None
        while current and current.id_barang != id_barang:
            prev = current
            current = current.next
        if current is None:
            print("Barang dengan ID barang tersebut tidak ditemukan")
            return
        prev.next = current.next
        current = None
        print("Data barang berhasil dihapus!")

    def membeli(self):
        if not self.head:
            print("tidak ada menu yang tersedia")
            return
        
        print("pilih menu yang akan di beli: ")
        self.tampilan_barang()
        pilihan = input("Masukan NO Barang: ")

        try:
            pilihan = int(pilihan)
        except ValueError:
            print("masukan tidak ada")
            return
        
        beli=self.head
        i = 1
        while beli:
            if i == pilihan:
                if self.saldo < int(beli.harga):
                    print("saldo anda tidak cukup")
                    return
                hasil = input(f"masukan berapa {beli.nama_barang} yang akan di beli: ")
                try:
                    hasil = int(hasil)
                except ValueError:
                    print("masukan tidak ada")
                    return
                if hasil <=0:
                    print("jumlah tidak ada")
                    return
                if self.saldo < beli.harga *hasil:
                    print("saldo anda tidak cukup")
                    return
                self.saldo -= beli.harga *hasil
                print(f"anda telah membeli {hasil} {beli.nama_barang}. sisa saldo anda : {self.saldo}")

                #invoice
                with open("invoice.txt","w") as f:
                    f.write(f" invoice pembelian {beli.nama_barang}\n")
                    f.write(f"hasil:{hasil}\n")
                    f.write(f"Harga Satuan {beli.harga}\n")
                    f.write(f"Total Harga {beli.harga *hasil}\n")

                return
            beli = beli.next
            i += 1

        print("Nomor menu yang dimasukan tidak valid")


    


data = LinkedList()

def  menu_user():
    while True:
        print("""   
       
              work shop online               
         1.Membeli Barang      
         2.cek saldo
         3.Keluar  

       
        """)

        pilih1 = input("masukan pilihan anda :")

        if pilih1 == "1":          
            data.membeli()



        if pilih1 == "7":
            break


def  menu_admin():
    while True:
        print("""   
       
              work shop online               
         1.TAMBAH BARANG       
         2.TAMPILAN BARANG     
         3.UPDATE BARANG      
         4.CARI BARANG         
         5.HAPUS BARANG        
         6.KELUAR 
         7. KELUAR DARI ADMIN

       
        """)

        pilih = input("masukan pilihan anda :")

        if pilih == "1":
            id_barang   = input("masukan id barang    : ")
            nama_barang = input("masukan nama barang  : ")
            harga       = input("masukan harga barang : ")
            data.tambah_barang(id_barang,  nama_barang, harga)
            print("data barang berhasil ditambahkan!")

        elif pilih == "2":
            data.tampilan_barang()


        elif pilih == "3":
            data.tampilan_barang()
            id_barang = input("masukan ID barang yang anda ingin update :")
            barang = data.cari_barang(id_barang)
            if barang:
                id_baru     = input("masukan ID barang baru    :")
                nama_baru   = input("masukan nama barang baru  :")
                harga_baru  = input("masukan harga baru        :")
                barang.id_barang   = id_baru
                barang.nama_barang = nama_baru
                barang.harga       = harga_baru
                data.update_barang(id_baru, nama_baru, harga_baru)
            else:
                print("barang dengan id barang tersebut tidak ditemukan")

        elif pilih == "4":
            data.tampilan_barang()
            inputcari = int(input("Masukkan ID Barang yang akan dicari: "))
            barang = data.cari_barang(inputcari)
            if barang:
                print(f"data barang dengan id {inputcari} ditemukan")
                print(f"id barang : {barang.id_barang}")
                print(f"nama barang : {barang.nama_barang}")
                print(f"harga : {barang.harga}")
            else:
                print(f"data barang dengan id barang {id_barang} tidak ditemukan.")


        elif pilih == "5":
            data.tampilan_barang()
            id_barang =int(input("masukan id barang jika ingin menghapus data barang :"))
            barang = data.cari_barang(id_barang)
            if barang:
                data.hapus_barang(id_barang)
            else:
                print(f"data barang dengan id barang {id_barang} tidak ditemukan")

        elif pilih == "6":
            raise SystemExit
        elif pilih =="7":
            break
        else:
            print("masukan yang benar")








# Koneksi ke database
def koneksi():
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host="db4free.net",
            user="sql12609714",
            password="gXtJ98hYHx",
            database="kelompok11"
            )
    except mysql.connector.Error as e:
        print(f"'Erorr: {e}")
    return mydb


def register_user():
    # Get user input
    cursor = mydb.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Insert user data into database
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (username, password) VALUES ( %s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    # Print success message
    print("User registration successful!")
    menu_login()

# Call the function to register a user
    register_user()
    



# Fungsi login user
def user_login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    # Query untuk memeriksa keberadaan username dan password di tabel user
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    user = cursor.fetchone()

    # Jika ditemukan user dengan username dan password yang sesuai
    if user:
        print("Login berhasil. Selamat datang, {}!".format(user[0]))
        menu_user()
    else:
        print("Login gagal. Silakan coba lagi.")

# Fungsi login admin
def admin_login():
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput("Masukkan password admin: ")

    # Query untuk memeriksa keberadaan username dan password di tabel admin
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    admin = cursor.fetchone()

    # Jika ditemukan admin dengan username dan password yang sesuai
    if admin:
        print("Login berhasil. Selamat datang, {}!".format(admin[0]))
        menu_admin()
    # else:
    #     print("Login gagal. Silakan coba lagi.")

    
mydb = koneksi()
# Main program

def menu_login():
    data.tambah_barang(111 , "kunci inggris", 15000)
    data.tambah_barang(333 , "kunci italia", 20000)
    data.tambah_barang(222 , "kunci puan", 100000)
    data.tambah_barang(444 , "kunci joko", 400000)
    while True:
        print("Selamat datang di program login.")
        print("Pilih opsi:")
        print("1. registrasi user")
        print("2. Login user")
        print("3. Login admin")

        choice = input("Masukkan pilihan: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_login()
        elif choice == "3":
            admin_login()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu_login()

