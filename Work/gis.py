# Importing the required modules
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

df = pd.read_excel("/Users/santi/Desktop/Work/base_limpia.xlsx", engine="openpyxl")

# Creating an instance of Nominatim Class
geolocator = Nominatim(user_agent="santi")

# applying the rate limiter wrapper
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=4)

# Applying the method to pandas DataFrame
df["add"] = df["DIRECCION"] + " " + df["BARRIOS"] + " Buenos Aires, Argentina"
df["location"] = df.index
for i in df.index:
    print(f"{i} of {len(df)}")
    df["address"] = df["DIRECCION"] + " " + df["BARRIOS"] + " Buenos Aires, Argentina"
    try:
        df['Latitud'][i] = geolocator.geocode(df['address'][i]).latitude
        df['Longitud'][i] = geolocator.geocode(df['address'][i]).longitude

    except:
        df['location'][i] = None
    print(f"position {i} is lat {df['Latitud'][i]} and long {df['Longitud'][i]}")

df.to_excel("base_georeferenciada.xlsx")
