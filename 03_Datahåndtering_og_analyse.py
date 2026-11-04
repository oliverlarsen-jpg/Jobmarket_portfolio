#%%
from pathlib import Path  # Importerer værktøjer til at arbejde med filstier

OUTPUT_DIR = Path("outputs")  # Definerer mappen, hvor figurer skal gemmes
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # Opretter mappen, hvis den ikke allerede findes

## Trin 03.1 - Dataaudit ##
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
bike_sharing = pd.read_csv("03_bike_sharing.csv")

#%%
# Undersøg datasættets struktur
# Viser de første fem rækker
print(bike_sharing.head())

# Viser antal rækker og kolonner
print(bike_sharing.shape)

# Viser kolonnenavne
print(bike_sharing.columns)

# Viser datatyper, antal ikke-manglende værdier og hukommelsesforbrug
print(bike_sharing.info())

bike_sharing.describe()

#%%
# Undersøg missing values
# isna() identificerer manglende værdier
# sum() tæller antallet af manglende værdier i hver kolonne
print(bike_sharing.isna().sum())

#andelen i procent:
print((bike_sharing.isna().mean() * 100).round(2))

# %%
# Undersøg dubletter
# duplicated() identificerer dublerede rækker
# sum() tæller antallet af dubletter
print(bike_sharing.duplicated().sum())
# og print selve dupletterne:
print(bike_sharing[bike_sharing.duplicated()])

# %%
# Undersøg ekstreme værdier - find outliers (IQR-metoden)
# Udvælger numeriske kolonner
numeric_df = bike_sharing.select_dtypes(include="number")

# Beregner første og tredje kvartil
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)

# Beregner interkvartilafstanden
IQR = Q3 - Q1

# Finder observationer uden for 1,5 * IQR
outliers = (
    (numeric_df < Q1 - 1.5 * IQR) |
    (numeric_df > Q3 + 1.5 * IQR)
)

# Tæller potentielle ekstreme værdier i hver kolonne
print(outliers.sum())

# %%
#Lav en data dictionary
# En data dictionary er i princippet bare en oversigt over datasættets variabler.
data_dictionary = pd.DataFrame({
    "Variabel": bike_sharing.columns,
    "Datatype": bike_sharing.dtypes.astype(str).values
})

print(data_dictionary)

#%%
betydninger = {
    "instant": "Løbenummer for observationen",
    "dteday": "Dato for observationen",
    "season": "Årstid",
    "yr": "År",
    "mnth": "Måned",
    "holiday": "Ferie eller ej",
    "weekday": "Ugedag (6=lør, 0=søn)",
    "workingday": "Arbejdsdag eller ej (0=ej)",
    "weathersit": "Vejrforhold (1-4; godt-dårligt)",
    "temp": "Normaliseret temperatur",
    "atemp": "Normaliseret følt temperatur",
    "hum": "Normaliseret luftfugtighed",
    "windspeed": "Normaliseret vindhastighed",
    "casual": "Antal udlejninger til ikke-registrerede brugere",
    "registered": "Antal udlejninger til registrerede brugere",
    "cnt": "Samlet antal udlejninger"
}

data_dictionary["Betydning"] = data_dictionary["Variabel"].map(betydninger)

print(data_dictionary)

# %%
## Trin 03.2 - Visualisering ##
# •	Lav en tidsserie, en fordeling og et scatterplot.
import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv("03_bike_sharing.csv")
bike_sharing["dteday"] = pd.to_datetime(bike_sharing["dteday"])
# Konverterer dato-kolonnen til et rigtigt datoformat
#%%
# Tidsserie – udvikling over tid
plt.figure(figsize=(12, 5))  # Opretter en figur med bredde 12 og højde 5 tommer

plt.plot(bike_sharing["dteday"], bike_sharing["casual"], label="Casual")  # Tegner tidsserien for ikke-registrerede brugere
plt.plot(bike_sharing["dteday"], bike_sharing["registered"], label="Registered")  # Tegner tidsserien for registrerede brugere
#plt.plot(bike_sharing["dteday"], bike_sharing["cnt"], label="Total")  # Tegner tidsserien for det samlede antal udlejninger

