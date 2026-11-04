#%%
import pandas as pd  # Bruges til at oprette og håndtere dataserier
import pytest  # Bruges til at teste koden og kontrollere forventede fejl

from afkast import beregn_afkast  # Importerer funktionen fra afkast.py


def test_beregner_korrekte_afkast():
    priser = pd.Series([100, 110, 99])  # Opretter tre eksempelpriser

    resultat = beregn_afkast(priser)  # Beregner afkastet på priserne

    # pd.isna() kontrollerer, om en værdi mangler (NaN)
    # Det første afkast er NaN, fordi der ikke findes en tidligere pris
    assert pd.isna(resultat.iloc[0])

    # iloc[] henter en værdi ud fra dens placering (0 er første række)
    # pytest.approx() tillader små afrundingsforskelle i decimaltal
    # assert kontrollerer, om resultatet stemmer med det forventede
    assert resultat.iloc[1] == pytest.approx(0.10)  # 100 til 110 = 10 %
    assert resultat.iloc[2] == pytest.approx(-0.10)  # 110 til 99 = -10 %


def test_tomt_datasaet():
    priser = pd.Series(dtype=float)  # Opretter en tom Series med numerisk datatype

    # pytest.raises() kontrollerer, om den forventede fejl bliver udløst
    with pytest.raises(ValueError):
        beregn_afkast(priser)


def test_manglende_vaerdier():
    priser = pd.Series([100, None, 120])  # None repræsenterer en manglende værdi

    resultat = beregn_afkast(priser)  # Beregner afkast med manglende data

    # Første kontrol: afkastet på den manglende pris kan ikke beregnes
    assert pd.isna(resultat.iloc[1])

    # Anden kontrol: afkastet kan heller ikke beregnes for 120,
    # da den foregående pris mangler
    assert pd.isna(resultat.iloc[2])


def test_forkert_inputtype():
    priser = [100, 110, 120]  # En almindelig Python-liste, ikke en pandas Series

    # Kontrollerer, at funktionen afviser den forkerte inputtype
    with pytest.raises(TypeError):
        beregn_afkast(priser)


def test_ikke_numeriske_priser():
    priser = pd.Series(["100", "110", "120"])  # Tallene er tekststrenge

    # Kontrollerer, at funktionen afviser tekst i stedet for numeriske værdier
    with pytest.raises(TypeError):
        beregn_afkast(priser)

# %%

### Hele testen kan køres med 'python -m pytest -v' i terminalen
