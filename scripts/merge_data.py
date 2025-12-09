import pandas as pd
from pathlib import Path

SP_PATH = Path("data/sp500_clean.csv")
WSB_PATH = Path("data/wsb_daily_sentiment.csv")


OUT_PATH = Path("results/merged_data.csv")

def main():

    sp = pd.read_csv(SP_PATH)
    sp['date'] = pd.to_datetime(sp['date']).dt.date

    daily = pd.read_csv(WSB_PATH)
    daily['date'] = pd.to_datetime(daily['date']).dt.date

    merged = pd.merge(sp, daily, on='date', how='inner')

    merged = merged[merged['date'] >= pd.to_datetime("2022-01-01").date()]

    merged = merged.sort_values('date')

    merged['sentiment_ma7'] = merged['sentiment'].rolling(window=7).mean()

    OUT_PATH.parent.mkdir(exist_ok=True)  
    merged.to_csv(OUT_PATH, index=False)

    print(f"Saved merged dataset to {OUT_PATH}")

if __name__ == "__main__":
    main()
