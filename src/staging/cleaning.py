import os
from staging.loader import fetch_data

workshop_home = os.environ.get("workshop")


def selectfeatures(home):
    data = fetch_data(home)
    relevant_columns = [ "StockCode", "Quantity", "InvoiceDate","UnitPrice","Country"]
    cleaned = data[relevant_columns]
    return cleaned


def lowername(data):
    columns = [col.lower() for col in data.columns] 
    data.columns = columns 
    return data  


def main(home):
    data = selectfeatures(home) 
    data = lowername(data)
    return data 

if __name__ == "__main__":
    data = main(workshop_home)








