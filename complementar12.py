class Mamifero:

    quantidade = 0
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def objetos(self):
        Mamifero.quantidade += 1



cachorro = Mamifero("Jack", 4, "Pastor")
gato = Mamifero("Vivi", 2, "Viralata")
macaco = Mamifero("Flor", 5, "Mico")
girafa = Mamifero("Bel", 1, "Masai")

cachorro.objetos()
gato.objetos()
macaco.objetos()
girafa.objetos()

print(Mamifero.quantidade)
