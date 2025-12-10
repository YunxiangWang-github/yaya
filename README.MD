# WallStreetBets Sentiment vs. S&P 500: Is There a Relationship?

## Contributors
- Yunxiang Wang  
- Leonard Cao  

---

## Summary

This project investigates whether aggregated sentiment expressed on Reddit’s r/WallStreetBets (WSB) is meaningfully related to movements in the S&P 500 index, one of the most widely followed benchmarks of U.S. equity markets. In recent years, WSB has become synonymous with meme stocks, speculative trading, and emotionally charged discussions about financial markets. Headlines around dramatic price movements in stocks such as GameStop (GME) and AMC have frequently framed WSB users as catalysts, raising the broader question of whether the “mood” of this online community has measurable impact beyond a small set of highly discussed tickers.

Our core research question is: **Does daily WallStreetBets sentiment show a measurable relationship with the S&P 500 index?** To address this question, we assembled two primary datasets. The first contains daily closing prices for the S&P 500 index, serving as a proxy for overall U.S. stock market performance. The second contains daily aggregated sentiment scores derived from WSB posts, providing a numerical summary of the community’s mood on each calendar day. We then designed a reproducible workflow that cleans, aligns, and merges these datasets into a unified time series in order to enable comparative visualization and quantitative analysis.

Methodologically, the project emphasizes reproducibility and transparency. Instead of performing ad-hoc manual manipulations of CSV files, we rely on a Snakemake workflow that can be executed end-to-end on a clean environment. All data preparation and analysis steps are captured in python file, and the workflow orchestrates them in a structured and repeatable manner. This approach supports both the pedagogical goals of the course and broader best practices in data-intensive research.

Our exploratory analysis proceeds in several stages. We first visualize S&P 500 index levels and WSB sentiment over time, inspecting whether any obvious co-movements or lagged relationships appear. Because sentiment derived from social media is inherently noisy, we also compute a 7-day moving average of daily sentiment scores to highlight broader trends. Next, we compute summary statistics and correlation coefficients between sentiment and index values (both same-day and with simple lags). Finally, we fit basic regression models to test whether sentiment explains meaningful variation in S&P 500 levels.

The resulting evidence consistently points in the same direction: **there is no strong, stable, or robust relationship between aggregated WSB sentiment and S&P 500 index levels**. Visualizations reveal that sentiment fluctuates rapidly and irregularly, while the S&P 500 evolves more smoothly in response to macroeconomic forces. Correlation coefficients remain close to zero even when smoothing sentiment and experimenting with simple lag structures. Regression models indicate that sentiment explains virtually none of the variation in index values.

Taken together, our findings suggest that WSB sentiment—at least in the aggregated daily form analyzed here—does not provide useful information for understanding or forecasting broad market indices. This does not mean that sentiment is irrelevant in financial markets; rather, it underscores the importance of granularity (e.g., ticker-level analysis) and modeling choices. The project closes by outlining several potential extensions, including ticker-specific sentiment modeling, advanced natural language processing (NLP) for financial slang, richer time-series techniques, and integration of multiple sentiment sources. Beyond its substantive conclusion, the project aims to demonstrate a clear, well-documented, and reproducible workflow for social-media-based financial analysis.


---

## Reproducing Our Workflow

All steps required to reproduce our results are listed below.  
After obtaining the raw datasets (due to licensing constraints, raw files are not included in the repository), the entire analysis can be regenerated with Snakemake.

### 1. Install dependencies
All required Python packages are listed in `requirements.txt`.

### 2. Run the full pipeline with Snakemake
```
snakemake --cores 1
```

---

## Workflow Transparency

This section documents all major steps in our workflow and the corresponding artifacts that appear in the repository. Each stage of the pipeline produces outputs that can be inspected directly, ensuring full transparency.

### 1. Repository Structure Overview

```text
data/           # Raw, cleaned, and processed datasets
notebooks/      # Interactive cleaning, merging, and analysis notebooks
scripts/        # Python scripts used by Snakemake
results/        # Final merged dataset and generated visualizations
Snakefile       # Defines the complete workflow
requirements.txt# Python dependencies
```


### 2. Scripts and Their Inputs/Outputs

