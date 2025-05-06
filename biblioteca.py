class Pessoa():
    def __init__(self, peso, nome, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida):
        if self.comendo == True:
            print (f"{self.nome} já está comendo")
        elif self.falando == True:
            print (f"{self.nome} já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} foi comer {comida}")
            self.comendo = True
    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} já está comendo")
        elif self.falando == True:
            print(f"{self.nome} já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        else:
            print (f"{self.nome} hablou")
            self.falando = True

    def dormir(self):
        if self.comendo == True:
            print(f"{self.nome} já está comendo")
        elif self.falando == True:
            print(f"{self.nome} já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        else:
            print (f"{self.nome} dormiu")
            self.dormindo = True
    def parardecomer(self):
        if self.comendo == True:
            print("acabou de comer")
            self.comendo = False
        else:
            print("ele não está comendo.")

    def calaboca(self):
        if self.falando == True:
            print("acabou de falar")
            self.falando = False
        else:
            print("ele não está falando.")

    def acordar(self):
        if self.dormindo == True:
            print("acordou")
            self.falando = False
        else:
            print("ele não está dormindo.")







