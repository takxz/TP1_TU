from code_binaire import Bit, CodeBinaire, AuMoinsUnBitErreur
from pytest import raises

#2 et 
def test_ajouter_bit():
    code = CodeBinaire(Bit.BIT_0)
    code.ajouter(Bit.BIT_1)
    assert code.bits == [Bit.BIT_0, Bit.BIT_1]
    assert len(code) == 2
    assert code.bits[len(code) - 1] == Bit.BIT_1
    
def test_ajouter_bit_non_valide():
    code = CodeBinaire(Bit.BIT_0)
    with raises(TypeError):
        code.ajouter(2) 

#7
def test_len():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
    assert len(code) == 3

#7
def test_concatener():
    code1 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    code2 = CodeBinaire(Bit.BIT_1, Bit.BIT_0)
    code_concatene = code1 + code2
    assert code_concatene.bits == [Bit.BIT_0, Bit.BIT_1, Bit.BIT_1, Bit.BIT_0]
    assert len(code_concatene) == 4

#3
def test_get_item_slice():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
    sliced_code = code[1:3]
    assert sliced_code.bits == [Bit.BIT_1, Bit.BIT_0]
    assert len(sliced_code) == 2
#3
def test_get_item_index():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
    assert code[0] == Bit.BIT_0
    assert code[1] == Bit.BIT_1
    assert code[2] == Bit.BIT_0

#4
def test_set_item_index():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
    code[1] = Bit.BIT_0
    assert code.bits == [Bit.BIT_0, Bit.BIT_0, Bit.BIT_0]
#4
def test_set_item_slice():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
    code[1:3] = CodeBinaire(Bit.BIT_0, Bit.BIT_0)
    assert code.bits == [Bit.BIT_0, Bit.BIT_0, Bit.BIT_0, Bit.BIT_1]

#5
def test_del_index():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    del code[1]
    assert code.bits == CodeBinaire(Bit.BIT_0).bits

#5
def test_del_slice():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
    del code[1:3]
    assert code.bits == [Bit.BIT_0, Bit.BIT_1]

def test_del_last_bit():
    code = CodeBinaire(Bit.BIT_0)
    with raises(AuMoinsUnBitErreur):
        del code[0]

def test_iter():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)
    bits = iter(code)
    assert list(bits) == [Bit.BIT_0, Bit.BIT_1, Bit.BIT_0]

#1 
def test_eq():
    code1 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    code2 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    code3 = CodeBinaire(Bit.BIT_1, Bit.BIT_0)
    assert code1 == code2
    assert code1 != code3


#8

def test_representation_formelle():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    assert repr(code) == "CodeBinaire(Bit.BIT_0, Bit.BIT_1)"

#9

def test_representation_informelle():
    code = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    assert code.chaine == "01"