| Script | Input | Output | Purpose |
|--------|--------|---------|---------|
| `scripts/clean_sp500.py` | `data/sp500_raw.csv` | `data/sp500_clean.csv` | Cleans and standardizes S&P 500 data |
| `scripts/clean_wsb.py` | `data/wsb_raw.csv` | `data/wsb_daily_sentiment.csv` | Cleans and aggregates WallStreetBets sentiment |
| `scripts/merge_data.py` | `data/sp500_clean.csv`, `data/wsb_daily_sentiment.csv` | `results/merged_data.csv` | Aligns and merges both datasets |
| `scripts/plot_results.py` | `results/merged_data.csv` | `results/sp500_vs_sentiment.png` | Produces the main visualization |

All scripts are executed automatically when Snakemake runs.

### 3. Snakemake Workflow Overview

The Snakefile defines a four-stage workflow:

1. Clean S&P 500 data → `data/sp500_clean.csv`  
2. Clean WSB sentiment data → `data/wsb_daily_sentiment.csv`  
3. Merge both cleaned datasets → `results/merged_data.csv`  
4. Generate visualization → `results/sp500_vs_sentiment.png`

Each file listed above is produced by the workflow and included in the repository, enabling inspection of every intermediate and final artifact.

### 4. Notebooks for Manual Inspection (Optional)

The `notebooks/` folder contains interactive versions of each processing step:

- `clean_sp500.ipynb`
- `clean_wsb.ipynb`
- `merge_data.ipynb`
- `analysis_sentiment_stock.ipynb`

These notebooks mirror the scripted workflow and display intermediate checks and exploratory analysis.

---


## Data Profile

Our analysis is built on two primary datasets and one derived merged dataset, each fulfilling a distinct conceptual and technical role within the project: the S&P 500 index dataset, the WSB sentiment dataset, and a merged dataset that aligns the two on a common temporal axis.

### S&P 500 Dataset

The S&P 500 dataset consists of daily closing prices for the S&P 500 index. Each row represents a single trading day and includes at minimum a `date` column (formatted as `YYYY-MM-DD`) and a `close` column containing the index’s closing value for that day. The dataset is sourced from a reputable public financial data provider (such as the Federal Reserve Economic Data (FRED) system or Yahoo Finance). These sources are widely used in academic and industry research due to their reliability, consistent formatting, and long historical coverage.

An important property of this dataset is that it reflects **trading days only**. Weekends and market holidays are excluded because no official closing prices are recorded on those days. This affects how the S&P 500 series can be aligned with WSB sentiment, which exists for every calendar day. From a legal and ethical standpoint, the S&P 500 dataset is straightforward: it contains only public aggregate market information with no personal or sensitive content. Our use falls under non-commercial educational analysis and is consistent with typical terms of service for public financial data.

Before integration, we performed several light preprocessing steps. We verified that `date` values were valid, unique, and strictly increasing; confirmed that `close` values were numeric and free of missing entries; and removed any duplicate rows. These operations ensure that the S&P 500 time series is structurally sound and suitable as a baseline for subsequent merging and analysis.

### WallStreetBets Sentiment Dataset

The WallStreetBets sentiment dataset is derived from unstructured textual data posted on Reddit. Original WSB posts contain free-form text that ranges from serious analysis to jokes and memes, often using highly idiosyncratic slang. Rather than processing raw posts ourselves, we rely on an existing preprocessed dataset that provides **daily aggregated sentiment scores**. Each row records a `date` value and a numeric `sentiment` score summarizing the community’s mood for that day.

The dataset is designed to be privacy-preserving and compliant with platform constraints. It does not include usernames, post IDs, or raw text content; instead, it aggregates sentiment at the day level, which also reduces the dimensionality of the problem. Nevertheless, the dataset inherits several limitations. First, sentiment models are imperfect, especially when applied to sarcasm, humor, and non-standard language. Second, daily sentiment scores may be based on a small number of posts on some days, increasing sensitivity to noise. Third, extreme sentiment values may reflect transient activity bursts or model errors rather than genuine shifts in collective mood.

To prepare this dataset for analysis, we standardized date formats, removed rows with missing or clearly invalid sentiment scores, and restricted the time range to overlap with our S&P 500 data. We also created an additional variable, `sentiment_ma7`, defined as a 7-day moving average of the daily sentiment scores, to capture broader trends beyond high-frequency noise.

### Merged Dataset

