class Cachorro:

    quantidade = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def setNome(self, name):
        self.nome = name

    def getIdade(self):
        return self.idade

    def setIdade(self, age):
        self.idade = age


Dog = Cachorro("Jack", 4)
print(Dog.nome, Dog.idade)
Dog.setNome("Pablo")
Dog.setIdade(6)
print(Dog.nome, Dog.idade)
