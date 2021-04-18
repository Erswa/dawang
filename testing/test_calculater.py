import  sys

import pytest
import yaml

sys.path.append("..")
from pytestcode.Calculator import Calculator

def get_datas():
    with open("./calc.yml") as f :
        datas = yaml.safe_load(f)
    return  datas['add']['datas']
@classmethod
class TestCalc:
    def test_add(self):
        # calc = Calculator
        self.calc = Calculator()
        # assert 2 == calc.add(1,1,1)
    @pytest.mark.parametrize("a,b,result",get_datas())
    def test_add1(self,a,b,result ):
        # calc = Calculator
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a,b)