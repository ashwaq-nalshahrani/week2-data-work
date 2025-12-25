## Week 2 Project: Data Pipeline (ETL) and Analysis (EDA)
This project implements a complete data pipeline that cleans raw order and user data, joins them into an analytics-ready table, and performs exploratory data analysis.

#### 🛠️ 1. Environment Setup
Follow these steps to prepare the environment and install necessary dependencies.

Create Virtual Environment:
python -m venv .venv

Activate Virtual Environment

Windows (PowerShell):
.venv\Scripts\activate

macOS / Linux:
source .venv/bin/activate

Install Dependencies
uv pip install -r requirements.txt

#### ⚙️ 2. Run ETL Process
Execute the ETL script to process raw data and generate the analytics tables. This script handles schema enforcement, datetime parsing, and outlier detection.

Windows (PowerShell):
$env:PYTHONPATH="src"
python scripts/run_etl.py


macOS / Linux:
PYTHONPATH=src python scripts/run_etl.py

#### 📊 3. Generated Outputs
Once the ETL script completes, the following files will be generated in the data/processed/ directory:
orders_clean.parquet: Cleaned and validated orders data.
users.parquet: Processed users data.
analytics_table.parquet: The final table used for analysis.
_run_meta.json: Metadata summary of the ETL execution (row counts, match rates, etc.).

#### 4. Exploratory Data Analysis (EDA)
To view the analysis results and generated visualizations:
Ensure the ETL process has been completed successfully.
Open the Jupyter notebook located at notebooks/eda.ipynb.
Select the project's virtual environment (.venv) as your kernel.
Run all cells to generate plots and view the data audit.

#### 📝 5. Project Summary
Key Findings
Data Integrity: Successfully joined orders and users with a high match rate.
Data Quality: Handled missing values in critical columns and flagged outliers in the amount field using winsorization.
Schema: Enforced strict data types for analytics consistency.