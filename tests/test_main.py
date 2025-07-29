from src.files_for_testing.main_for_test import A
import logging
from my_logging.loggers import get_core_logger
from my_logging.init_logging import init_logging

def test_main():
    assert A.x==1

def test_2():
    assert 2==2

def test_sum():
    init_logging(is_verbose=True)
    logger = get_core_logger()
    logger.info("Начинается тест test_sum")
    x=1
    y=2
    assert x+y == 3

def test_div():
    x=1
    y=2
    assert x/y == 0.5