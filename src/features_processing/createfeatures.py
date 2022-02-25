import os
import pandas as pd
import numpy as np
from staging import cleaning

workshop_home = os.environ.get("workshop")


def get_cleaned_data(home):
    data = cleaning.main(home)
    return data


def create_doy(data):
    data["doy"] = data.invoicedate.dt.dayofyear.astype(np.int32)
    return data


def create_month_year(data):
    data["year"] = pd.DatetimeIndex(data.invoicedate).year
    data["month"] = pd.DatetimeIndex(data.invoicedate).month
    data["day_of_month"] = pd.DatetimeIndex(data.invoicedate).day
    return data


if __name__ == "__main__":
    data = get_cleaned_data(workshop_home)
    data = create_doy(data)
    data = create_month_year(data)
