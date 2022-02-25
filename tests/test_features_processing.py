"""
testing features processing 

"""

from os.path import dirname, abspath
import pytest
import numpy as np
from features_processing import createfeatures


@pytest.fixture(name="workshop_dir", scope="session")
def fixture_xmi_home():
    folder_name = dirname(dirname(abspath(__file__)))
    return folder_name


@pytest.fixture(name="data", scope="module")
def fixture_select_columns(workshop_dir):
    data = createfeatures.get_cleaned_data(workshop_dir)
    return data


def test_doy_creation(data):
    data_with_doy = createfeatures.create_doy(data)
    assert "doy" in list(data_with_doy.columns), "problem in creating day of year"
    assert (
        data_with_doy["doy"].dtype == np.int32
    ), "problem in day of year type, expected np.int32"
    assert data.doy.shape[0] == 541909, "missed rows in doy, expected 541909"


def test_mdy_creation(data):
    data_with_doy = createfeatures.create_doy(data)
    data_with_mdy = createfeatures.create_month_year(data_with_doy)
    assert "year" in data_with_mdy.columns, "year is not found in processed data"
    assert "month" in data_with_mdy.columns, "month is not found in processed data"
    assert (
        "day_of_month" in data_with_mdy.columns
    ), "day of month is not found in processed data"
