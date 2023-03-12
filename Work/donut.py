import matplotlib.pyplot as plt
from limpieza_2022 import df
#print(df)
tipos = []
label = []
cmap= plt.cm.magma
for i in df["TIPO_OBRA"].unique():
    label.append(i)
    obra = df[df["TIPO_OBRA"] == i]
    tipos.append(len(obra))

plt.pie(tipos, labels=label, autopct='%1.1f%%',pctdistance=1.24, colors=[cmap(0), cmap(0.5), cmap(0.9)])


plt.savefig("Torta")
