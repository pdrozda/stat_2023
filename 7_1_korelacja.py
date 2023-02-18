import pandas as pd
import scipy.stats as scs
import numpy as np

dane_mozgowe = pd.read_csv('files/brain_size.csv', sep=';', na_values='.')
print(dane_mozgowe.head())

# korelacja Pearsona
wspolczynnik_pearson, pvalue = scs.pearsonr(dane_mozgowe['Weight'], dane_mozgowe['Height'])
print('Współczynnik korelacji Pearsona wzrost i waga:', wspolczynnik_pearson)
print('wartość prawodopodobieństwa:', pvalue)
wspolczynnik_spearman, pvalue = scs.spearmanr(dane_mozgowe['Weight'], dane_mozgowe['Height'])
print('Współczynnik korelacji Spearmana wzrost i waga:', wspolczynnik_spearman)
print('wartość prawodopodobieństwa:', pvalue)
wspolczynnik_pearson_1, pvalue_1 = scs.pearsonr(dane_mozgowe['FSIQ'], dane_mozgowe['VIQ'])
print('Współczynnik korelacji Pearsona FSIQ i VIQ:', wspolczynnik_pearson_1)
print('wartość prawodopodobieństwa:', pvalue_1)

macierz = [dane_mozgowe['FSIQ'], dane_mozgowe['VIQ'], dane_mozgowe['PIQ'], dane_mozgowe['Weight'],
           dane_mozgowe['Height'], dane_mozgowe['MRI_Count']]
macierz_korelacji = np.corrcoef(macierz).round(2)
print(macierz_korelacji)

wspolczynnik_pearson_2, pvalue_2 = scs.pearsonr(dane_mozgowe['FSIQ'], dane_mozgowe['Height'])
print('Współczynnik korelacji Pearsona FSIQ i Height:', wspolczynnik_pearson_2.round(2))
print('wartość prawodopodobieństwa:', pvalue_2)
if (pvalue_2>=0.05):
    print('Korelacja nie zachodzi')
else:
    print('Korelacja zachodzi i współczynnik korelacji jest równy:', wspolczynnik_pearson_2)