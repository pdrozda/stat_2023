import numpy as np
import scipy.stats as scs
import pandas as pd
import statistics as stat

#Zadanie 1
data = pd.read_csv('MDR_RR_TB_burden_estimates_2020-11-18.csv')
data_statistics = data.describe()
print(data_statistics)

#Zadanie 2
dane_wzrost = np.loadtxt('Wzrost.csv', delimiter=',',skiprows=0)

# przykładowe funkcje
print(stat.stdev(dane_wzrost))
print(stat.pstdev(dane_wzrost))
print(stat.variance(dane_wzrost))
print(stat.pvariance(dane_wzrost))
#Zadanie 3
dane = pd.read_csv("napoje_po_reklamie.csv", sep=';', na_values='.')

mean = scs.tmean(dane)
variance = scs.variation(dane)
skewness = scs.skew(dane)
kurtosis = scs.kurtosis(dane)

print(dane)
print("Średnia: ", mean)
print("Wariancja: ",variance)
print("Skośność: ",skewness)
print("kurtoza: ",kurtosis)

#Zadanie 4
import matplotlib.pyplot as plt

data = pd.read_csv('brain_size.csv', sep=';', na_values='.');
print('Mean of VIQ column: ',data['VIQ'].mean())
count_of_genders = data['Gender'].value_counts()
print("The count of genders: ", count_of_genders)

hist1 = data['VIQ'].hist(bins=3)
plt.show()
hist2 = data['PIQ'].hist(bins=3)
plt.show()
hist3 = data['FSIQ'].hist(bins=3)
plt.show()

data[data['Gender'] == 'Female']['VIQ'].hist()
data[data['Gender'] == 'Female']['PIQ'].hist()
data[data['Gender'] == 'Female']['FSIQ'].hist()
plt.show()