import pytest
from app.calc import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_negative(self):
        assert self.calc.adding(self, 1, -3) == -2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 2, 2) != 3

    # def test_adding_unsuccess_no(self):
    #     with pytest.raises(ArithmeticError):
    #         self.calc.adding(self, 2, 2) != 4

    def test_subtraction_negative(self):
        assert self.calc.subtraction(self, 3,5) == -2

    def test_subtraction_positive(self):
        assert self.calc.subtraction(self, 5,3) == 2

    def test_division_int(self):
        assert self.calc.subtraction(self, 6,3) == 3


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_positive(self):
        assert self.calc.multiply(self, 5,3) == 15

    def test_multiply_float(self):
        assert self.calc.multiply(self, 5.5,3.0) == 16.5

    def test_multiply_negative(self):
        assert self.calc.multiply(self, 5, -3) == -15


    def test_multiply_zero(self):
        assert self.calc.multiply(self, 1, 0) == 0


    def teardown(self):
        print('Выполнение метода Teardoun')

