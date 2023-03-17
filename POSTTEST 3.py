import os


def skip():
    sekip = input("\n\nTekan enter untuk melanjutkan ")

class node:
    def __init__(self, data = None, nextNode = None):
        self.roti = data["roti"]
        self.harga = data["harga"]
        self.nextNode = nextNode

class linkedlist:
    def __init__(self):
        self.head = None

    def tambahdata(self, data):
        newNode = node(data)
        newNode.nextNode = self.head
        self.head = newNode

    def lihatdata(self):
        currentNode = self.head
        if self.head is None:
            print("Data Masih Kosong")
        else:
            print('''
 ===============================
|          DAFTAR MENU          |
 ===============================
''')
            while currentNode is not None:
                print("   Roti  : {} \n   Harga : {}".format(currentNode.roti, currentNode.harga))
                if currentNode.nextNode is not None:
                    print("")
                currentNode = currentNode.nextNode

    def hapusdata(self):
        if self.head == None:
            print("Data Masih Kosong")
            skip()
            os.system("cls")
            return
        else:
            roti = input(">> Masukkan nama roti yang ingin dihapus: ")
            os.system("cls")
            currentNode = self.head
            if self.head.roti == roti:
                self.head = self.head.nextNode
                print("Data {} berhasil dihapus".format(roti))
                skip()
                os.system("cls")
                return
            else:
                self.head.roti != self.head
                print("Mohon Mengulang Kembali")
                skip()
                os.system("cls")

    def menu(self):
        while True:
            print('''
             =============================================
             |                MENU PILIHAN               |
             |-------------------------------------------|
             |  1. Tambah Data                           |
             |  2. Lihat Data                            |
             |  3. Hapus Data                            |
             |  4. Keluar                                |
             =============================================
            ''')
            tanya = input(">> Masukkan pillihan menu: ")
            os.system("cls")
            if tanya == "1":
                roti = str(input(">> Masukkan nama roti  : "))
                harga = int(input(">> Masukkan harga roti : "))
                self.tambahdata({
                    "roti": roti,
                    "harga": harga})
                os.system("cls")
                print("Data Berhasil Ditambahkan!")
                skip()
                os.system("cls")
            elif tanya == "2":
                self.lihatdata()
                skip()
                os.system("cls")
            elif tanya == "3":
                self.hapusdata()
            elif tanya =="4":
                print("Terima Kasih")
                break
            else:
                print("KESALAHAN")
try:
    if __name__ == "__main__":
        l = linkedlist()
        l.menu()
except ValueError:
    os.system("cls")
    print("KESALAHAN, MOHON COBA LAGI")