
'''Curso: Informática
Turma: 2A matutino
Disciplina: Programação Orientada a Objetos
Integrantes do Grupo: Mirian Menezes, Ashlley Kimberlly, Franciele Kamily, Kerlon Ryan e Evanilson Pinheiro
Grupo Gestão Eventos
'''

from usuarios import AlunoRepresentante
from rifa import Rifa
from evento import Evento
from local import Local
from conta import Conta

#ADICIONADO
from TipodeUser import TipoUsuarioInvalidoException
from ErroLogin import LoginInvalidoException

import time

# Armazenar os usuários cadastrados
usuarios_cadastrados = []


# cadastrar user
def cadastrar_usuario():
    try:
        print()
        time.sleep(0.5)
        print("Precisamos saber qual seu perfil para cadastro...")
        time.sleep(1)

        tipo_usuario = int(input('''Digite o tipo de usuário.
1 - Aluno Representante 
Insira o número correspondente: '''))
        print()
        if tipo_usuario == 1:
            nome = input("Digite o nome de usuário: ").strip()
            #ADICIONADO
            if not nome:
                 raise ValueError("O nome do usuário não pode estar vazio.")
            senha = input("Digite a senha: ").strip()
            #ADICIONADO
            if len(senha) < 6:
                 raise ValueError("A senha deve ter no mínimo 6 caracteres.")
            cpf = input("Digite o CPF: ").strip()
            #ADICIONADO
            if not cpf:
                 raise ValueError("O CPF exige a inserção de 11 caracteres.")
            email = input("Digite o email: ").strip()
            turma = input("Digite a turma: ").strip()
            usuario = AlunoRepresentante(nome, senha, cpf, email, turma)
            
        else:
            raise TipoUsuarioInvalidoException("Tipo de usuário inválido, por favor escolha um tipo de usuário existente.")
           
         
        usuarios_cadastrados.append(usuario)
        time.sleep(2)
        print()
        print(f"Usuário {nome} cadastrado com sucesso.")
    #correção para ValueErro caso seja vazio
    except ValueError as e:
        print()
        print(f"\033[1;31mErro: {e} \033[m")
        
def fazer_login():
    print()
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    usuario_encontrado = None
    for usuario in usuarios_cadastrados:
        if usuario.mostrar_nome() == nome and usuario.validar_senha(senha):
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print("Login bem-sucedido!")
        print(usuario_encontrado.exibirInfo())

    else:
        raise LoginInvalidoException(f"Usuário {nome} não encontrado, verifique suas credenciais")
        


def menu():
    while True:
        
            print("\n\033[1;35m1. Cadastrar Usuário")
            print("\n2. Fazer Login")
            print("\n3. Acessar Instâncias ")
            print("\n4. Sair\033[m")

            opcao = input("\n\033[1;35mEscolha uma opção: \033[m").strip()

            if opcao == "1":
               cadastrar_usuario()
            
            elif opcao == "2":
               fazer_login()
            
            elif opcao == "4":
               print("Saindo...")
               time.sleep(1)
               break

            elif opcao == "3":
               print()
        
               print("Carregando instâncias em:")
               for tempo in range(1, 4):
                  print(tempo, "s")
                  time.sleep(1)
               print("Processando...")
               time.sleep(3)
            

               print("\033[1;31mInstâncias de Alunos Representantes:\033[m ")
               # instancias alunos
               aluno1 = AlunoRepresentante("Ester","ester123","123.456.789-00","ester.ifro@hotgmail.com","2A informática")
               aluno2 = AlunoRepresentante("Thiago","Thiago456","987.654.321-11","Thiago.ifro@hotgmail.com","2A Informática")
               aluno3 = AlunoRepresentante("Davi","Davi123","123.456.789-00","Davi.ifro@hotgmail.com","2A Informática")

               print(aluno1.exibirInfo())
               print(aluno2.exibirInfo())
               print(aluno3.exibirInfo())


               #instância rifa
               print("\033[1;31mInstância Rifa:\033[m ")
               rifa1 = Rifa("Iphone 14 ProMax", 500, 15)
               print(rifa1.exibirRifa())
               print("")

               # instâncias local
               print("\033[1;31mInstância Local:\033[m ")
               local1 = Local("Av Calama", "Agenor de Carvalho", "Porto Velho", 500)
            
               print(f"Local 1: {local1.ExibirLocal()}")
               print("")
               local2 = Local("Rua das estrelas", "Centro", "Manaus", 1000)
               print(f"Local 2: {local2.ExibirLocal()}")
               print("")

               #instância banco
               print("\033[1;31mInstância Banco:\033[m ")
               banco1 = Conta("Inter", "290.830.990", "78.90.934", "thiago.mendes@gmail.com", "0", "2500" )
               print(banco1.exibirChave())

               print("")

               #instância evento
               print("\033[1;31mInstância Evento:\033[m ")
               evento1 = Evento("Semana da Vida", "15/11/24", local1, "16:00", "22:00" )
               print(evento1.detalhes())
               print("")

               evento2 = Evento("Norte Show", "22/12/24", local2, "11:00", "18:00")
               print(evento2.detalhes())
               time.sleep(6)

            else:
                 print("Essa opção não existe. Tente novamente")
                 print("")

        
menu()
# fim do fim