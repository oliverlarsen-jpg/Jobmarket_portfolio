# Jobmarket Portfolio

## 1. Formål

Dette projekt bruges til at opbygge en Python-baseret portfolio med praktiske projekter inden for dataanalyse, statistik, finans og risikomodellering.

Formålet er at demonstrere programmeringsfærdigheder, analytisk problemløsning og anvendelse af data til at besvare konkrete problemstillinger.

## 2. Opsætning

Projektet anvender Python og et virtuelt miljø til at holde projektets pakker adskilt fra øvrige Python-installationer.

### Krav
- Python 3
- Visual Studio Code (anbefalet)
- Git (anbefalet)

### Installation

1. Klon projektet, eller download projektmappen.
2. Åbn terminalen i projektmappen.
3. Opret et virtuelt miljø:

   ```bash
   python3 -m venv .venv
   ```

4. Aktivér miljøet på macOS:

   ```bash
   source .venv/bin/activate
   ```

5. Installér de nødvendige Python-pakker:

   ```bash
   python -m pip install -r requirements.txt
   ```

## 3. Projektforløb

### Trin 1 – Grundlæggende dataanalyse med Titanic-datasættet

**Formål:** At lære at indlæse, undersøge og analysere data med pandas samt visualisere resultater med Matplotlib.

**Gennemført:**
- Indlæst og undersøgt Titanic-datasættet.
- Undersøgt datatyper, manglende værdier og deskriptiv statistik.
- Beregnet statistiske nøgletal fordelt på grupper, herunder gennemsnit, standardafvigelse, median og antal observationer.
- Analyseret overlevelsesandele på tværs af passagerklasser og køn.
- Oprettet og gemt søjlediagrammer med Matplotlib.
- Opdelt koden i genbrugelige funktioner.
- Arbejdet med en `main()`-funktion til at samle analysens arbejdsgang.

### Trin 2 – Pandas, NumPy og automatiserede tests

**Formål:** At arbejde mere effektivt med datastrukturer, beregninger og kvalitetssikring af Python-kode.

**Gennemført:**
- Arbejdet med filtrering, sortering og gruppering af data.
- Arbejdet med sammenlægning og omstrukturering af datasæt.
- Beregnet procentvise ændringer i aktiekurser med pandas og NumPy.
- Undersøgt afkast og gennemsnitlige afkast på tværs af aktier.
- Opbygget en funktion til beregning af afkast.
- Oprettet automatiserede tests med pytest.
- Testet normal funktionalitet, tomme datasæt, manglende værdier og ugyldige input.
- Kontrolleret, at testene opdager fejl i beregningerne.

### Trin 3 – Dataaudit, visualisering og reproducerbar analyse

**Formål:** At gennemføre en samlet dataanalyse, dokumentere datakvaliteten og gøre analysen reproducerbar på en anden computer.

#### Trin 3.1 – Dataaudit
- Indlæst Bike Sharing-datasættet.
- Undersøgt datasættets størrelse, kolonner og datatyper.
- Kontrolleret manglende værdier og dubletter.
- Undersøgt potentielle outliers med IQR-metoden.
- Udarbejdet en dataordbog med variabelnavne, datatyper og forklaringer.

#### Trin 3.2 – Visualisering
- Oprettet en tidsserie over daglige cykeludlejninger fordelt på brugertype.
- Oprettet et histogram over fordelingen af daglige cykeludlejninger.
- Oprettet et scatterplot over temperatur og antal cykeludlejninger.
- Tilføjet en lineær tendenslinje til scatterplottet.
- Beregnet og sammenlignet R² for første-, anden- og tredjegradspolynomier.
- Undersøgt sammenhængen mellem temperatur og cykeludlejninger uden at sidestille korrelation med kausalitet.
- Gemmer visualiseringer i projektets `outputs/`-mappe.

#### Trin 3.3 – Reproducerbar kørsel
- Samlet dataaudit, visualiseringer og beregninger i et Python-script.
- Oprettet `requirements.txt` med projektets nødvendige Python-pakker.
- Dokumenteret installation og kørsel i denne README.
- Arbejdet med en ensartet projektstruktur, så analysen kan køres fra projektmappen.
- Forberedt projektet, så en anden person kan installere afhængighederne og genskabe analysens resultater.

## 4. Kørsel af analyser

Aktivér først det virtuelle miljø, og kør derefter det relevante Python-script fra projektmappen.

Eksempel på aktivering på macOS:

```bash
source .venv/bin/activate
```

Eksempler på kørsel:

```bash
python test.py
python afkast.py
python 01_arbejdsmiljø_og_baseline.py
```

Kør Bike Sharing-analysen med:

```bash
python 03_Datahåndtering_og_analyse.py
```

Automatiserede tests kan køres med:

```bash
python -m pytest -v
```

## 5. Projektstruktur

Projektet indeholder blandt andet følgende filer og mapper:

- `README.md` – projektbeskrivelse, opsætning og dokumentation.
- `requirements.txt` – nødvendige Python-pakker.
- `test.py` – indledende test af Python-opsætningen.
- `titanic.csv` – datasæt til den indledende dataanalyse.
- `01_arbejdsmiljø_og_baseline.py` – grundlæggende dataanalyse og visualisering.
- `stockdata.csv` – aktiekursdata til pandas- og NumPy-øvelser.
- `afkast.py` – funktion til beregning af afkast.
- `test_afkast.py` – automatiserede tests af afkastfunktionen.
- `03_bike_sharing.csv` – datasæt til dataaudit og visualisering.
- `03_bike_sharing.py` – analyse af Bike Sharing-datasættet.
- `outputs/` – gemte figurer og andre analyseoutput.
- `.gitignore` – filer og mapper, som Git ikke skal versionsstyre.
- `.venv/` – lokalt virtuelt Python-miljø, som ikke gemmes i Git.

Listen er vejledende og bør tilpasses de faktiske filnavne i projektet.

## 6. Teknologier

- **Python** – programmeringssprog.
- **pandas** – indlæsning, bearbejdning og analyse af data.
- **NumPy** – numeriske beregninger.
- **Matplotlib** – visualisering af data.
- **pytest** – automatiserede tests.
- **Git** – versionsstyring, herunder feature-branch

## 7. Status og næste skridt

Projektet er under udvikling. Nye projekter og analyser tilføjes løbende med fokus på at opbygge praktiske kompetencer inden for dataanalyse, statistik, finans og risikomodellering.

Fremtidige projekter kan blandt andet omfatte:
- Mere avanceret statistisk analyse.
- Finansielle data og afkastmodellering.
- Prediktive modeller og machine learning.
- Kreditrisiko og risikomodellering.
- Datavisualisering og formidling af analytiske resultater.