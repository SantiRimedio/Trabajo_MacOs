import matplotlib.pyplot as plt
from Geopandas import df1
import numpy as np
from matplotlib import cm
import matplotlib

df1 = df1.sort_values(by="SUP_KM", ascending=True)
plt.figure(2, figsize=(17,20))
ax = plt.gca()
cmap= plt.cm.magma
# create normalization instance
norm = matplotlib.colors.Normalize(vmin=df1["SUP_KM"].min(), vmax=df1["SUP_KM"].max())
# create a scalarmappable from the colormap
sm = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
bars = plt.barh(df1["BARRIO"],df1["SUP_KM"],height=0.8,color=sm.to_rgba(df1["SUP_KM"]))
#plt.show()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_linewidth(2)
ax.axvline(x=df1["SUP_KM"].mean(),lw=2, color="red", label="Promedio")
plt.xticks(fontsize="x-large", fontweight="bold")
plt.yticks(fontsize="large", fontweight="bold")
plt.tick_params(left = False)
plt.grid(axis="x",color='lightgrey', linestyle='dashed', linewidth=2)
plt.legend(loc="lower center", frameon=False,fontsize=25)
plt.savefig("BarrasH")
plt.close()
