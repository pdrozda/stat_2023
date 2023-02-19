import MySQLdb
import numpy as np
from datetime import date
import config
import os

MySQL_Config = config.mysql
folder = 'dane'
folder_docelowy ='przetworzone'
db_connection = MySQLdb.connect(host=MySQL_Config['host'], user=MySQL_Config['user'],
                                passwd=MySQL_Config['passwd'], db=MySQL_Config['db'])
cur = db_connection.cursor()
lista_plikow = os.listdir(folder)
print(lista_plikow)
data_dzisiejsza = date.today()
for plik in lista_plikow:
    sciezka_pliku = folder+'/'+plik
    docelowa_sciezka = folder_docelowy+'/'+plik
    dane_wzrost = np.loadtxt(sciezka_pliku, delimiter=',')
    print('przetwarzam plik:', sciezka_pliku)
    for wartosc in dane_wzrost:
        zapytanie = "INSERT INTO osoba(wzrost, data_dodania) VALUES("+str(wartosc)+\
                    ",'"+str(data_dzisiejsza)+"');"
        cur.execute(zapytanie)
        db_connection.commit()
    os.rename(sciezka_pliku, docelowa_sciezka)
db_connection.close()
