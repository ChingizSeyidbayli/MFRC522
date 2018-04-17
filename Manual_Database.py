import sqlite3
def Manual_Program(New_UID):
    flag_AnaDongu = True
    flag_OgrenciNumara= True
    E = 1
    H = 2
    evet = int(E)
    hayir = int(H)
    while flag_AnaDongu:
        program_sorusu = input("Veri islemek istiyor musunuz? (Evet(1)/Hayir(2)): ")
        if program_sorusu == evet:
            with sqlite3.connect('home\\pi\\Desktop\\Yoklama\\database.sqlite') as vt:
                im = vt.cursor()
                im.execute("""CREATE TABLE IF NOT EXISTS Laboratuvar (RFID_Kodu, Adi_Soyadi, Numarasi)""")
            Ad_Soyad = input("Ad ve Soyad Giriniz: ")
            while flag_OgrenciNumara:
                Numara = input("Ogrenci Numarasini 9 haneli olarak giriniz: ")
                if len(Numara) == 9:
                    flag_OgrenciNumara = False
                    try:
                        Numara = int(Numara)
                    except ValueError:
                        print("Girdiginiz ogrenci numarasi sadece sayi icermiyor!")
                        flag_OgrenciNumara = True
                else:
                    print("Girdiginiz numara 9 haneli degil..\n")
                    flag_OgrenciNumara = True

            im.execute("""INSERT INTO Laboratuvar VALUES (?, ?, ?)""", (New_UID, Ad_Soyad, Numara))
            vt.commit()

            flag_AnaDongu = True
            flag_OgrenciNumara = True
        elif program_sorusu == hayir:
            print("Gorusmek Uzere!!")
            flag_AnaDongu = False
        else:
            print("'E' veya 'H' cevaplarindan birisini vermeniz gerekiyor..")
            flag_AnaDongu = True