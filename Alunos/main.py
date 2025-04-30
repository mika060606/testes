from platform import system

from Alunos import Alunos

alunos= []
while True:
    print("Menu:")
    print("1- criar aluno\n2- ver alunos\n3- sair")
    escolha= int(input("->"))

    if escolha==1:
        nome=str(input("Qual o nome ->"))
        idade=int(input("Qual a idade ->"))
        curso=str(input("Qual o curso ->"))
        matricula=int(input("Qual a matricula ->"))
        aluno=Alunos(nome,idade,curso,matricula)
        alunos.append(aluno)
    elif escolha==2:
        if not alunos:
            print("nenhum aluno ainda")
            continue
        else:
            print("Alunos:")
            for i,aluno in enumerate(alunos):
                print(f"{i}- {aluno.nome}")
            esc=int(input("Escolha o numero ->"))
            if 0<=esc < len(alunos):
                alunos[esc].exibir_caracteristicas()
                a=input()
            else:
                print("Não tem esse valor")

    elif escolha== 3:
        print("Ate a proxima")
        break

    else:
        print("opção invalida.")




