from pathlib import Path
import sys
import json
from datetime import datetime, timezone
import logging

ROOT = Path (__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv, write_parquet
from bootcamp_data.transforms import enforce_schema

def main():
    paths = make_paths(ROOT)
    orders = read_orders_csv(paths.raw / "orders.csv")
    orders = enforce_schema(orders)
    output_path = paths.processed / "orders.parquet"
    write_parquet(orders, output_path)

if __name__ == "__main__":
    main()