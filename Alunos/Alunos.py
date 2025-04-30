
class Alunos:
    def __init__(self,nome="Desonhecido",idade="00",curso="Não defenido",numerodematricula="0000"):
        self.nome=nome
        self.idade=idade
        self.curso=curso
        self.matricula=numerodematricula

    def exibir_caracteristicas(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")
        print(f"Matricula: {self.matricula}")
