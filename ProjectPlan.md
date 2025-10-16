## Overview

This project investigates how public sentiment expressed in financial news and social media relates to movements in the U.S. stock market. Recent studies and real-world events have shown that collective emotions—such as optimism, fear, or uncertainty—can influence short-term trading behavior and market volatility. Understanding this relationship is valuable for investors, analysts, and policymakers who seek to interpret non-traditional data sources as signals of market dynamics.  

The project aims to systematically measure this connection using real-world open datasets and reproducible data workflows.

The goal of this project is to quantify the relationship between daily sentiment and stock market performance, using the S&P 500 index as a benchmark. Sentiment scores will be extracted from financial headlines and social media posts using natural language processing (NLP) techniques such as TextBlob. Stock data will be obtained from the Federal Reserve Economic Data (FRED) API. By aligning and analyzing both datasets over time, the project aims to identify whether sentiment polarity correlates with daily market returns.

Ultimately, this work will demonstrate how open data and reproducible workflows can be combined to explore real-world financial phenomena. The findings may provide evidence of emotional bias in trading patterns and highlight the growing role of data science and machine learning in financial analysis.  


## Research Questions

1. Does public sentiment extracted from financial news or social media correlate with daily changes in the S&P 500 index?  
2. Can sentiment polarity (positive or negative tone) predict short-term stock market direction, such as the next day’s return?  
3. Are days with extreme sentiment—either highly optimistic or pessimistic—associated with higher market volatility or trading volume?

## Team
- **Yunxiang Wang (Technical Lead — Data Collection & Coding)**  
  Yunxiang is responsible for the technical implementation of the project, including data acquisition from the FRED API, data preprocessing, and integration of sentiment data.  
  He will also develop the Python scripts for text analysis and visualization using libraries such as `pandas`, `matplotlib`, and `TextBlob`.  
  Yunxiang will ensure the workflow is fully reproducible and well-documented on GitHub.

- **Leonard Cao (Analysis Lead — Statistical & Interpretive Analysis)**  
  Leonard will focus on the analytical components of the project, including statistical correlation testing, trend interpretation, and the evaluation of sentiment–market relationships.  
  He will lead the interpretation of results, contribute to writing the analytical sections of the report, and ensure that findings are communicated clearly and supported by evidence.

**Collaboration Approach:**  
Both members will work collaboratively through a shared GitHub repository.  
Yunxiang will maintain the codebase, while Leonard will focus on data interpretation and documentation.  
Regular weekly check-ins will be held to synchronize progress and integrate technical and analytical outputs.


## Datasets

This project uses two open and publicly available datasets to investigate the relationship between financial sentiment and U.S. stock market performance. By integrating text-based sentiment data with quantitative stock market indicators, we aim to identify whether daily sentiment trends correlate with S&P 500 movements.

| Dataset | Source | Format | Description | Access Method |
|----------|---------|----------|--------------|----------------|
| **Sentiment Analysis for Financial News** | Kaggle — [Sentiment Analysis for Financial News](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news) | CSV | Contains more than 4,800 financial news headlines labeled as *positive*, *negative*, or *neutral*. These headlines originate from major financial media outlets and cover various market events. | Downloadable CSV from Kaggle |
| **S&P 500 Index Data** | Federal Reserve Economic Data (FRED) — [SP500](https://fred.stlouisfed.org/series/SP500) | JSON / CSV | Provides daily S&P 500 closing values. The data includes trading date, open, high, low, close, and volume. | Retrieved programmatically via FRED API using `fredapi` or Python `requests` library |

**Integration Plan:**  
1. Load and preprocess the Kaggle dataset in Python (`pandas`).  
2. Compute sentiment polarity and subjectivity scores using **TextBlob** to quantify emotional tone.  
3. Aggregate sentiment scores by publication date.  
4. Retrieve corresponding daily S&P 500 index values from FRED API.  
5. Merge the two datasets on the *date* field, aligning sentiment trends with stock movements.  
6. Handle non-trading days and missing values through forward-filling or interpolation.  

**Data Cleaning & Quality Control:**  
- Remove duplicate or irrelevant headlines (e.g., non-financial topics).  
- Standardize date formats and convert all timestamps to UTC.  
- Normalize sentiment polarity scores to a continuous range of [-1, 1].  
- Ensure API data integrity and handle potential missing trading days.

**Ethical & Legal Notes:**  
Both datasets are publicly accessible and contain no personally identifiable information (PII).  
All data collection complies with Kaggle’s open data license and the FRED API’s terms of use.  
The dataset and analysis scripts will be version-controlled in GitHub for full reproducibility.

## Timeline

The project will run from **Week 8 to Week 16**
Both team members will coordinate through GitHub and weekly meetings.  
**Yunxiang Wang** will lead coding, data acquisition, and reproducibility, while **Leonard Cao** will focus on statistical analysis, interpretation, and reporting.

| Week | Tasks | Responsible Member(s) |
|------|--------|------------------------|
| **Week 8** | Finalize project topic, confirm datasets (Kaggle + FRED), and clearly define research questions. | Both |
| **Week 9** | Download Kaggle dataset and connect to the FRED API for S&P 500 data; verify dataset structure and completeness. | Yunxiang |
| **Week 10** | Clean and preprocess both datasets (remove duplicates, standardize date/time formats, normalize sentiment polarity). | Yunxiang |
| **Week 11** | Integrate sentiment and stock data by date; generate daily sentiment averages and initial exploratory plots. | Yunxiang & Leonard |
| **Week 12** | Perform statistical correlation and regression analysis to test sentiment–market relationships. | Leonard |
| **Week 13** | Evaluate additional indicators such as volatility and trading volume; interpret analytical results. | Leonard |
| **Week 14** | Develop and refine visualizations (trend lines, scatterplots, correlation heatmaps) for the final report and presentation. | Yunxiang |
| **Week 15** | Draft the final report and prepare presentation slides summarizing results, implications, and limitations. | Leonard |
| **Week 16** | Final review, polish GitHub repository for reproducibility, rehearse presentation, and submit final deliverables. | Both |

**Deliverables:**  
- Cleaned and merged dataset (CSV)  
- Python notebooks for preprocessing, analysis, and visualization  
- Final report and presentation slides  
- GitHub repository documenting all code and workflow

## Constraints / Limitations

Several practical and methodological constraints may influence the scope and accuracy of this project:

1. **Data Coverage and Timeliness** –  
   The Kaggle dataset may not fully align with the latest market conditions or trading dates in the FRED S&P 500 data.  
   Differences in data frequency and publication timing could affect correlation accuracy.

2. **Sentiment Analysis Accuracy** –  
   The TextBlob library uses a general-purpose lexicon and may not capture domain-specific financial sentiment as effectively as specialized models such as FinBERT.  
   As a result, polarity scores might not perfectly reflect investor emotions.

3. **Limited Sample Size** –  
   The Kaggle dataset includes roughly 4,800 headlines, which may limit statistical power when aggregating by day.



---

## Gaps / Future Work

This project serves as an initial exploration of the relationship between financial sentiment and market behavior.  
Future improvements and extensions may include:



1. **Expanding Data Sources** –  
   Include additional financial text datasets (e.g., Twitter, Reddit’s r/WallStreetBets, or real-time news feeds) to capture broader investor sentiment.

2. **Interactive Visualization Dashboard** –  
   Build an interactive dashboard (using Plotly or Dash) to visualize the sentiment–market relationship dynamically.