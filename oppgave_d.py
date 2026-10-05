import pandas as pd
import matplotlib.pyplot as plt

"""
All data er hentet ifra https://seklima.met.no
"""

#csv filer er skilles ofte med "," og ikke ";" så sier til programmet at den skal slikke kollonene med ; istedenfor det normale ,
data = pd.read_csv("table.csv", sep=";")

# Konverterer datoer
data["Tid(norsk normaltid)"] = pd.to_datetime(
    data["Tid(norsk normaltid)"], format="%d.%m.%Y"
    )

# Convert temperature to numbers
data["Middeltemperatur (døgn)"] = pd.to_numeric(
    data["Middeltemperatur (døgn)"].astype(str).str.replace(",", ".", regex=False),errors="coerce"
    )

# Keep only rows where temperature exists
data = data.dropna(subset=["Middeltemperatur (døgn)"])

# Plot
plt.plot(
    data["Tid(norsk normaltid)"],
    data["Middeltemperatur (døgn)"]
)

plt.xlabel("Dato")
plt.ylabel("Middeltemperatur (°C)")
plt.title("Middeltemperatur på Sola")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()