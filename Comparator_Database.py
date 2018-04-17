import sqlite3
import Manual_Database

Okunmus_RFID = ""

def Comparator_Program(Okunmus_RFID):
    flag = True
    while flag:
        bos_liste = []
        karsilastirma_verisi = []

        with sqlite3.connect('home\\pi\\Desktop\\Yoklama\\database.sqlite') as vt:
            im = vt.cursor()
            im.execute("""CREATE TABLE IF NOT EXISTS Laboratuvar (RFID_Kodu, Adi_Soyadi, Numarasi)""")
            im.execute("""SELECT * FROM Laboratuvar WHERE RFID_Kodu = ?""", (Okunmus_RFID,))
            karsilastirma_verisi = im.fetchall()

        if(karsilastirma_verisi == bos_liste):
            Manual_Database.Manual_Program()
            vt.commit()
            flag = True

        elif (karsilastirma_verisi != bos_liste):
            if (karsilastirma_verisi[0][0] == Okunmus_RFID):
                RFID_UID = karsilastirma_verisi[0][0]
                Ad_Soyad = karsilastirma_verisi[0][1]
                Numara = karsilastirma_verisi[0][2]
                with sqlite3.connect('home\\pi\\Desktop\\Yoklama\\Yoklama_Listesi.sqlite') as db:
                    im2 = db.cursor()
                    im2.execute("""CREATE TABLE IF NOT EXISTS Yoklama (RFID_Kodu, Adi_Soyadi, Numarasi)""")
                    im2.execute("""INSERT INTO Yoklama VALUES (?, ?, ?)""", (RFID_UID, Ad_Soyad, Numara))
                    db.commit()
                print(RFID_UID,Ad_Soyad,Numara)
                flag = False
        else:
            flag = False