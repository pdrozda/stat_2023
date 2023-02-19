import numpy as np
import scipy.stats as scs

dane_wzrost = np.loadtxt('dane/Wzrost.csv', delimiter=',')
print(dane_wzrost.mean())
dane_wzrost1 = np.loadtxt('dane/Wzrost1.csv', delimiter=',')
print(dane_wzrost1.mean())
dane_wzrost2 = np.loadtxt('dane/Wzrost2.csv', delimiter=',')
print(dane_wzrost2.mean())

# NORMALNOŚĆ
test_normalnosc = scs.normaltest(dane_wzrost)
print('Normalność', test_normalnosc)
test_normalnosc1 = scs.normaltest(dane_wzrost1)
print('Normalność 1', test_normalnosc1)
test_normalnosc2 = scs.normaltest(dane_wzrost2)
print('Normalność 2', test_normalnosc2)

# TEST RÓWNOŚCI WARIANCJI
levene_test_wariancji = scs.levene(dane_wzrost, dane_wzrost1)
print("Równość wariancji:", levene_test_wariancji)