The merged dataset, stored as `results/merged_data.csv`, integrates the S&P 500 and WSB sentiment datasets into a single table with four key columns: `date`, `close`, `sentiment`, and `sentiment_ma7`. We perform an inner join on the `date` column, ensuring that each row corresponds to a day for which we have both market data and sentiment data. A side effect of this decision is that weekend and holiday sentiment observations without S&P 500 values are dropped.

This merged dataset forms the analytical foundation of the project. It enables side-by-side visualization of sentiment and index levels, computation of correlations, and regression modeling. Conceptually, it aligns a market-level performance indicator (S&P 500) with an online community-level mood indicator (WSB sentiment), allowing us to test whether shifts in one correspond systematically to shifts in the other.

---

## Data Quality

Ensuring data quality is essential for trustworthy conclusions. We evaluate data quality separately for each source dataset and for the merged dataset, focusing on completeness, consistency, correctness, and interpretability.

### S&P 500 Data Quality

Because the S&P 500 dataset comes from a professional financial data provider, it is relatively robust. Our primary checks included:

- **Completeness:** verifying that all trading days in the chosen time window are represented;  
- **Missing values:** checking for null or NaN entries in the `close` column;  
- **Uniqueness and ordering:** verifying that each `date` appears at most once and that rows are sorted chronologically;  
- **Format correctness:** ensuring that `date` values comply with the expected `YYYY-MM-DD` format and that the `close` column is numeric.

These checks confirmed that only minor cleaning was required (e.g., enforcing explicit typing and sorting). We treat the resulting series as a “gold standard” baseline for market performance.

### WallStreetBets Sentiment Data Quality

The WSB sentiment dataset required more extensive quality assessment due to both the noisiness of social-media data and the complexity of sentiment modeling.

Our quality checks included:

- **Validity of sentiment scores:** identifying and removing rows with missing, NaN, or obviously invalid sentiment values (e.g., extreme outliers generated by model errors rather than genuine sentiment extremes);  
- **Date parsing:** verifying that all `date` values could be parsed into valid calendar dates and fell within our study period;  
- **Distributional checks:** inspecting the distribution of `sentiment` scores to ensure that ranges and patterns were plausible, and that outliers reflected meaningful events rather than systematic errors.

Even after cleaning, the sentiment series remains noisy, which is expected for social-media-derived measures. To mitigate this, we created `sentiment_ma7`, a 7-day moving average that smooths short-term fluctuations while still capturing meaningful shifts in community mood.

### Merged Dataset Quality

When merging the datasets, we focused on ensuring that the integration procedure did not introduce new quality problems. Key considerations were:

- **Row loss due to non-overlapping dates:** some days with sentiment but no S&P 500 close (e.g., weekends) are necessarily dropped. We documented this as a conceptual rather than a technical issue.  
- **Missing values after joining:** we verified that no rows in the merged dataset contained missing values in the `close`, `sentiment`, or `sentiment_ma7` columns.  
- **Type consistency:** we ensured that both datasets represented `date` in compatible formats before performing the join, preventing subtle misalignments.

After harmonizing types and performing the inner join, we inspected the merged dataset to confirm that it contained a continuous series of trading days with valid, aligned sentiment measures. The final merged dataset is free of missing values in key fields and ready for analysis.

---

## Findings

Our analysis consistently indicates that **aggregated WSB sentiment does not exhibit a strong or reliable relationship with S&P 500 index levels**.

When we visualize the two time series, the most striking impression is their qualitative mismatch. The S&P 500 index follows a relatively smooth trajectory: it trends upward or downward over extended periods, with occasional jumps associated with macroeconomic news, earnings reports, or policy announcements. In contrast, the WSB sentiment series oscillates rapidly, with sharp spikes and dips that often reflect localized conversations, viral memes, or enthusiasm around individual stocks.

To reduce noise, we compare the S&P 500 index with the 7-day moving average of sentiment (`sentiment_ma7`). While smoothing does reveal some medium-term swings in community mood, these do not align consistently with index movements. There are occasional intervals in which mildly positive sentiment coincides with rising index levels or negative sentiment overlaps with flat or declining markets, but these episodes are sporadic and not persistent enough to suggest a stable relationship.

Quantitatively, correlation analysis confirms the visual impression. The linear correlation between daily sentiment (or its moving average) and S&P 500 closing values is close to zero. We also compute simple lagged correlations to test whether sentiment today is related to index levels several days later, but these too remain weak and unstable across lags.

