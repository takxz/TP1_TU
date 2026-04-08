from enum import Enum

class Bit(Enum):
    BIT_0 = 0
    BIT_1 = 1

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Bit.{self.name}"

class AuMoinsUnBitErreur(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CodeBinaire:
    def __init__(self, bit, *bits):
        self.bits = [bit] + list(bits)

    def __repr__(self):
        return f"CodeBinaire({', '.join(repr(bit) for bit in self.bits)})"

    def ajouter(self, bit):
        if not isinstance(bit, Bit):
            raise TypeError("Le bit ajoute doit etre de type Bit")
        self.bits.append(bit)

    @property
    def chaine(self):
        return ''.join(str(bit) for bit in self.bits)


    def __len__(self):
        return len(self.bits)
    
    def __add__(self, code2):
        new_list = self.bits + code2.bits
        return CodeBinaire(*new_list)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return CodeBinaire(*self.bits[index])
        return self.bits[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self.bits[index] = value.bits
        self.bits[index] = value
    
    def __delitem__(self, index):
        if len(self.bits) > 1:
            del self.bits[index]
        else:
            raise AuMoinsUnBitErreur("Le code binaire doit contenir au moins un bit.")

        
    def __iter__(self):
        return iter(self.bits)
    
    def __eq__(self, other):
        if isinstance(other, CodeBinaire):
            return self.bits == other.bits
        return False

#test1



