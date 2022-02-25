import os
import zipfile
import pandas as pd

workshop_home = os.environ.get("workshop")


def fetch_data(home):
    """
    Description
    ----------
    read data from zip file

    Parameters
    ----------
    home: data home directory

    Returns
    -------
    data : pandas dataframe
        retail data (8 columns, 541909 rows, mixed types)

    """

    # specifying the zip file name
    folder = os.path.join(home, "retail_data.zip")
    # opening the zip file in READ mode
    with zipfile.ZipFile(folder) as zip:
        with zip.open("Online_Retail.csv") as myZip:
            data = pd.read_csv(myZip, encoding="unicode_escape")
    return data
