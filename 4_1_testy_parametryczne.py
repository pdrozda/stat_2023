import numpy as np
import scipy.stats as scs


dane_wzrost = np.loadtxt('dane/Wzrost.csv', delimiter=',')
print(dane_wzrost.mean())
dane_wzrost1 = np.loadtxt('dane/Wzrost1.csv', delimiter=',')
print(dane_wzrost1.mean())
dane_wzrost2 = np.loadtxt('dane/Wzrost2.csv', delimiter=',')
print(dane_wzrost2.mean())

# JEDNA ŚREDNIA
# Standardowo przyjmujemy poziom istotności alfa = 0.05
# Dla wartości pvalue jeśli jest ona wyższa od poziomu istotności to przyjmujemy H0,
# jeśli jest mniejsza to odrzucamy H0 na korzyść H1
test_1_proba_wzrost = scs.ttest_1samp(dane_wzrost, 171)
print("statystyka T, i prawdopodobieństwo, plik wzrost.csv:",test_1_proba_wzrost)
test_1_proba_wzrost2 = scs.ttest_1samp(dane_wzrost2, 171)
print("statystyka T, i prawdopodobieństwo, plik wzrost2.csv:",test_1_proba_wzrost2)

# DWIE ŚREDNIE - próby niezależne
test_2_wzrost_niezalezne = scs.ttest_ind(dane_wzrost, dane_wzrost1)
print('Statystyka T i prawdopodobieństwo, próby niezależne:', test_2_wzrost_niezalezne)
test_2_wzrost_niezalezne_bis = scs.ttest_ind(dane_wzrost1, dane_wzrost2)
print('Statystyka T i prawdopodobieństwo, próby niezależne:', test_2_wzrost_niezalezne_bis)

# DWIE ŚREDNIE - próby zależne
test_2_wzrost_zalezne = scs.ttest_rel(dane_wzrost, dane_wzrost1)
print('Statystyka T i prawdopodobieństwo, próby zależne:', test_2_wzrost_zalezne)