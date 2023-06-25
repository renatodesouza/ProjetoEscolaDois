class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso

p = Pessoa(nome='renato', peso=80, idade=39)
print(p.nome)