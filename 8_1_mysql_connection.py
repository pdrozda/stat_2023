import MySQLdb
import config
import os
import numpy as np
from datetime import date

mysql_config = config.mysql
folder = 'dane'
folder_docelowy='przetworzone'

db_connection = MySQLdb.connect(host=mysql_config['host'],
                                user=mysql_config['user'],
                                passwd=mysql_config['passwd'],
                                db=mysql_config['db'])
cur = db_connection.cursor()
lista_plikow = os.listdir(folder)
print(lista_plikow)
data_dzisiejsza = date.today()
for plik in lista_plikow:
    sciezka_pliku = folder+'/'+plik
    docelowa_sciezka = folder_docelowy+'/'+plik
    print(sciezka_pliku)
    dane_wzrost = np.loadtxt(sciezka_pliku, delimiter=',')
    print(dane_wzrost)
    for wartosc_wzrostu in dane_wzrost:
        zapytanie = "INSERT INTO osoba(wzrost,data_dodania) " \
                    "VALUES("+str(wartosc_wzrostu)+",'"\
                    +str(data_dzisiejsza)+"')"
        cur.execute(zapytanie)
        db_connection.commit()
    os.rename(sciezka_pliku, docelowa_sciezka)

zapytanie = "SELECT * FROM osoba"
cur.execute(zapytanie)
for wynik in cur:
    print(wynik)

db_connection.close()