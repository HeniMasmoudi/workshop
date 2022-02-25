import os
import pandas as pd
from staging.loader import fetch_data

workshop_home = os.environ.get("workshop")


def selectfeatures(home):
    data = fetch_data(home)
    relevant_columns = ["StockCode", "Quantity", "InvoiceDate", "UnitPrice", "Country"]
    cleaned = data[relevant_columns]
    return cleaned


def lowername(data):
    columns = [col.lower() for col in data.columns]
    data.columns = columns
    return data


def parse_datetime(data):
    data.invoicedate = pd.to_datetime(data.invoicedate, infer_datetime_format=True)
    return data


def main(home):
    data = selectfeatures(home)
    data = lowername(data)
    data = parse_datetime(data)
    return data


if __name__ == "__main__":
    data = main(workshop_home)