Finally, we fit basic regression models with S&P 500 closing values as the dependent variable and sentiment variables as predictors. These models explain virtually none of the variance in index levels; the estimated coefficients are small and often statistically insignificant. Together, these results strongly suggest that aggregated WSB sentiment lacks predictive power for broad market index behavior in the sample examined.

---

## Future Work

Although our findings indicate a negligible relationship between aggregated WSB sentiment and S&P 500 index levels, they also point toward several promising directions for future research and methodological refinement.

First, **granularity** may matter greatly. WSB conversations are often concentrated on a small set of specific tickers or sectors (e.g., meme stocks, high-growth tech firms, or highly shorted names). Aggregating sentiment across all posts into a single market-wide index may dilute strong signals related to individual securities. A natural extension is to construct **ticker-level sentiment indices**, aligning daily sentiment scores for specific stocks with their respective returns, volatility, or trading volume. Sector-level aggregations (e.g., technology, consumer discretionary) could also reveal relationships that are invisible at the broad index level.

Second, future work could leverage **more advanced NLP models** tailored to financial language and social-media slang. Our current sentiment dataset is based on relatively simple scoring methods that may misinterpret sarcasm, irony, or community-specific jargon. Fine-tuning transformer-based models (such as FinBERT or other finance-adapted architectures) on annotated WSB data could yield more accurate sentiment estimates and potentially reveal stronger relationships with market outcomes.

Third, our analysis focuses primarily on **contemporaneous correlations**. It remains plausible that sentiment reacts to price changes (i.e., is driven by the market) rather than the other way around. Future research could adopt more sophisticated time-series and causal frameworks, including Granger causality tests, vector autoregression (VAR), or state-space models, to examine whether sentiment systematically leads or lags market movements. Neural sequence models such as RNNs or transformer-based time-series architectures could further capture non-linear or regime-dependent dynamics.

Fourth, WSB is only one platform within a broader ecosystem of online investor communities. Extending the analysis to incorporate **multiple sentiment sources**—for example, Twitter/FinTwit, StockTwits, Discord trading servers, or Google Trends search volume—might provide a more stable and representative measure of retail investor sentiment. Combining signals across platforms could also help distinguish platform-specific chatter from broader market narratives.

Finally, future work could shift focus from level predictions to **risk-oriented metrics**, such as realized volatility, tail risk, or crash probabilities. Sentiment extremes may be more informative about the likelihood of sharp market moves or localized stress events than about average returns. Exploring these richer outcome variables may uncover more nuanced ways in which online communities interact with financial markets.

---

## Compliance with Licenses and Terms of Use

We reviewed the licensing, usage restrictions, and ethical considerations for all datasets and software tools used in this project. Our project complies with all relevant terms of use.

### S&P 500 Index Data
- Sourced from a public financial provider (e.g., Federal Reserve Economic Data (FRED) or Yahoo Finance).  
- These providers allow **non-commercial academic use**, data analysis, and redistribution of derived results (plots, analyses) but not necessarily redistribution of raw data files.  
- To comply with these terms, we **do not redistribute proprietary raw data**; users should obtain the raw CSV files directly from the provider following instructions in `README_DATA_SOURCES.md`.

### WallStreetBets Sentiment Data
- Sourced from a public aggregated dataset on Kaggle (contains **no raw Reddit text, usernames, IDs, or personal identifiers**).  
- The dataset is distributed under a permissive license that allows academic reuse.  
- Because only **daily aggregated sentiment scores** are included, our use complies with Reddit’s API and content redistribution policies by not exposing any user-generated text.

### Software and Libraries
- All computational tools used are open-source and licensed under permissive terms (MIT, BSD, Apache 2.0), including Python, Pandas, NumPy, Matplotlib, Snakemake, and Jupyter.  
- We cite these tools below in accordance with the course requirement.

Overall, the project adheres fully to licensing, privacy, and ethical constraints regarding data acquisition, storage, transformation, and publication.

---

## Licensing & Data Source Compliance Notes

### WallStreetBets 2022 (Kaggle)

- Dataset: “WallStreetBets 2022”, retrieved from Kaggle.  
  URL: https://www.kaggle.com/datasets/gpreda/wallstreetbets-2022  
