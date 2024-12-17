'''Curso: Informática
Turma: 2A matutino
Disciplina: Programação Orientada a Objetos
Integrantes do Grupo: Mirian Menezes, Ashlley Kimberlly, Franciele Kamily, Kerlon Ryan e Evanilson Pinheiro
Grupo Gestão Eventos'''

from usuarios import AlunoRepresentante
from rifa import Rifa
from evento import Evento
from local import Local
from conta import Conta
from Visitante import Visitante

import time
import os

#Função para limpar a tela
def limpar_tela():
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

#Armazenar os usuários cadastrados
usuarios_cadastrados = []

#Cadastrar usuário
def cadastrar_usuario():
    print()
    time.sleep(0.5)
    print("Precisamos saber qual seu perfil para cadastro...")
    time.sleep(1)

    try:
        tipo_usuario = int(input('''Digite o tipo de usuário.
1 - Aluno Representante
Insira o número correspondente: '''))
        print()

        nome = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()
        cpf = input("Digite o CPF: ").strip()
        email = input("Digite o email: ").strip()

        if tipo_usuario == 1:
            turma = input("Digite a turma: ").strip()
            usuario = AlunoRepresentante(nome, senha, cpf, email, turma)
        else:
            print("Tipo de usuário inválido.")
            return

        usuarios_cadastrados.append(usuario)
        time.sleep(2)
        limpar_tela()
        print(f"Usuário {nome} cadastrado com sucesso.")
    except ValueError:
        print("Erro: Por favor, insira um número válido para o tipo de usuário.")
        time.sleep(2)

#Fazer login
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
        print(usuario_encontrado.exibir_info())
    else:
        print("Usuário não encontrado. Verifique suas credenciais.")
        print('''\033[1;31;3mCaso não tenha realizado seu cadastro, não será possível realizar seu login!\033[m''')

#carregar as instâncias
def carregar_instancias():
    print("\033[1;31mInstâncias de Alunos Representantes:\033[m ")
    #instâncias alunos
    aluno1 = AlunoRepresentante("Ester", "ester123", "123.456.789-00", "ester.ifro@hotgmail.com", "2A informática")
    aluno2 = AlunoRepresentante("Thiago", "Thiago456", "987.654.321-11", "Thiago.ifro@hotgmail.com", "2A Informática")
    aluno3 = AlunoRepresentante("Davi", "Davi123", "123.456.789-00", "Davi.ifro@hotgmail.com", "2A Informática")

    print(aluno1.exibir_info())
    print(aluno2.exibir_info())
    print(aluno3.exibir_info())

    #instância rifa
    print("\033[1;31mInstância Rifa:\033[m ")
    rifa1 = Rifa("Iphone 14 ProMax", 500, 15)
    print(rifa1.exibirRifa())

    #instâncias local
    print("\033[1;31mInstância Local:\033[m ")
    local1 = Local("Av Calama", "Agenor de Carvalho", "Porto Velho", 500)
    print(local1.ExibirLocal())

    local2 = Local("Rua das estrelas", "Centro", "Manaus", 1000)
    print(local2.ExibirLocal())

    #instância banco
    print("\033[1;31mInstância Banco:\033[m ")
    banco1 = Conta("Inter", "290.830.990", "78.90.934", "thiago.mendes@gmail.com", 0, 2500)
    print(banco1.exibirChave())

    #instância evento
    print("\033[1;31mInstância Evento:\033[m ")
    evento1 = Evento("Semana da Vida", "15/11/24", local1, "16:00", "22:00")
    print(evento1.detalhes())

    evento2 = Evento("Norte Show", "22/12/24", local2, "11:00", "18:00")
    print(evento2.detalhes())
    time.sleep(6)

#Menu
def menu():
    while True:
        limpar_tela()
        print("\033[1;35m1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Acessar Instâncias ")
        print("4. Sair\033[m")

        try:
            opcao = input("\n\033[1;35mEscolha uma opção: \033[m").strip()

            if opcao == "1":
                limpar_tela()
                cadastrar_usuario()
            elif opcao == "2":
                fazer_login()
            elif opcao == "3":
                carregar_instancias()
            elif opcao == "4":
                print("Saindo...")
                time.sleep(1)
                limpar_tela()
                break
            else:
                print("Essa opção não existe. Tente novamente.")
                time.sleep(1)
        except ValueError:
            print("Opção inválida. Por favor, insira um número válido.")
            time.sleep(1)

menu()