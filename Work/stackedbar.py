import matplotlib.pyplot as plt
from limpieza_2022 import df

cmap= plt.cm.magma

for i in range(1,5):
    x = 0
    trimestre = df[df["TRIMESTRE"] == i]
    for j, k in zip(df["TIPO_OBRA"].unique(), range(0,4)):
        obra = trimestre[trimestre["TIPO_OBRA"] == j]
        color = [cmap(0),cmap(0.5),cmap(0.9)]
        p = plt.bar(i, len(obra), bottom=x, color=color[k])
        ax = plt.gca()
        ax.bar_label(p,label_type='center', color="white")
        print(color[k])
        x = len(obra) + x

plt.savefig("Edificios")
