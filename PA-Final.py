# # Library / Module
# from prettytable import PrettyTable
# import csv
# import os
# import pwinput

# # Variabel 
# passReg = "9080"

# userBiasa = {"user" : ["wahyu", "riyandi", "rissa"],
#             "pCodeUser" : ["farmer1", "farmer2", "farmer2"]}

# superUser = {"userAdmin" : ["admin1", "admin2"],
#             "pCodeAdmin" : ["superuser1", "superuser2"]}

# dataTernak = [["Sapi", "12 Ekor", "1A"],
#             ["Kambing", "10 Ekor", "2A"],
#             ["Ayam", "90 Ekor", "3A"]]

# tableT = PrettyTable(["Nomor", "Jenis Hewan", "Jumlah Hewan", "Nomor Kandang"])
# tableT.title = "Data Peternakan"

# os.system("cls")

# # Fungsi Format CSV
# def laporan():
#     with open('laporan_ternak.csv', 'w', newline='') as csv_1:
#         csv_out = csv.writer(csv_1)
#         for a in range(0,len(dataTernak[0])):
#             csv_out.writerow([a+1, dataTernak[a][0], dataTernak[a][1], dataTernak[a][2]])

# # Fungsi CRUD
# # Fungsi Tampil Data (Read)
# def tabelTernak():
#     i = 0 
#     tableT.clear_rows()
#     for i in range(len(dataTernak)):
#         tableT.add_row([i+1, dataTernak[i][0], dataTernak[i][1], dataTernak[i][2]])
#         i+=1
#     print(tableT)

# # Fungsi Ubah Data (Update)
# def update(dataTernak):
#     tabelTernak()
#     data = int(input(">> Pilih nomor data yang ingin diubah : "))
#     ubahHewan = input(">> Masukkan Jenis Hewan baru : ")
#     ubahJumlah = input(">> Masukkan Jumlah baru : ")
#     ubahKandang = input(">> Masukkan Nomor Kandang Baru : ")
#     dataTernak[data-1] = [ubahHewan,ubahJumlah,ubahKandang]
#     tabelTernak()
#     menu()

# # Fungsi Tambah Data (Create)
# def create():
#     dataTernakBaru = []
#     hb = input("> Masukkan Hewan Baru : ")
#     dataTernakBaru.append(hb)
#     jb = input("> Masukkan Jumlah Baru : ")
#     dataTernakBaru.append(jb)
#     nkb = input("> Masukkan Nomor Kandang Baru : ")
#     dataTernakBaru.append(nkb)
#     dataTernak.append(dataTernakBaru)

# # Fungsi Hapus Data (Delete)
# def delete(dataTernak, tabelTernak):
#         tabelTernak()
#         print()
#         print(">> Pilih Nomor Data Yang Akan Hapus ")
#         src = int(input(">> Masukkan Nomor Data : "))
#         del dataTernak[src-1] 
#         tabelTernak()

# # Fungsi Register Akun Admin / User
# def registerAkun():
#     print("="*10, "PILIH TIPE AKUN".center(30), "="*10)
#     print("(1.) Admin")
#     print("(2.) User")
#     akun = input("Pilih tipe akun yang ingin dibuat   : ")
#     if akun == "1":
#         ul = "ya"
#         while (ul == "ya"):
#             print('=' * 52)
#             adminBaru = input("Masukkan Username Admin Yang Anda Inginkan : ")
#             if adminBaru in superUser.get("userAdmin"):
#                 print("Maaf Username Yang Anda Pilih Sudah Terdaftar\nSilahkan Masukkan Username Yang Lain")
#                 registerAkun()
#             else:
#                 pcAdBaru = pwinput.pwinput(prompt = "Masukkan Passcode Anda : ")
#                 superUser.get("userAdmin").append(adminBaru)
#                 superUser.get("pCodeAdmin").append(pcAdBaru)
#                 print("Anda Telah Berhasil Register!!")
#                 print("Silahkan Coba Akun Baru")
#                 login()
#             break

#     elif akun == "2":
#         ul = "ya"
#         while (ul == "ya"):
#             print('=' * 52)
#             userBaru = input("Masukkan Username Yang Anda Inginkan : ")
#             if userBaru in userBiasa.get("user"):
#                 print("Maaf Username Yang Anda Pilih Sudah Terdaftar\nSilahkan Masukkan Username Yang Lain")
#                 registerAkun()
#             else:
#                 pcUsBaru = pwinput.pwinput(prompt = "Masukkan Passcode Anda : ")
#                 userBiasa.get("user").append(userBaru)
#                 userBiasa.get("pCodeUser").append(pcUsBaru)
#                 print("Anda Telah Berhasil Register!!")
#                 print("Silahkan Coba Akun Baru")
#                 login()
#             break
#     else:
#         print("Pilihan tidak tersedia!")
#         registerAkun()

