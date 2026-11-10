# Jobmarket Portfolio

## Formål

Dette repository indeholder praktiske Python-projekter inden for dataanalyse, statistik og finans.

Formålet er at demonstrere programmeringsfærdigheder, analytisk problemløsning og anvendelse af data til at undersøge konkrete problemstillinger. Projektet fungerer samtidig som en løbende portfolio med fokus på at omsætte teoretisk viden til praktiske analyser.

## Projekter

### 1. Grundlæggende dataanalyse – Titanic

Analyse af passagerdata fra Titanic med fokus på databehandling, deskriptiv statistik og visualisering.

- Undersøgelse af datatyper, manglende værdier og dubletter.
- Deskriptiv statistik og gruppering af data.
- Analyse af overlevelsesandele fordelt på passagerklasse og køn.
- Visualisering af resultater med Matplotlib.
- Opdeling af kode i genbrugelige funktioner.

**Datasæt:** [Titanic Dataset – Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

### 2. Datahåndtering og afkastberegning – Pandas og NumPy

Praktiske øvelser i databehandling og numeriske beregninger med historiske aktiekurser.

- Filtrering, sortering og gruppering af data.
- Sammenlægning og omstrukturering af datasæt.
- Beregning af procentvise aktieafkast.
- Analyse af afkast på tværs af aktier.
- Udvikling og test af en genbrugelig afkastfunktion med pytest.

**Datasæt:** `stockdata.csv` – historiske aktiekurser for fem aktier i perioden 2007–2016.

### 3. Dataaudit og visualisering – Bike Sharing

En samlet analyse af cykeludlejning med fokus på datakvalitet, statistiske sammenhænge og visualisering.

- Dataaudit med undersøgelse af datatyper, manglende værdier, dubletter og potentielle outliers.
- Udarbejdelse af dataordbog.
- Visualisering af cykeludlejning over tid og fordeling af efterspørgsel.
- Analyse af sammenhængen mellem temperatur og cykeludlejning.
- Sammenligning af lineære og polynomielle modeller ved hjælp af R².
- Gemning af visualiseringer i projektets `outputs/`-mappe.

**Datasæt:** [Bike Sharing Dataset – UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)

## Teknologier

- **Python** – programmeringssprog.
- **pandas** – databehandling og analyse.
- **NumPy** – numeriske beregninger.
- **Matplotlib** – datavisualisering.
- **pytest** – automatiserede tests.
- **Git** – versionsstyring.

## Opsætning og kørsel

Projektet kræver Python 3.12 eller nyere.

1. Klon repository'et:

   ```bash
   git clone https://github.com/oliverlarsen-jpg/Jobmarket_portfolio.git
   cd Jobmarket_portfolio
   ```

2. Opret og aktivér et virtuelt miljø:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Installér afhængigheder:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Kør et analyse-script fra projektmappen:

   ```bash
   python 01_arbejdsmiljø_og_baseline.py
   python afkast.py
   python 03_bike_sharing.py
   ```

5. Kør automatiserede tests:

   ```bash
   python -m pytest -v
   ```

## Begrænsninger

Analyserne er udviklings- og demonstrationsprojekter, og resultaterne skal fortolkes med udgangspunkt i de anvendte datasæt og metoder.

- **Titanic:** Datasættet beskriver én historisk hændelse og kan ikke uden videre generaliseres til andre populationer.
- **Aktiedata:** Analysen omfatter fem aktier i en afgrænset historisk periode. Historiske afkast er ikke nødvendigvis repræsentative for fremtidige afkast.
- **Bike Sharing:** Datasættet dækker en begrænset periode og et bestemt geografisk område. Observerede statistiske sammenhænge dokumenterer ikke i sig selv årsagssammenhænge.
- **Statistiske modeller:** Resultaterne afhænger af datakvalitet, valg af variable og modellernes antagelser.

## Status og næste skridt

Projektet er under løbende udvikling. Fremtidige projekter vil udvide portfolioen med mere avancerede metoder inden for:

- Statistisk analyse og modellering.
- Finansielle data og afkastmodellering.
- Prediktive modeller og machine learning.
- Kreditrisiko og risikomodellering.