import matplotlib.pyplot as plt
import scipy.stats as scs
import seaborn as sns

# Zadanie 1

wartosci = (1, 2, 3, 4, 5, 6)
prawdopodobienstwa = (1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
data = scs.rv_discrete(values=(wartosci, prawdopodobienstwa))
print('Srednia: ', data.mean())
print('Mediana: ', data.median())
print('Wariancja: ', data.var())
print('Odchylenie standardowe: ', data.std())
print('Wartosc oczekiwana: ', data.expect())

# Zadanie 2
p = 0.4
n = 12
bernoulli = scs.bernoulli.rvs(p, size=100)
binomial = scs.binom.rvs(n, p, size=100)
poisson = scs.poisson.rvs(p, size=100)

bernoulli_mean = bernoulli.mean()
bernoulli_var = bernoulli.var()
bernoulli_kur = scs.kurtosis(bernoulli)
bernoulli_skew = scs.skew(bernoulli)

binomial_mean = binomial.mean()
binomial_var = binomial.var()
binomial_kur = scs.kurtosis(binomial)
binomial_skew = scs.skew(binomial)

poisson_mean = poisson.mean()
poisson_var = poisson.var()
poisson_kur = scs.kurtosis(poisson)
poisson_skew = scs.skew(poisson)

print('Bernoulli')
print('Średnia: ', bernoulli_mean)
print('Wariancja: ', bernoulli_var)
print('Kurtoza: ', bernoulli_skew)
print('Skośność: ', bernoulli_kur)

print('Binomial')
print('Średnia: ', binomial_mean)
print('Wariancja: ', binomial_var)
print('Kurtoza: ', binomial_kur)
print('Skośność: ', binomial_skew)

print('Poisson')
print('Średnia: ', poisson_mean)
print('Wariancja: ', poisson_var)
print('Kurtoza: ', poisson_kur)
print('Skośność: ', poisson_skew)

# Zadanie 4
plot = sns.distplot(bernoulli)
plot.set(xlabel='Bernoulli distribution', ylabel='Frequency')
plt.show()

plot = sns.distplot(binomial)
plot.set(xlabel='Binomial distribution', ylabel='Frequency')
plt.show()

plot = sns.distplot(poisson)
plot.set(xlabel='Poisson distribution', ylabel='Frequency')
plt.show()

# Zadanie 4
binomial = scs.binom.rvs(n=20, p=0.4, size=1000)
plot = sns.distplot(binomial)
plot.set(xlabel='Binomial distribution', ylabel='Frequency')
plt.show()
print("Probability sum: ", scs.binom.cdf(k=20, n=20, p=0.4))

# Zadanie 5
norm = scs.norm.rvs(size = 10000, loc=0, scale=2)
print('Mean: expected 0, actual ', norm.mean())
print('Variance: expected 4, actual ', norm.var())
print('Standard deviation: expected 2, actual ', norm.std())
print('Median: expected 0, actual ', scs.norm.median(loc=0, scale=2))
print('Expected value: expected 0, actual ', scs.norm.expect(loc=0, scale=2))
print('Kurtosis: expected 0, actual ', scs.kurtosis(norm))
print('Skewness: expected 0, actual ', scs.skew(norm))

# Zadanie 6
data1 = scs.norm.rvs(size=1000, loc=1, scale=2)
data2 = scs.norm.rvs(size=1000, loc=0, scale=1)
data3 = scs.norm.rvs(size=1000, loc=-1, scale=0.5)

plot = sns.distplot(data1, color='red')
plot = sns.distplot(data2, color='blue')
plot = sns.distplot(data3, color='black')

plt.show()