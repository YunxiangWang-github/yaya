## Repository Artifact Map

### data/
- **sp500_raw.csv**  
  Raw S&P 500 index data downloaded before cleaning.

- **sp500_clean.csv**  
  Cleaned and standardized S&P 500 data with consistent date formats and no missing values.

- **wsb_daily_sentiment.csv**  
  Daily aggregated sentiment data computed from the wallstreetbets-2022 Reddit dataset.

- **merged_sp500_wsb.csv**  
  Final merged dataset combining S&P 500 daily data with WSB daily sentiment and sentiment MA7.

### notebooks/
- **clean_sp500.ipynb**  
  Notebook for cleaning the S&P 500 dataset (sorting dates, removing duplicates, handling missing values).

- **clean_wsb.ipynb**  
  Notebook for processing the WSB dataset, computing sentiment scores, and aggregating them to daily level.

- **merge_data.ipynb**  
  Notebook for merging the cleaned S&P 500 data with the daily sentiment data and generating exploratory visualizations.

- **analysis_sentiment_stock.ipynb**  
  Notebook for Week 12 tasks: creating daily return variable, running correlation analysis, performing OLS regression, and generating scatter/regression plots.

### scripts/
- **download_sp500.py**  
  Script for downloading S&P 500 data from external sources using fredapikey.

## Updated Timeline (Progress Status as of Week 12)

The project is scheduled to run from **Week 8 to Week 16**.  
This updated timeline reflects the current progress, completed tasks, and expected completion dates for remaining work.

| Week | Tasks | Status | Expected / Actual Completion | Responsible Member(s) |
|------|--------|---------|-------------------------------|------------------------|
| **Week 8** | Finalize project topic, confirm datasets (Kaggle + FRED), and define research questions. | Completed | Week 8 | Both |
| **Week 9** | Download datasets, inspect structure, validate completeness. | Completed | Week 9 | Yunxiang |
| **Week 10** | Clean and preprocess datasets (date cleaning, sentiment extraction, CSV generation). | Completed with one revision (dataset replacement due to missing timestamps). | Week 10 | Yunxiang |
| **Week 11** | Merge datasets, create moving average sentiment, and produce initial exploratory visualizations. | Completed | Week 11 | Yunxiang & Leonard |
| **Week 12** | Conduct correlation and regression analysis (daily return vs sentiment). | Completed | Week 12 | Leonard |
| **Week 13** | Evaluate additional indicators such as volatility and trading volume; interpret analytical results. | Not started | Expected Week 13–14 | Leonard |
| **Week 14** | Develop final visualizations (trend lines, scatterplots, heatmaps) for final report and presentation. | Not started | Expected Week 14 | Yunxiang |
| **Week 15** | Draft final written report; prepare presentation slides. | Not started | Expected Week 15 | Leonard |
| **Week 16** | Final review, repository polishing, reproducibility check, rehearsal, and submission. | Not started | Expected Week 16 | Both |

## Changes to the Project Plan

Several adjustments were made to the original project plan based on data constraints discovered during implementation and feedback from Milestone 2.

### 1. Replacement of the Sentiment Dataset
The initial plan proposed using a financial-news–based sentiment dataset. However, during Week 10, we discovered that the dataset lacked reliable timestamp information, which made it impossible to align sentiment events with daily S&P 500 returns.  
To resolve this, we replaced it with the **wallstreetbets-2022** dataset from Kaggle:  
https://www.kaggle.com/datasets/gpreda/wallstreetbets-2022  
which provides Reddit posts with precise timestamps and sufficient volume for daily aggregation.


**Impact on the project:**  
- Cleaning workflow had to be adjusted but was completed within the same week.  
- No changes to the research questions were needed.  
- Subsequent tasks (merging, analysis) remained on schedule.

### 2. Adjustment to Preprocessing Workflow
Due to the dataset replacement, we added a sentiment–aggregation step to generate **daily sentiment scores** and a **7-day moving average** (`sentiment_ma7`).  
This step was not included in the original plan but became necessary for smoothing highly noisy Reddit sentiment data.

### 3. Team Member Contributions

### Leonard Cao
In this milestone, I completed all analytical tasks for Week 12, including creating the daily return variable, running correlation and regression analysis, generating visualizations, and interpreting the statistical results. I authored the `analysis_sentiment_stock.ipynb` notebook and helped verify the merged dataset used for modeling.

### Yunxiang Wang
Yunxiang completed the data acquisition and preprocessing tasks in Weeks 9–11, including cleaning the S&P 500 dataset, processing the wallstreetbets-2022 dataset, aggregating daily sentiment scores, and generating the initial merged dataset and exploratory visualizations.


### 4. No Change to the Overall Timeline
Despite the dataset switch and workflow adjustments, all tasks through Week 12 were completed on time.  
Future tasks (Weeks 13–16) are still feasible within the original timeline.

