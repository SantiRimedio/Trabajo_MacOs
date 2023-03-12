import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from limpieza_2022 import list, sup_barrio
from cmap_gcba import cmap_gcba
GeoJson_barrios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/barrios/barrios.geojson"
gdf = gpd.read_file(GeoJson_barrios)

#print(gdf["BARRIO"])
#print(list)
#plt.show()
gdf = pd.merge(gdf,sup_barrio, left_on="BARRIO", right_on="BARRIOS", how="inner").sort_values(by="SUP_CONST")
gdf["AREA HA"] = gdf["AREA"]/10000
gdf["SUP_KM"] = gdf["SUP_CONST"]/gdf["AREA HA"]
fig, ax = plt.subplots(1, 1)
ax.set_axis_off()

gdf.plot(column='SUP_KM',ax=ax, cmap=cmap_gcba,
           legend=True, linewidth=10,
           legend_kwds={'label': "Densidad de Superficie Construida. M2/Ha.",
                        'orientation': "horizontal", "fraction": 0.046,})
df1 = pd.DataFrame(gdf[["BARRIO", "SUP_KM"]])
#print(gdf)
#plt.show()
plt.savefig("Mapa_Barrios", dpi=800)

#plt.close()
print(gdf)