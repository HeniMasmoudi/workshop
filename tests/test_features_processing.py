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


def test_doy_creation(workshop_dir):
    data = createfeatures.create_doy(workshop_dir)
    assert "doy" in list(data.columns), "problem in creating day of year"
    assert (
        data["doy"].dtype == np.int32
    ), "problem in day of year type, expected np.int32"
    assert data.doy.shape[0] == 541909, "missed rows in doy, expected 541909"
