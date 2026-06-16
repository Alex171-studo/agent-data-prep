import pandas as pd  
from pathlib import Path

RAW_DIR = Path("data/raw")

def load_csv(filename: str) -> pd.DataFrame:
    path = RAW_DIR/filename
    df = pd.read_csv(path)
    print(f"[loader]{filename} -> {df.shape[0]} lignes et {df.shape[1]} colonnes ")
    return df

def load_all() -> dict[str, pd.DataFrame]:
    files = list(RAW_DIR.glob("*.csv"))
    datasets = {}
    for f in files:
        datasets[f.stem] = load_csv(f.name)
    return datasets

def quick_inspect(df:pd.DataFrame, name: str = "") -> None:
    print(f"\n{'='*40}")
    print(f"Dataset : {name}")
    print(f"Shape   : {df.shape}")
    print(f"Colonnes : {list(df.columns)}")
    print(f"\nTypes:\n{df.dtypes}")
    print(f"\nValeurs manquantes:\n{df.isnull().sum()}")
    print(f"{'='*40}")
