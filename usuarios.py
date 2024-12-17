from main import DivisorInvalidoError  # Importando a exceção personalizada
from abc import ABC, abstractmethod
from collections import deque


class Pessoa(ABC):
    def __init__(self, nome, senha, cpf, email):
        self.nome = nome
        self.__senha = senha  # Visibilidade privada
        self.__cpf = cpf
        self.__email = email

    @abstractmethod
    def exibir_info(self):
        pass

    def validar_senha(self, senha):
        return self.__senha == senha

    def mostrar_nome(self):
        return self.nome

    def get_cpf(self):
        return self.__cpf

    def get_email(self):
        return self.__email

#AlunoRepresentante herda atributos e métodos da classe Pessoa
class AlunoRepresentante(Pessoa):
    def __init__(self, nome, senha, cpf, email, turma, conta):
        super().__init__(nome, senha, cpf, email)
        self.turma = turma
        self.conta = conta


    def exibirConta(self):
        return f"{self.conta.exibirChave()}"

    def exibir_info(self):
        return f'''
Aluno representante: {self.nome}
Turma: {self.turma}
CPF: {self.get_cpf()}
Email: {self.get_email()}
'''

    def dividirValor(self, total: int, divisor: int) -> int:
        try:
            if divisor == 0:
                raise DivisorInvalidoError()  # Levanta exceção personalizada
            resultado = total // divisor
            self.historico_valores.append(resultado)  # Armazena o resultado na lista
            return resultado
        except DivisorInvalidoError as e:
            print(e)
            return 0
        finally:
            print("Operação de divisão concluída (com sucesso ou falha).")

    def calcularLucro(self, receita: int, custo: int) -> int:
        try:
            lucro = receita - custo
            if lucro < 0:
                raise ValueError("O lucro não pode ser negativo.")
            return lucro
        except ValueError as e:
            print(e)
            return 0
        finally:
            print("Operação de cálculo de lucro finalizada.")