plt.title("Daglige cykeludlejninger fordelt på brugertype")  # Tilføjer en titel
plt.xlabel("Dato")  # Navngiver x-aksen
plt.ylabel("Antal udlejninger")  # Navngiver y-aksen
plt.legend()  # Viser en forklaring på, hvilken linje der tilhører hvilken variabel
plt.grid(True, alpha=0.3)  # Tilføjer et diskret gitter for at gøre værdierne lettere at aflæse

plt.figtext(
    0.1, 0.01,  # Angiver placeringen af kildeteksten i figuren
    "Kilde: UCI Machine Learning Repository, Bike Sharing Dataset",  # Selve kildeteksten
    fontsize=8  # Angiver skriftstørrelsen
)

plt.tight_layout()  # Tilpasser layoutet
plt.savefig(OUTPUT_DIR / "03_tidsserie_brugertyper.png", dpi=300)  # Gemmer grafen som en PNG-fil
plt.show()  # Viser grafen

# %%
# Fordeling – hvordan er værdierne fordelt? Histogram
plt.figure(figsize=(8, 5))  # Opretter en figur med bredde 8 og højde 5 tommer

plt.hist(bike_sharing["cnt"], bins=30, edgecolor="black")  # Laver et histogram af cnt opdelt i 30 intervaller med sorte kanter

plt.title("Fordeling af daglige cykeludlejninger")  # Tilføjer en titel til grafen
plt.xlabel("Antal udlejninger")  # Navngiver x-aksen
plt.ylabel("Antal dage")  # Navngiver y-aksen

plt.figtext(
    0.1, 0.01,  # Angiver placeringen af kildeteksten i figuren
    "Kilde: UCI Machine Learning Repository, Bike Sharing Dataset",  # Selve kildeteksten
    fontsize=8  # Angiver skriftstørrelsen
)

plt.tight_layout()  # Tilpasser layoutet, så teksten passer ind
plt.savefig(OUTPUT_DIR / "03_fordeling.png", dpi=300)  # Gemmer figuren som en PNG-fil med høj opløsning
plt.show()  # Viser figuren på skærmen


# %%
# Scatterplot – sammenhæng mellem to variable (temp og cnt)
import numpy as np  # Importerer NumPy til numeriske beregninger
import matplotlib.pyplot as plt  # Importerer Matplotlib til visualisering

x = bike_sharing["temp"]  # Gemmer temperaturvariablen som x
y = bike_sharing["cnt"]  # Gemmer antal udlejninger som y

a, b = np.polyfit(x, y, 1)  # Beregner hældning (a) og skæring (b) for den bedste rette linje

x_linje = np.linspace(x.min(), x.max(), 100)  # Laver 100 jævnt fordelte temperaturværdier mellem minimum og maksimum
y_linje = a * x_linje + b  # Beregner tendenslinjens y-værdier for de nye temperaturværdier

plt.figure(figsize=(8, 5))  # Opretter en figur
plt.scatter(x, y, alpha=0.6, label="Observationer")  # Tegner observationerne
plt.plot(x_linje, y_linje, color="red", label="Lineær tendenslinje")  # Tegner en glat, korrekt sorteret tendenslinje

plt.title("Temperatur og antal cykeludlejninger")  # Tilføjer en titel
plt.xlabel("Temperatur (normaliseret)")  # Navngiver x-aksen
plt.ylabel("Antal udlejninger")  # Navngiver y-aksen
plt.legend()  # Viser forklaringen
plt.grid(True, alpha=0.3)  # Tilføjer gitter

plt.figtext(
    0.1, 0.01,  # Angiver placeringen af kildeteksten i figuren
    "Kilde: UCI Machine Learning Repository, Bike Sharing Dataset",  # Selve kildeteksten
    fontsize=8  # Angiver skriftstørrelsen
)

plt.tight_layout()  # Tilpasser layoutet
plt.savefig(OUTPUT_DIR / "03_scatterplot_tendenslinje.png", dpi=300)  # Gemmer figuren
plt.show()  # Viser figuren

