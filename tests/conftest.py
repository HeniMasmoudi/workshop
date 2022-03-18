import pytest

@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    # setup
    yield
    # teardown - put your command here