import sqlite3
def Yoklama_Database_Sifirlama():
    with sqlite3.connect('home\\pi\\Desktop\\Yoklama\\Yoklama_Listesi.sqlite') as bbk:
        cs = bbk.cursor()
        cs.execute("""DELETE FROM Yoklama""")
        bbk.commit()

def Yoklama_Ciktisi():
    with sqlite3.connect('home\\pi\\Desktop\\Yoklama\\Yoklama_Listesi.sqlite') as bk:
        csd = bk.cursor()
        csd.execute("""SELECT * FROM personel""")
        f = open("C:\\Users\\Bilgehan\\Desktop\\RFID.Database\\database.txt", "w")
        for veri1 in csd:
            veri = str(veri1)
            f.write(veri)
            f.write("\n")
        f.close()