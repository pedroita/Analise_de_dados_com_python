class Pessoa:
    def __init__(self,name:str, idade : int) -> None:
        self.name = name
        self.idade = idade
    def dirigir(self,veiculo: str)-> None:
        print ('Dirigindo uma (a) {}'.format(veiculo ))
    def cantar(self):
        print("alalalalala")
    def apresentar_idade(self):
        return self.idade