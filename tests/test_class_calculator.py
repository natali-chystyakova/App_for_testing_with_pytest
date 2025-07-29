from src.files_for_testing.class_calculator import Calculator
import pytest
from contextlib import nullcontext as does_not_raise

class TestCalculator:
    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, '-1', -5, pytest.raises(TypeError)),
            (5, 0, 4, pytest.raises(ZeroDivisionError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y)==res


    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (5, "-1", 4, pytest.raises(TypeError)),

        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y)==res


#вызов конкретного теста(если не класс)
# pytest tests/test_class_calculator.py::test_add
#  pytest tests/test_class_calculator.py::test_add[1-2-3]

#запуск тестов всего класса TestCalculator
#pytest tests/test_class_calculator.py::TestCalculator
#pytest tests/test_class_calculator.py::TestCalculator::test_divide

#https://github.com/artemonsh/pytest_course/tree/master/src/alembic