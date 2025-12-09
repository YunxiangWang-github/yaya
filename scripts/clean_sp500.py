import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")  

def main():
    sp = pd.read_csv(DATA_DIR / "sp500_raw.csv")

    sp["date"] = pd.to_datetime(sp["date"])
    sp = sp.sort_values("date")
    sp = sp.dropna(subset=["date", "close"])

    sp.to_csv(DATA_DIR / "sp500_clean.csv", index=False)
    print("Saved cleaned data to data/sp500_clean.csv")

if __name__ == "__main__":
    main()
