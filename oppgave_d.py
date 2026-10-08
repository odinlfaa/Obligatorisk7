import pandas as pd
import matplotlib.pyplot as plt

"""
All data er hentet fra https://seklima.met.no
"""

# Fjerner knappene nederst på grafvinduet
plt.rcParams["toolbar"] = "None"

# Spør etter årstall
while True:
    try:
        arstall = int(input("Hvilket årstall vil du se på (2020-2026): "))
        if 2020 <= arstall <= 2026:
            break
        else:
            print("Du må skrive et årstall mellom 2020 og 2026.")
    except ValueError:
        print("Du må skrive inn et gyldig årstall mellom 2020 og 2026.")



# Leser CSV-filen
data = pd.read_csv("table.csv", sep=";")

# Konverterer dato
data["Tid(norsk normaltid)"] = pd.to_datetime(
    data["Tid(norsk normaltid)"],
    format="%d.%m.%Y"
)

# Velger Sola og Sviland
data = data[data["Navn"].isin(["Sola", "Sviland"])]

# Velger bare ønsket år
data = data[
    data["Tid(norsk normaltid)"].dt.year == arstall
]

# Gjør om værdata til tall
kolonner = [
    "Nedbør (døgn)",
    "Snødybde",
    "Middeltemperatur (døgn)",
    "Høyeste middelvind (døgn)"
]

for kolonne in kolonner:
    data[kolonne] = pd.to_numeric(
        data[kolonne]
        .astype(str)
        .str.replace(",", ".", regex=False),
        errors="coerce"
    )

# Sorterer etter dato
data = data.sort_values("Tid(norsk normaltid)")

# Deler opp dataene i Sola og Sviland
sola = data[data["Navn"] == "Sola"]
sviland = data[data["Navn"] == "Sviland"]

# Lager 4 grafer
fig, axs = plt.subplots(
    4, 1,
    figsize=(12, 10),
    sharex=True
)

# Endrer "Figure 1" til "Obligatorisk Gruppeprosjekt"
fig.canvas.manager.set_window_title(
    "Obligatorisk Gruppeprosjekt"
)

# Tittel inni grafen
fig.text(
    0.5,
    0.965,
    f"Værdata på Sola og Sviland i {arstall}",
    ha="center",
    fontsize=14
)



#Nedbør graf
axs[0].plot(
    sola["Tid(norsk normaltid)"],
    sola["Nedbør (døgn)"],
    label="Sola",
    color="blue"
)

axs[0].plot(
    sviland["Tid(norsk normaltid)"],
    sviland["Nedbør (døgn)"],
    label="Sviland",
    color="deepskyblue"
)

axs[0].set_ylabel("Nedbør (mm)")
axs[0].set_title("Nedbør")
axs[0].legend()
axs[0].grid()

#Snødybde graf
axs[1].plot(
    sola["Tid(norsk normaltid)"],
    sola["Snødybde"],
    label="Sola",
    color="blue"
)

axs[1].plot(
    sviland["Tid(norsk normaltid)"],
    sviland["Snødybde"],
    label="Sviland",
    color="deepskyblue"
)

axs[1].set_ylabel("Snødybde (cm)")
axs[1].set_title("Snødybde")
axs[1].legend()
axs[1].grid()

#Temperatur graf
axs[2].plot(
    sola["Tid(norsk normaltid)"],
    sola["Middeltemperatur (døgn)"],
    label="Sola",
    color="red"
)

axs[2].set_ylabel("Temperatur (°C)")
axs[2].set_title("Middeltemperatur")
axs[2].legend()
axs[2].grid()

#Vind graf
axs[3].plot(
    sola["Tid(norsk normaltid)"],
    sola["Høyeste middelvind (døgn)"],
    label="Sola",
    color="green"
)

axs[3].set_ylabel("Vind (m/s)")
axs[3].set_title("Høyeste middelvind")
axs[3].legend()
axs[3].grid()

#Månder på x-aksen
måneder = [
    "Jan", "Feb", "Mar", "Apr",
    "Mai", "Jun", "Jul", "Aug",
    "Sep", "Okt", "Nov", "Des"
]

datoer = pd.date_range(
    start=f"{arstall}-01-01",
    end=f"{arstall}-12-01",
    freq="MS"
)

axs[3].set_xticks(datoer)
axs[3].set_xticklabels(måneder)

axs[3].set_xlabel(
    "Måned",
    labelpad=5
)

# Roterer månedene
plt.xticks(rotation=45)


# Bedre plass rundt grafene
plt.tight_layout(
    rect=[0, 0.04, 1, 0.94]
)


# Viser grafene
plt.show()