import pandas as pd
from textblob import TextBlob
from pathlib import Path


DATA_DIR = Path("data")  

RAW_PATH = DATA_DIR / "wallstreetbets_2022.csv"
OUT_PATH = DATA_DIR / "wsb_daily_sentiment.csv"


def get_polarity(text):
    return TextBlob(str(text)).sentiment.polarity


def main():
    df = pd.read_csv(RAW_PATH, low_memory=False)

    df = df[["timestamp", "body"]].dropna()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    df["sentiment"] = df["body"].apply(get_polarity)

    daily = df.groupby("date")["sentiment"].mean().reset_index()

    daily.to_csv(OUT_PATH, index=False)
    print(f"Saved daily sentiment to {OUT_PATH}")


if __name__ == "__main__":
    main()
