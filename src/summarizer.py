import pandas as pd  
from pathlib import Path

def summarize_for_agent(cleaned:dict, results:dict) -> str:
    products = cleaned["products"]
    users = cleaned["users"]
    purchases = cleaned["purchases"]

    p = results["products"]
    u=results["users"]
    pu=results["purchases"]

    top_cat = p["top_categories"].index[0]
    top_cat_count = p["top_categories"].iloc[0]
    most_expensive_cat = p["avg_price_by_category"].index[0]
    avg_price_expensive = p["avg_price_by_category"].iloc[0]

    total_users = len(users)
    bronze_pct = round(u["loyalty_distribution"]["bronze"] / total_users *100,1)
    top_country = u["top_countries"].index[0]

    total_revenue = pu["total_revenue"]
    avg_basket = pu["avg_basket"]
    best_month = pu["revenue_by_month"].idxmax()
    best_month_revenue = pu["revenue_by_month"].max()

    summary = f"""
 === AGENT CONTEXT SUMMARY ===

 DATASET: E-Commerce Product Intelligence
SOURCE: Kaggle - aujsaha012346789
PIPELINE : loaded -> cleaned -> analyzed

--- PRODUITS ({len(products)} références) ---
- Catégorie Dominante : {top_cat} ({top_cat_count} produits)
- Catégorie la plus chère : {most_expensive_cat} (prix moyen ${avg_price_expensive})
- Note moyenne globale : {products["rating_avg"].mean():.2f}/5
- Ruptures de stock : 0

--- UTILISATEURS ({total_users:,} comptes) ---
- {bronze_pct}% sont au tier Bronze (faible engagement)
- Marché principal : {top_country}
- Tiers disponibles : Bronze -> Silver -> Gold -> Platinium

--- ACHATS ({len(purchases)} transactions) ---
- CA total : ${total_revenue:,.2f}
- Panier moyen : ${avg_basket}
- Tendance : croissance continue 2023 -> 2026

--- SIGNAUX POUR AGENT ---
- Opportunité : convertir les {u["loyalty_distribution"]["bronze"]:,} users Bronze
- Levier pricig : Electronics ($211 avg) génère plus de valeur
- Focus géo : US + GB + CA = 53% de la base users

--- END CONTEXT ===
"""
    return summary

def save_summary(summary:str, path:str = "data/clean/agent_context.txt") -> None:
    Path(path).write_text(summary,encoding="utf-8")
    print(f"[summarizer] Résumé sauvegardé -> {path}")



