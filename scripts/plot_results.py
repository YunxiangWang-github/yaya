import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERGED_PATH = ROOT / "results" / "merged_data.csv"
OUT_DIR = ROOT / "results"
OUT_FILE = OUT_DIR / "sp500_vs_sentiment.png"

def main():
    df = pd.read_csv(MERGED_PATH)
    df["date"] = pd.to_datetime(df["date"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(df['date'], df['close'], color='blue', label='SP500')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('SP500 Close Price', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()

    ax2.plot(df['date'], df['sentiment_ma7'], color='red', label='Sentiment (MA7)')
    ax2.set_ylabel('Sentiment Index', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title("SP500 vs WSB Sentiment (MA7)")

    plt.tight_layout()
    plt.savefig(OUT_FILE)
    plt.close()

    print(f"Plot saved to: {OUT_FILE}")

if __name__ == "__main__":
    main()
