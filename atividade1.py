from biblioteca import Pessoa

aluno01 = Pessoa(83, "paulo", 26)
aluno02 = Pessoa(50, "ana clara", 19)
aluno03 = Pessoa(78, "wesley", 23)
aluno04 = Pessoa(56, "joalisson", 19)
aluno05 = Pessoa(87, "gabriel", 20)
aluno06 = Pessoa(64, "fabricio", 19)


print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso}kg")
print(aluno02.nome)
aluno03.comer("Caju")
aluno03.comer("empada")
aluno03.parardecomer()
aluno03.comer("broa")
aluno03.parardecomer()
aluno03.parardecomer()