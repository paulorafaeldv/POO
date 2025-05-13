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

class ContaBancaria():
    def __init__ (self, numero, nome, tipo):
        self.numero = numero
        self.n = nome
        self.tipo = tipo
        self.saldo = 0
        self.status = False
        self.limite = 0

    def ativar(self):
        if self.status == False:
            print ("Conta ativada! ")
            self.status = True
        else:
            print ("A conta já está ativada.")

    def depositar(self, deposito):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        else:
            print(f"valor depositado: {deposito}")
            self.saldo += deposito


    def sacar(self, saque):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        elif (self.saldo + self.limite) < saque:
            print(f"Saque indisponível. Valor disponível: {self.saldo}")
        else:
            print (f"{self.n} sacou {saque} reais")
            self.saldo -= saque

    def consulta(self):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        else:
            print (f"Seu saldo é {self.saldo}")

    def criarLimite(self, novolimite):
        if self.status == False:
            print ("Necessário ativar a conta! ")
        else:
            self.limite += novolimite
            print (f"Seu novo limite é {self.limite}")

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print (f"O {self.nome} foi miando")

    def vomitarPelo(self):
        print (f"O {self.nome} ta vomitando bola de pelo")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer capim")

    def mugir(self):
        print(f"A {self.nome} muge")

class Coelhinho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print (f"O {self.nome} pulou")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print (f"O {self.nome} latiu")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print (f"R${self.valor}")


class ingressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        self.area = base * altura
        print (f"A área é {self.area}")

    def calculaPerimetro(self, base, altura):
        self.perimetro = 2 * (base * altura)
        print(f"O perímetro é {self.perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        self.area = (base * altura) / 2
        print(f"A área é {self.area}")

    def calculaPerimetro(self, lado1, lado2, lado3):
        self.area = lado1 + lado2 + lado3
        print(f"O perímetro é {self.area}")











