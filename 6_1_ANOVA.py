import scipy.stats as scs
import pandas
brain_dataset = pandas.read_csv('files/brain_size.csv', na_values='.', sep=';')
print(brain_dataset.columns)
ANOVA_results = scs.f_oneway(brain_dataset['FSIQ'], brain_dataset['VIQ'], brain_dataset['PIQ'])
print(ANOVA_results)