#%%
# R^2 - hvor godt passer tendenslinjen?
y_pred = a * x + b  # Beregner modellens forudsagte værdier

ss_res = ((y - y_pred) ** 2).sum()  # Beregner summen af de kvadrerede residualer
ss_tot = ((y - y.mean()) ** 2).sum()  # Beregner den samlede variation i cnt

r_squared = 1 - ss_res / ss_tot  # Beregner modellens R²
print(f"R²: {r_squared:.3f}")  # Udskriver R² med tre decimaler
# Positiv korrelation, men passer ikke særlig godt: R^2=0.394!

#%%
# Undersøger, om 2.grads- eller 3.gradspolynomier passer bedre:
import numpy as np  # Importerer NumPy til numeriske beregninger
import matplotlib.pyplot as plt  # Importerer Matplotlib til grafer

x = bike_sharing["temp"].to_numpy()  # Henter temperaturerne som et NumPy-array
y = bike_sharing["cnt"].to_numpy()  # Henter antal udlejninger som et NumPy-array

# Beregner polynomierne
koef_1 = np.polyfit(x, y, 1)  # Beregner et førstegradspolynomium (ret linje)
koef_2 = np.polyfit(x, y, 2)  # Beregner et andengradspolynomium (parabel)
koef_3 = np.polyfit(x, y, 3)  # Beregner et tredjegradspolynomium

# Beregner modellernes forudsagte værdier
y_pred_1 = np.polyval(koef_1, x)  # Beregner forudsagte værdier fra førstegradsmodellen
y_pred_2 = np.polyval(koef_2, x)  # Beregner forudsagte værdier fra andengradsmodellen
y_pred_3 = np.polyval(koef_3, x)  # Beregner forudsagte værdier fra tredjegradsmodellen

# Beregner den samlede variation i y
ss_tot = ((y - y.mean()) ** 2).sum()  # Beregner den samlede kvadrerede afvigelse fra gennemsnittet

# Beregner R² for hver model
r2_1 = 1 - ((y - y_pred_1) ** 2).sum() / ss_tot  # R² for førstegradsmodellen
r2_2 = 1 - ((y - y_pred_2) ** 2).sum() / ss_tot  # R² for andengradsmodellen
r2_3 = 1 - ((y - y_pred_3) ** 2).sum() / ss_tot  # R² for tredjegradsmodellen

print(f"Førstegradspolynomium: R² = {r2_1:.3f}")  # Udskriver R² med tre decimaler
print(f"Andengradspolynomium: R² = {r2_2:.3f}")  # Udskriver R² med tre decimaler
print(f"Tredjegradspolynomium: R² = {r2_3:.3f}")  # Udskriver R² med tre decimaler
#Bedre, men stadig ikke super - nok begrænset sammenhæng!

# %%
## Scatterplot med de 3 forskellige polynomier
# Opretter temperaturværdier til at tegne glatte polynomiekurver
x_linje = np.linspace(x.min(), x.max(), 200)

# Beregner modellernes forudsagte værdier
y_linje_1 = np.polyval(koef_1, x_linje)
y_linje_2 = np.polyval(koef_2, x_linje)
y_linje_3 = np.polyval(koef_3, x_linje)

# Opretter figuren
plt.figure(figsize=(10, 6))

# Tegner de faktiske observationer
plt.scatter(x, y, alpha=0.4, label="Observationer")

# Tegner de tre polynomier
plt.plot(x_linje, y_linje_1, label=f"Grad 1 (R²={r2_1:.3f})")
plt.plot(x_linje, y_linje_2, label=f"Grad 2 (R²={r2_2:.3f})")
plt.plot(x_linje, y_linje_3, label=f"Grad 3 (R²={r2_3:.3f})")

# Tilføjer titel og aksebetegnelser
plt.title("Temperatur og cykeludlejninger: polynomielle modeller")
plt.xlabel("Temperatur (normaliseret)")
plt.ylabel("Antal udlejninger")

# Tilføjer forklaring og gitter
plt.legend()
plt.grid(True, alpha=0.3)

# Tilpasser layout og gemmer figuren
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_polynomier_sammenligning.png", dpi=300)
plt.show()

# %%
