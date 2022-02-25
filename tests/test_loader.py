"""
testing ML script 
"""

from os.path import dirname, abspath
import pytest
from staging import loader


@pytest.fixture(name="workshop", scope="session")
def fixture_xmi_home():
    folder_name = dirname(dirname(abspath(__file__)))
    return folder_name


def test_loader(workshop):
    data = loader.fetch_data(workshop)
    columns = data.columns
    assert len(columns) == 8, "error in loading data"
