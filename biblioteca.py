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
        self.limite += novolimite
        print (f"Seu novo limite é {self.limite}")






