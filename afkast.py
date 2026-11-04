# %%
## Test og Fejlfinding
#Laver en funktion, der beregner afkast:

import pandas as pd  # Importerer pandas til at arbejde med dataserier og data

def beregn_afkast(priser):  # Definerer en funktion, der beregner afkast ud fra priser

    # isinstance() kontrollerer, om inputtet er en pandas Series
    if not isinstance(priser, pd.Series):
        raise TypeError("Priser skal være en pandas Series.")
        # raise TypeError stopper funktionen og viser en fejl, hvis inputtypen er forkert

    # empty kontrollerer, om dataserien er tom
    if priser.empty:
        raise ValueError("Prisserien må ikke være tom.")
        # raise ValueError viser en fejl, hvis inputtet ikke indeholder data

    # is_numeric_dtype() kontrollerer, om værdierne er numeriske
    if not pd.api.types.is_numeric_dtype(priser):
        raise TypeError("Priser skal være numeriske.")
        # Sikrer, at priserne består af tal og ikke eksempelvis tekst

    # pct_change() beregner procentændringen fra én observation til den næste
    # fill_method=None forhindrer automatisk udfyldning af manglende værdier
    return priser.pct_change(fill_method=None)


# Erstat return priser.pct_change(fill_method=None) med return priser.diff() for at få fejl