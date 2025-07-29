import pytest
from my_logging.init_logging import init_logging

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    init_logging(is_verbose=True)