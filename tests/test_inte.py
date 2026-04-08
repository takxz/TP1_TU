from code_binaire import Bit
from input import Input
from code_binaire import CodeBinaire
from unittest.mock import Mock, patch

@patch("builtins.input")
def test_input_to_code_binaire(mocker):
    mocker.return_value = "1010"
    input1 = Input("")
    result = input1.input_to_code_binaire()

    assert result == CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)




