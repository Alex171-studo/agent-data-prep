# agent-data-prep

Pipeline de préparation des données pour agents LLM construit sur un dataset e-commerce réel.

## Pourquoi ce projet ?

La performance d'un agent LLM dépend directement de la qualité des données qu'on lui injecte.
Ce pipeline transforme des CSV bruts en un contexte structuré, propre et prêt à être utilisé dans un prompt.

## Pipeline

data/row ->loader->cleaner->analyser->exporter->summarizer->agent_context.txt

## Structure

agent-data-prep/
 |----src/
 | |---loader.py # Chargement et inspection des CSV
   |---cleaner.py # Nettoyage:valeurs manquantes,doublons,types
   |---analyzer.py # Analyses:groupby,pivot_table_agrégations
   |---exporter.py # Export CSV des données nettoyées et analyses
   |---summarizer.py # Génération du résumé pour un agent LLM
 |---data/
   |---raw/ # Données brutes (non versionnées)
   |---clean # Données nettoyées (non versionnées)
 |---main.py
 |---README.md

## Dataset
[E-Commerce Product Intelligence Dataser](https://www.kaggle.com/datasets/anujsaha0123456789/e-commerce-product-intelligence-dataset) - Kaggle (MIT License)

6 fichiers CSV : products, users, purchases, reviews, sessions, interactions

## Setup

```bash
git clone 
cd agent-data-prep
python -m venv venv && source venv/bin/activate
pip install pandas kaggle

# Configurer Kaggle API : https://www.kaggle.com/settings
mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json

# Téléchargerle dataset
kaggle datasets download -d anujsaha0123456789/e-commerce-product-intelligence-dataset -p data/raw --unzip

python main.py
```

## Ce que ça couvre (Pandas)

- `read_csv`, `to_csv`, `to_json`
- `fillna`, `dropna`, `drop_duplicates`, `astype`
- `groupby`, `pivot_table`, `sort_values`
- `str.strip`, `str.lower`, `dt.to_period`
- Series : `value_counts`, `idxmax`, `between`

## Prochaine étape

Brancher un agent LLM sur `agent_context.txt` pour Q&A automatisé sur les données. 