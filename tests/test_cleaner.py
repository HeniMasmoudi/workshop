"""
testing ML script 
"""

from os.path import dirname, abspath
import pytest
import numpy as np
from staging import cleaning

features = ["stockcode", "quantity", "invoicedate", "unitprice", "country"]


@pytest.fixture(name="workshop_dir", scope="session")
def fixture_xmi_home():
    folder_name = dirname(dirname(abspath(__file__)))
    return folder_name


@pytest.fixture(name="data", scope="module")
def fixture_select_columns(workshop_dir):
    data = cleaning.selectfeatures(workshop_dir)
    return data


@pytest.fixture(name="selected_features", scope="module")
def fixture_get_features(data):
    features = list(data.columns)
    return features


@pytest.fixture(name="lower_columns", scope="module")
def fixture_lower_columns(data):
    data = cleaning.lowername(data)
    lower_columns = list(data.columns)
    return lower_columns


def test_check_columns(selected_features):
    assert len(selected_features) == 5, (
        "error in loading columns"
        f"expecting 5 columns got {len(selected_features)} columns instead."
    )
    assert len(selected_features) == len(np.unique(selected_features)), (
        "error in creating columns" f"redendant columns {selected_features}"
    )


@pytest.mark.parametrize("feature", features)
def test_lower(feature, lower_columns):
    assert feature in lower_columns, f"{feature} is not found in the features set"


def test_datetime(data):
    data = cleaning.lowername(data)
    data = cleaning.parse_datetime(data)
    assert data.invoicedate.dtype == "datetime64[ns]", "problem in parsing datetime"
    assert data.invoicedate.shape[0] == 541909, (
        "error in creating datetime",
        f"expecting 541909 instance but got {data.invoicedate.shape[0]} instead",
    )
