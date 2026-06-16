import pandas as pd  
from pathlib import Path

CLEAN_DIR = Path("data/clean")

def export_csv(df:pd.DataFrame, filename:str) -> None:
    path = CLEAN_DIR/filename
    df.to_csv(path,index=False)
    print(f"[exporter] {filename} -> {path}.")

def export_all(cleaned:dict) -> None:
    print("\n[exporter] Export des datasets nettoyés...")
    for name, df in cleaned.items():
        export_csv(df,f"{name}_clean.csv")
    print("[exporter] Terminé.")

def export_analysis(results: dict) -> None:
    print("\n[exporter] Export des analyses...")

    # Pivot catégories produits
    results["products"]["pivot_category"].to_csv( CLEAN_DIR/ "pivot_category.csv")
    print("[exporter] pivot_category.csv")

    # CA par mois
    results["purchases"]["revenue_by_month"].to_csv(CLEAN_DIR / "revenue_by_month.csv")
    print("[exporter] revenue_by_month.csv")

    # Loyalty distribution
    results["users"]["loyalty_distribution"].to_csv(CLEAN_DIR / "loyalty_distribution.csv")
    print("[exporter] loyalty_distribution.csv")

    print("[exporter] Terminé.")

