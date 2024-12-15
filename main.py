# Curso: Informática
# Turma: 2A matutino
# Disciplina: Programação Orientada a Objetos
# Integrantes do Grupo: Mirian Menezes, Ashlley Kimberlly, Franciele Kamily, Kerlon Ryan e Evanilson Pinheiro
# Grupo Gestão Eventos

from usuarios import AlunoRepresentante
from rifa import Rifa
from evento import Evento
from local import Local
from conta import Conta
from Visitante import Visitante

import time
import os

# Armazenar os usuários cadastrados
usuarios_cadastrados = []

# Exceção personalizada para usuários inválidos
class UsuarioInvalidoError(Exception):
    pass

# Função para limpar a tela (independente do sistema)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Cadastrar usuário
def cadastrar_usuario():
    print()
    time.sleep(0.5)
    print("Precisamos saber qual seu perfil para cadastro...")
    time.sleep(1)

    try:
        tipo_usuario = int(input('''Digite o tipo de usuário.
1 - Aluno Representante 
Insira o número correspondente: '''))
        if tipo_usuario != 1:
            raise UsuarioInvalidoError("Tipo de usuário inválido.")

        print()
        time.sleep(0.5)

        nome = input("Digite seu nome: ").strip()
        cpf = input("Digite seu CPF: ").strip()
        email = input("Digite seu email: ").strip()
        turma = input("Digite sua turma: ").strip()
        conta = input("Digite sua conta: ").strip()
        senha = input("Digite sua senha: ").strip()

        usuario = AlunoRepresentante(nome, senha, cpf, email, turma, Conta("Banco X", conta, "1234-5678", "chavepix", 1000, 0, None))
        usuarios_cadastrados.append(usuario)

        print()
        time.sleep(0.5)
        print("Cadastro realizado com sucesso!")
        time.sleep(1)

    except ValueError:
        print("Erro: Por favor, insira um número válido para o tipo de usuário.")
    except UsuarioInvalidoError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        limpar_tela()
        print("Finalizando cadastro.\n")

# Fazer login
def fazer_login():
    print()
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    print()
    time.sleep(0.5)
    print("Verificando...")
    time.sleep(1)

    try:
        usuario_encontrado = None
        for usuario in usuarios_cadastrados:
            if usuario.nome == nome and usuario.validar_senha(senha):
                usuario_encontrado = usuario
                break

        if not usuario_encontrado:
            raise UsuarioInvalidoError("Nome de usuário ou senha incorretos.")

        print()
        print("Login bem-sucedido!")
        return usuario_encontrado

    except UsuarioInvalidoError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Finalizando processo de login.\n")

# Menu principal
def menu():
    while True:
        print("\n\033[1;35m1. Cadastrar Usuário")
        print("\n2. Fazer Login")
        print("\n3. Acessar Instâncias ")
        print("\n4. Sair\033[m")

        print()
        try:
            opcao = input("Digite a opção desejada: ").strip()

            if opcao == "1":
                cadastrar_usuario()
            elif opcao == "2":
                usuario = fazer_login()
                if usuario:
                    print(f"Bem-vindo, {usuario.nome}!")
            elif opcao == "3":
                instancias()
            elif opcao == "4":
                print("Saindo...")
                break
            else:
                raise ValueError("Opção inválida. Tente novamente.")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
        finally:
            print("Retornando ao menu principal.\n")
            time.sleep(1)

# Iniciar o menu
menu()

# Fim do código
