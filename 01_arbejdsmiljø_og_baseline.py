#%%
import sys
print("Python virker!")
print(sys.executable)

#%%
import pandas as pd
titanic = pd.read_csv('titanic.csv')

# Datasættets størrelse
print(titanic.shape)

# Datatyper og antal ikke-manglende værdier
titanic.info()

# De første fem rækker
print(titanic.head())

#%%
# Samlet overblik over de numeriske kolonner
print(titanic.describe())

#%%
#Gns., std. afv. og median for hele Age kolonne:
print(titanic["Age"].mean())
print(titanic["Age"].std())
print(titanic["Age"].median())
#%%
#Gns., std. afv. og median for grupperinger af Age kolonne:
titanic.columns
titanic.groupby("Sex")["Age"].agg(
    ["mean", "std", "median", "count"]
)

#%%
#Undersøg overlevelsesandelen fordelt på passagerklasse
titanic.groupby("Pclass")["Survived"].agg(
    ["mean", "std", "median", "count"]
)
# %%
#Lav én graf og gem den som PNG (overlevelsesandele)
import matplotlib.pyplot as plt

survival_rate = titanic.groupby("Pclass")["Survived"].mean() * 100

survival_rate.plot(kind="bar", rot=0)

plt.title("Overlevelsesandel efter passagerklasse")
plt.xlabel("Passagerklasse")
plt.ylabel("Overlevende (%)")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("outputs/01_survival_rate_by_class.png", dpi=300)
plt.show()

# %%