# # Fungsi Menu Manipulasi Data Untuk Admin
# def menu():
#     print("="*52)
#     print("="*5, "MENU MANIPULASI DATA PETERNAKAN ".center(40), "="*5)
#     print("="*52)
#     print("(1.) Tampilkan Data Ternak")
#     print("(2.) Tambah Data Ternak")
#     print("(3.) Ubah Data Ternak")
#     print("(4.) Hapus Data Ternak")
#     print("(5.) Laporan Data Ternak CSV")
#     print("(6.) Kembali ke Login Page")
#     print("(7.) Keluar")
#     print()
#     print("="*52)
#     print("="*5, "TENTUKAN PILIHAN".center(40), "="*5)
#     print("="*52)
#     pils = input("> Masukkan Pilihan : ")
#     if pils == "1":
#         tabelTernak()
#         menu()
    
#     elif pils == "2":
#         create()
#         tabelTernak()
#         menu()
    
#     elif pils == "3":
#         update(dataTernak)
#         tabelTernak()
#         menu()

#     elif pils == "4":
#         delete(dataTernak, tabelTernak)
#         menu()
    
#     elif pils == "5":
#         laporan()
#         print("Laporan CSV Berhasil Dicetak!")
#         menu()
    
#     elif pils == "6":
#         login()

#     elif pils == "7":
#         print("="*5, " TERIMA KASIH ".center(40), "="*5)
#         exit()
    
#     else:
#         print("Pilihan tidak tersedia!")
#         menu()

# # Fungsi Menu Tampilan Data Untuk User
# def menuUser():
#     print("="*52)
#     print("="*5, "MENU DATA PETERNAKAN ".center(40), "="*5)
#     print("="*52)
#     print("(1.) Tampilkan Data Ternak")
#     print("(2.) Kembali ke login page")
#     print("(3.) Keluar")
#     print()
#     print("="*52)
#     print("="*5, "TENTUKAN PILIHAN".center(40), "="*5)
#     print("="*52)
#     pils = input("> Masukkan Pilihan : ")
#     if pils == "1":
#         tabelTernak()
#         menuUser()

#     elif pils == "2":
#         login()

#     elif pils == "3":
#         exit()
        
#     else:
#         print("Pilihan tidak tersedia!")
#         menuUser()

# # Fungsi Login Page
# def login():
#     print("="*52)
#     print("="*5, "APLIKASI MANIPULASI DATA PETERNAKAN ".center(40), "="*5)
#     print("="*52)
#     print("(1.) Login (Admin / User)")
#     print("(2.) Register Akun Baru")
#     print("(3.) Keluar")
#     print()
#     print("="*52)
#     print("="*5, "TENTUKAN PILIHAN".center(40), "="*5)
#     print("="*52)
#     opt = input("Masukkan Pilihan : ")
#     if opt == "1":
#         print("> Login sebagai User/Admin? ")
#         pil = input("Jika Admin Ketik 1, Jika User Ketik 2 : ")
#         if pil == "1":
#             adPut = input("Masukkan Username Admin : ")
#             paspud = pwinput.pwinput(prompt = "Masukkan Passcode : ")
#             search2 = superUser.get("userAdmin").index(adPut)
#             if adPut == superUser.get("userAdmin")[search2] and paspud == superUser.get("pCodeAdmin")[search2]:
#                 menu()
#             else:
#                 print("Username atau Passcode Anda Salah!, Coba Lagi!")
#                 login()

#         elif pil == "2":
#             usPut = input("Masukkan Username : ")
#             pasPut = pwinput.pwinput(prompt = "Masukkan Passcode : ")
#             search = userBiasa.get("user").index(usPut)
#             if usPut == userBiasa.get("user")[search] and pasPut == userBiasa.get("pCodeUser")[search]:
#                     print("Login Berhasil")
#                     menuUser()
                    
#             else:
#                 print("Username atau Passcode Anda Salah!, Coba Lagi!")
#                 login()
#         else :
#             print("Pilihan tidak tersedia!")
#             login()

#     elif opt == "2":
#             pinr = pwinput.pwinput(prompt = "Masukkan Pin Untuk Registrasi Akun Baru : ")
#             if pinr == passReg:
#                 registerAkun()
#             else:
#                 print("PIN Anda salah, coba lagi!")
#                 login()

#     elif opt == "3":
#             exit()

#     else:
#         print("Pilihan tidak tersedia!")
#         login()

# # Tampilan Pertama / Output Pertama Kali
# login()