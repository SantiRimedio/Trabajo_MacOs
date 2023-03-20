import matplotlib.pyplot as plt
from limpieza_2022 import df
#print(df)
import matplotlib.font_manager as font_manager
from matplotlib import rcParams


# Add every font at the specified location
font_dir = ['/Users/santi/Downloads/gotham-rounded']
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)

# Set font family globally
rcParams['font.family'] = 'Gotham Rounded'

tipos = []
label = []
for i in ["1","3"]:
        #df["TIPO_OBRA"].unique():
    print(i)
    label.append(i)
    obra = df[df["TIPO_OBRA"] == i]
    print(obra["BARRIOS"].value_counts())

    print(f"categoría {i} cantidad de obras {len(obra)}")
    print(obra["SUP_CONST"].sum())
    tipos.append(len(obra))
#print(df)
plt.pie(tipos, colors=["#EC607E","#29BDEF"])
#35,5%
# uno es obra nueva 3 es mod y ampliación
my_circle=plt.Circle( (0,0), 0.5, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)

plt.savefig("Torta.svg", dpi=800)
