from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

DATA_PATH = Path("results/merged_data.csv")
PLOT_PATH = Path("results/sp500_vs_sentiment.png")


def main():
    df = pd.read_csv(DATA_PATH)

    
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    df["return"] = df["close"].pct_change()

    df = df.dropna(subset=["return", "sentiment_ma7"])

    X = df[["sentiment_ma7"]]
    X = sm.add_constant(X)  
    y = df["return"]

    model = sm.OLS(y, X).fit()
    print(model.summary())

    plt.figure(figsize=(8, 5))

    
    plt.scatter(df["sentiment_ma7"], df["return"], alpha=0.4, label="Daily Data")

    
    x_vals = np.linspace(df["sentiment_ma7"].min(), df["sentiment_ma7"].max(), 200)
    X_line = sm.add_constant(x_vals)
    y_pred = model.predict(X_line)

    plt.plot(x_vals, y_pred, linewidth=2, label="Regression Line")

    plt.xlabel("WSB Sentiment (MA7)")
    plt.ylabel("S&P 500 Daily Return")
    plt.title("Regression: Sentiment → Return")
    plt.legend()
    plt.tight_layout()


    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(PLOT_PATH)
    plt.close()


if __name__ == "__main__":
    main()
