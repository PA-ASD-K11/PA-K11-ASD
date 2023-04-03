from prettytable import PrettyTable
import pwinput
import mysql.connector

class Barang:
    def __init__(self, id_barang, merk_barang, nama_barang, harga):
        self.id_barang = id_barang
        self.merk_barang = merk_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_barang(self, id_barang, merk_barang, nama_barang, harga):
        new_barang = Barang(id_barang, merk_barang, nama_barang, harga)

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
            current = self.head 
            table = PrettyTable(["ID", "Merk", "Nama", "Harga"])
            while current is not None:
                table.add_row([current.id_barang, current.merk_barang, current.nama_barang, current.harga])
                current = current.next
            print(table)

    def update_barang(self, id_barang, merk_barang, nama_barang, harga):
        barang = self.cari_barang(id_barang)
        if barang:
            barang.id_barang = id_barang
            barang.merk_barang = merk_barang
            barang.nama_barang = nama_barang
            barang.harga = harga
            print("Data barang berhasil diupdate!")
        else:
            print("Barang dengan ID barang tersebut tidak ditemukan")

    def cari_barang(self, id_barang):
        current = self.head
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

    


data = LinkedList()

def  menu():
    while True:
        print("""   
       
              work shop online               
         1.TAMBAH BARANG       
         2.TAMPILAN BARANG     
         3.UPDATE BARANG      
         4.CARI BARANG         
         5.HAPUS BARANG        
         6.KELUAR DARI ADMIN   
         7.KELUAR DARI PROGRAM 
       
        """)

        pilih = input("masukan pilihan anda :")

        if pilih == "1":
            id_barang   = input("masukan id barang    : ")
            merk_barang = input("masukan merek barang : ")
            nama_barang = input("masukan nama barang  : ")
            harga       = input("masukan harga barang : ")
            data.tambah_barang(id_barang, merk_barang, nama_barang, harga)
            print("data barang berhasil ditambahkan!")

        elif pilih == "2":
            data.tampilan_barang()


        elif pilih == "3":
            data.tampilan_barang()
            id_barang = input("masukan ID barang yang anda ingin update :")
            barang = data.cari_barang(id_barang)
            if barang:
                id_baru     = input("masukan ID barang baru    :")
                merk_baru   = input("masukan merek barang baru :")
                nama_baru   = input("masukan nama barang baru  :")
                harga_baru  = input("masukan harga baru        :")
                barang.id_barang   = id_baru
                barang.merk_barang = merk_baru
                barang.nama_barang = nama_baru
                barang.harga       = harga_baru
                data.update_barang(id_baru, merk_baru, nama_baru, harga_baru)
            else:
                print("barang dengan id barang tersebut tidak ditemukan")

        elif pilih == "4":
            id_barang = input ("masukan ID yang anda ingin dicari :")
            Barang = data.cari_barang(id_barang)
            if barang :
                print(f"data barang dengan id {id_barang} ditemukan")
                print(f"id barang : {barang.id_barang}")
                print(f"merk barang : {barang.merk_barang}")
                print(f"nama barang : {barang.nama_barang}")
                print(f"harga : {barang.harga}")
            else:
                print(f"data barang dengan id barang {id_barang} tidak ditemukan.")

        elif pilih == "5":
            data.tampilan_barang()
            id_barang = input("masukan id barang jika ingin menghapus data barang :")
            barang = data.cari_barang(id_barang)
            if barang:
                data.hapus_barang(id_barang)
            else:
                print(f"data barang dengan id barang {id_barang} tidak ditemukan")








# Koneksi ke database
mydb = mysql.connector.connect(
host="sql12.freesqldatabase.com",
user="sql12609714",
password="gXtJ98hYHx",
database="sql12609714"
)

def register_user():
    # Get user input
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
        print("Login berhasil. Selamat datang, {}!".format(user[1]))
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
        print("Login berhasil. Selamat datang, {}!".format(admin[1]))
        menu()
    else:
        print("Login gagal. Silakan coba lagi.")

    

# Main program

def menu_login_user():
    while True:
        print("Selamat datang di program login.")
        print("Pilih opsi:")
        print("1. registrasi user")
        print("2. Login user")
        print("3. Login admin")
        print("4. Keluar")

        choice = input("Masukkan pilihan: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_login()
        elif choice == "3":
            admin_login()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu_login_user()

def menu_login_admin():
    while True:
        print("selamat datang di login admin.")
        print("pilih opsi:")
        print("1. Login admin")
        print("2. keluar")

        x = input ("masukan pilihan :")
        
