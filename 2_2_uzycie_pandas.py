import pandas as pd


dane_mozgu = pd.read_csv('files/brain_size.csv', sep=';', na_values='.')
print(dane_mozgu.head())

dane_mozgu_pogrupowane = dane_mozgu.groupby('Gender')
print(dane_mozgu_pogrupowane.head())

for gender,value in dane_mozgu_pogrupowane['FSIQ']:
    print(gender, value.mean())

spolki = ['bos', 'bml', 'bio']
data_pocz = '20200101'
data_kon = '20210101'
for spolka in spolki:
    url = "https://stooq.pl/q/d/l/?s="+spolka+"&d1="+data_pocz+"&d2="+data_kon+"&i=d"
    notowania_bos = pd.read_csv(url)
    print("Notowanie dla spolki:"+spolka)
    print(notowania_bos.head())