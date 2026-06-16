import pandas as pd  

def analyse_products(df:pd.DataFrame) -> dict:
    stats = {}

    # Top 5 catégories
    stats["top_categories"] = (
        df.groupby("category")["product_id"]
        .count()
        .sort_values(ascending=False)
        .head(5)
        )
    
    # Prix moyen par catégorie
    stats["avg_price_by_category"] = (
        df.groupby("category")["price"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )

    #Produits en rupture de stocks
    stats["out_of_stock"] = df[df["stock_quantity"] == 0][["product_name","category","price"]]

    # Note moyenne et prix moyen par catégories
    stats["pivot_category"] = pd.pivot_table(
        df,
        values=["price","rating_avg"],
        index="category",
        aggfunc="mean"
    ).round(2)

    return stats

def analyse_users(df:pd.DataFrame) -> dict:
    stats = {}

    # Répartition par loyalty_tiers
    stats["loyalty_distribution"] = df["loyalty_tier"].value_counts()

    # Age moyen par income_level
    stats["avg_age_by_income"] = (
        df.groupby("income_level")["age"]
        .mean()
        .round(1)
    )

    # Top 5 pays
    stats["top_countries"] = df["country"].value_counts().head(5)

    return stats

def analyse_purchases(df: pd.DataFrame) -> dict:
    stats = {}

    # Chiffre d'affaire total
    stats["total_revenue"] = df["total_amount"].sum().round(2)

    # CA par mois
    df["month"] = df["order_date"].dt.to_period("M")
    stats["revenue_by_month"] = (
        df.groupby("month")["total_amount"]
        .sum()
        .round(2)
    )

    # Panier moyen
    stats["avg_basket"] = df["total_amount"].mean().round(2)

    return stats

def analyze_all(cleaned:dict) -> dict:
    print("\n[analyser] Analyse en cours...")
    results = {}
    results["products"] = analyse_products(cleaned["products"])
    results["users"] = analyse_users(cleaned["users"])
    results["purchases"] = analyse_purchases(cleaned["purchases"])
    print("[analyser] Terminé")
    return results

def print_results(results: dict) -> None:
    print("\n===== PRODUITS =====")
    print("\nTop catégories:")
    print(results["products"]["top_categories"])
    print("\nPrix moyen par catégorie:")
    print(results["products"]["avg_price_by_category"])
    print("\nProduits en rupture:")
    print(results["products"]["out_of_stock"].head())
    print("\nPivot catégorie:")
    print(results["products"]["pivot_category"])

    print("\n===== USERS =====")
    print("\nLoyalty tiers:")
    print(results["users"]["loyalty_distribution"])
    print("\nAge moyen par income:")
    print(results["users"]["avg_age_by_income"])
    print("\nTop pays:")
    print(results["users"]["top_countries"])

    print("\n===== PURCHASES =====")
    print(f"\nCA total: ${results['purchases']['total_revenue']}")
    print(f"Panier moyen: ${results['purchases']['avg_basket']}")
    print("\nCA par mois:")
    print(results["purchases"]["revenue_by_month"])