- This dataset is user-uploaded content on Kaggle. The original dataset page does **not** declare a standard open license (public domain or CC-license).  
- As such, the dataset should be treated as “proprietary or restricted data under user upload” rather than open data.  
- To comply with usage norms and avoid copyright issues, this project **does not redistribute the raw CSV**. Instead, we only include derived and aggregated outputs (cleaned data, aggregated daily sentiment, merged dataset, plots), which are generated under our analytical workflow.  
- Use within this project is strictly for **non-commercial educational research** (course assignment). Redistribution of raw data would require explicit permission from the data uploader/owner.

### S&P 500 Index (SP500) via FRED

- Data series: “S&P 500 [SP500]”, provided via FRED (Federal Reserve Bank of St. Louis).  
  URL: https://fred.stlouisfed.org/series/SP500  
- The series is owned by S&P Dow Jones Indices LLC, and carries a copyright notice. According to FRED terms of use, reproduction, redistribution, or public sharing of the full dataset (including raw CSV) may require **prior written permission** from S&P.  
- This project uses the data strictly for **non-commercial, educational, analytical purposes** as allowed under FRED’s “personal / educational / research” license. We do **not** include the full raw dataset in the public repository.  
- For verification and reproducibility, we provide instructions in `README.md` for other researchers to fetch the data independently via FRED API, rather than redistributing the proprietary data directly.

### Summary of Compliance Approach

- We respect the original data licensing and ownership: raw or proprietary datasets are not redistributed.  
- We include only derived data (cleaned, merged, aggregated) and results (plots, tables), which can be shared under fair use / academic use.  
- Data source attribution and clear citation are provided to ensure transparency and replicability.  
- For any downstream usage beyond educational or research contexts (e.g., publication, public dataset release), users must verify licensing and obtain any required permissions from data providers.

---
## FAIR Archival Compliance (Findable, Accessible, Interoperable, Reusable)

To meet FAIR principles and the course requirement to publish the project with accurate metadata, we provide a fixed archival snapshot of our final project deliverables. This snapshot includes all derived datasets and generated outputs necessary to validate our findings.

### Archival Repository (UIUC Box)

A permanent, versioned snapshot of the project outputs has been published at the following UIUC Box link:

🔗 **https://uofi.box.com/s/0u3kct4mchbgk1ukzv6pm91hndkewcd6**

The archived folder includes the following artifacts:

- **`data/` folder**  
  Contains cleaned and preprocessed datasets used for analysis, including:
  - Cleaned S&P 500 time-series  
  - Cleaned WallStreetBets sentiment series  
  - Supporting intermediate files used during data preparation  

- **`merged_data.csv`**  
  The final integrated dataset that aligns S&P 500 closing prices with WSB sentiment on a shared timeline.  
  This file serves as the analytical foundation for correlation, visualization, and regression tasks.

- **`sp500_vs_sentiment.png`**  
  The main visualization comparing daily S&P 500 index values and aggregated WSB sentiment, used in the Findings section of the report.

These files represent the complete set of derived artifacts needed to reproduce the analytical results presented in this project.

### FAIR Criteria

This archival snapshot ensures the project meets all FAIR requirements:

- **Findable:**  
  Hosted at a permanent Box URL that provides stable access to the project’s outputs.

- **Accessible:**  
  All files in the archive can be viewed or downloaded directly via the share link, requiring no authentication.

- **Interoperable:**  
  Data is provided in widely compatible formats (CSV, PNG).  
  Metadata in this README, along with consistent file naming conventions, ensures clarity and machine-readability.

- **Reusable:**  
  The snapshot includes all cleaned and merged datasets, along with final results, allowing future students or researchers to reuse the data and verify the analysis without needing proprietary raw sources.

## References

McKinney, W. (2010). *Data structures for statistical computing in Python*. In S. van der Walt & J. Millman (Eds.), *Proceedings of the 9th Python in Science Conference* (pp. 56–61).

Köster, J., & Rahmann, S. (2012). *Snakemake—A scalable bioinformatics workflow engine*. Bioinformatics, 28(19), 2520–2522. https://doi.org/10.1093/bioinformatics/bts480

Python Software Foundation. (2023). *Python: A dynamic, open source programming language*. https://www.python.org/

Preda, G. (2022). *WallStreetBets 2022* [Data set]. Kaggle. https://www.kaggle.com/datasets/gpreda/wallstreetbets-2022

Federal Reserve Bank of St. Louis. (2023). *S&P 500 (SP500)* [Data set]. FRED, Federal Reserve Bank of St. Louis. https://fred.stlouisfed.org/series/SP500

