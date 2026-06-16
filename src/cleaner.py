import pandas as pd

def clean_products(df: pd.DataFrame) -> pd.DataFrame:

    df["date_added"] = pd.to_datetime(df["date_added"])

    median_rating = df["rating_avg"].median()
    df["rating_avg"] = df["rating_avg"].fillna(median_rating)

    df = df.drop_duplicates(subset=["product_id"])

    df["category"] = df["category"].str.strip().str.lower()
    df["subcategory"] = df["subcategory"].str.strip().str.lower()
    df["brand"] = df["brand"].str.strip().str.lower()

    print(f"[cleaner] products -> {df.shape[0]} lignes, rating_avg manquants: {df['rating_avg'].isnull().sum()}")
    return df

def clean_users(df:pd.DataFrame) -> pd.DataFrame:
    df["gender"] = df["gender"].str.strip().str.lower()
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["loyalty_tier"] = df["loyalty_tier"].str.strip().str.lower()
    df["income_level"] = df["income_level"].str.strip().str.lower()
    df = df.drop_duplicates(subset=["user_id"])
    print(f"[Cleaner] users -> {df.shape[0]} lignes")
    return df

def clean_purchases(df:pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.drop_duplicates(subset=["purchase_id"])

    df["computed_total"] = df["quantity"] * df["unit_price"]
    df["total_mismatch"] = (df["total_amount"] - df["computed_total"]).abs() > 0.0
    n_mismatch = df["total_mismatch"].isnull().sum()
    print(f"[cleaner] purchases -> {df.shape[0]} lignes, {n_mismatch} incohérences")
    return df

def clean_reviews(df:pd.DataFrame) -> pd.DataFrame:
    df["review_date"] = pd.to_datetime(df["review_date"])

    df["purchase_id"] = df["purchase_id"].fillna("UNKNOWN")
    df = df.drop_duplicates(subset=["review_id"])

    df = df[df["rating"].between(1,5)]
    print(f"[cleaner] reviews -> {df.shape[0]} lignes")
    return df

def clean_sessions(df:pd.DataFrame) -> pd.DataFrame:
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["device_type"] = df["device_type"].str.strip().str.lower()
    df["referrer_source"] = df["referrer_source"].str.strip().str.lower()
    df = df.drop_duplicates(subset=["session_id"])
    print(f"[cleaner] sessions -> {df.shape[0]} lignes")
    return df

def clean_interactions(df:pd.DataFrame) -> pd.DataFrame:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["interaction_type"] = df["interaction_type"].str.strip().str.lower()

    df = df[df["dwell_time_ms"] >= 0]
    df = df.drop_duplicates(subset=["interaction_id"])
    print(f"[cleaner] interactions -> {df.shape[0]} lignes")
    return df

def clean_all(datasets:dict) -> dict:
    cleaners = {
        'products': clean_products,
        'users': clean_users,
        'purchases': clean_purchases,
        'reviews': clean_reviews,
        'sessions': clean_sessions,
        'interactions': clean_interactions
    }
    cleaned = {}
    for name,df in datasets.items():
        print(f"\n--- Nettoyage : {name} ---")
        cleaned[name] = cleaners[name](df)
    return cleaned