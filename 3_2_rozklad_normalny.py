import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt

x = np.linspace(scs.norm.ppf(0.0001), scs.norm.ppf(0.9999), 1000)
fig, ax = plt.subplots(1, 1)

ax.plot(x, scs.norm.pdf(x), 'r-', lw=5)

rv = scs.norm(loc=0, scale=0.5)
ax.plot(x, rv.pdf(x), 'y-', lw=2)
rv = scs.norm(loc=0, scale=2)
ax.plot(x, rv.pdf(x), 'g-', lw=8)

plt.show()