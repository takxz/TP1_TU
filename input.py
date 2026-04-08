
from code_binaire import CodeBinaire, Bit

class Input:
    def __init__(self, value: str):
        self.value = value

    def input_to_code_binaire(self):

        self.value = input("Entrez une une chaine de caractères composée uniquement de '0' et '1' : ")
        bits = []
        for c in self.value:
            if c == '0':
                bits.append(Bit.BIT_0)
            elif c == '1':
                bits.append(Bit.BIT_1)
            else:
                raise ValueError("La valeur d'entrée doit être une chaîne de caractères composée uniquement de '0' et '1'.")
        return CodeBinaire(*bits)


if __name__ == "__main__":
    input_instance = Input("")
    code_binaire = input_instance.input_to_code_binaire()
    print(code_binaire)