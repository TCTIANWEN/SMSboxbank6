import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f=open(r'bank2.dat', encoding='utf-8')
data_y = []
for line in f:
    s = line.strip().split(' ')
    y = []
    for j in range(0, len(s)):
        if s[j] != '':
            y.append(float(s[j]))
    data_y.append(y)
f.close()
data_n = np.array(data_y)


data_l = {
    'Genuine': list(data_n[0:100,5]),
    'Counterfeit': list(data_n[100:200, 5])
}

data = pd.DataFrame(data_l)

data.plot.box(title="Swiss Bank Notes")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
