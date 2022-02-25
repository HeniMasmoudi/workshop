import os
import pandas as pd
import numpy as np
from datetime import datetime
from staging import cleaning

workshop_home = os.environ.get("workshop")


def create_doy(home):
    data = cleaning.main(home)
    data["doy"] = data.invoicedate.dt.dayofyear.astype(np.int32)
    return data


if __name__ == "__main__":
    data = create_doy(workshop_home)
