

import matplotlib.pyplot as plt
from matplotlib.pyplot import violinplot







"""
random-score / (num-random-games)
cooperate-score / (num-cooperate-games)
defect-score / (num-defect-games)
tit-for-tat-score / (num-tit-for-tat-games)
unforgiving-score / (num-unforgiving-games)
unknown-score / (num-unknown-games)
joss-score / (num-joss-games)
anon-score / (num-anon-games)
"""

t11 = ['0' ,'random', 'cooperate', 'defect', 'tit-for-tat', 'unforgiving', 'unknown', 'joss', 'anon']


import pandas as pd
import numpy as np
df = pd.read_csv('p50Each.csv',delimiter=',')
nump = df.to_numpy()

l = []
for el in nump:
    # print(el)
    l.append(el[0].split(',')[11:])


f = np.array(l)
f_2 = []
print(float(f[0][0][1:-1]))
for el in f:
    a = []
    for s in el:
        a.append(float(s[1:-1]))
    f_2.append(a)

f_2 = np.array(f_2)
print(f_2)

rot = np.rot90(f_2)

print(rot)
print(len(rot))





violinplot([rot[0],rot[1],rot[2],rot[3],rot[4],rot[5],rot[6],rot[7]])
plt.xticks(range(len(t11)), t11, size='small')
plt.show()
