


rule all:
    input:
        "results/sp500_vs_sentiment.png"

rule download_sp500:
    output:
        "data/sp500_raw.csv",
        "data/sp500_raw.sha256"
    shell:
        "python scripts/download_sp500.py"

rule clean_sp500:
    input:
        "data/sp500_raw.csv"
    output:
        "data/sp500_clean.csv"
    shell:
        "python scripts/clean_sp500.py"

rule clean_wsb:
    input:
        "data/wallstreetbets_2022.csv"
    output:
        "data/wsb_daily_sentiment.csv"
    shell:
        "python scripts/clean_wsb.py"

rule merge_data:
    input:
        sp500 = "data/sp500_clean.csv",
        wsb   = "data/wsb_daily_sentiment.csv"
    output:
        "results/merged_data.csv"
    shell:
        "python scripts/merge_data.py"

rule plot_results:
    input:
        "results/merged_data.csv"
    output:
        "results/sp500_vs_sentiment.png"
    shell:
        "python scripts/plot_results.py"
