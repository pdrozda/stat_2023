import numpy as np
import statistics
import scipy.stats as scs


dane_wzrostu = np.loadtxt('files/Wzrost.csv', delimiter=',')
print(dane_wzrostu)

print("Minimalny wzrost:", dane_wzrostu.min())
print("Minimalny wzrost z numpy:", np.min(dane_wzrostu))
print()
print("Maksymalny wzrost:", dane_wzrostu.max())
print("Maksymalny wzrost z numpy:", np.max(dane_wzrostu))
print()
print("Średnia wzrostu:", dane_wzrostu.mean())
print("Średnia wzrostu z numpy:", np.mean(dane_wzrostu))
print()
print("Odchylenie std wzrostu:", dane_wzrostu.std())
print("Odchylenie std wzrostu z numpy:", np.std(dane_wzrostu))
print("Odchylenie std próby:", statistics.stdev(dane_wzrostu))
print("Odchylenie std populacji:", statistics.pstdev(dane_wzrostu))
print()
print("Mediana wzrostu:", np.median(dane_wzrostu))
print("Mediana wzrostu scipy:", scs.scoreatpercentile(dane_wzrostu,1))

print("Statystyki wzrostu:", scs.describe(dane_wzrostu))