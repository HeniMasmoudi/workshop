"""
testing ML script 
"""

from os.path import dirname, abspath
import pytest
from staging import loader


@pytest.fixture(name="workshop_dir", scope="session")
def fixture_xmi_home():
    folder_name = dirname(dirname(abspath(__file__)))
    return folder_name

@pytest.fixture(name="loaded_data", scope="module")
def fixture_load_data(workshop_dir):
    """Load data using staging/loader module """
    data = loader.fetch_data(workshop_dir)
    return data

def test_check_columns(loaded_data):
    columns = loaded_data.columns
    assert len(columns) == 8, (
            "error in loading columns"
            f"expecting 8 columns got {len(columns)} columns instead."
        )
def test_check_rows(loaded_data):
    assert len(loaded_data) == 541909, (
            "error in loading rows"
            f"expecting 541909 columns got {len(loaded_data)} rows instead."
        )
