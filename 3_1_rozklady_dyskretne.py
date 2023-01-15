import scipy.stats as scs

p = 0.3
size = 10000000
n = 4

# rozkład Bernoulliego
dane_bernoulli = scs.bernoulli.rvs(p, size=size)
#print(dane_bernoulli)
print("Parametry empirycznego rozkładu Bernoulliego:", scs.describe(dane_bernoulli))
srednia, wariancja, skosnosc, kurtoza = scs.bernoulli.stats(p, moments='mvsk')
print("Parametry teoretycznego rozkładu Bernoulliego:", srednia, wariancja, skosnosc, kurtoza)

suma_p = 0
# rozkład dwumianowy
for k in range(0,n+1):
    p_binom_k_n = scs.binom.pmf(k, n, p)
    print("Prawdopodobieństwo " + str(k) + " sukcesów w "+ str(n) + " probach z p="+ str(p) + " wynosi " +str(p_binom_k_n))
    suma_p = suma_p + p_binom_k_n
    print("Suma skumulowana prawdopodobieństwa:", suma_p)