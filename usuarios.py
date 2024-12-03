from abc import ABC, abstractmethod


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

#Aluno herda os atributos e métodos da classe Pessoa
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
        #Divide um valor total por um divisor e retorna o valor dividido.
        if divisor == 0:
            print("Divisor não pode ser zero.")
            return 0
        return total // divisor

    def calcularLucro(self, receita: int, custo: int) -> int:#Calcula o lucro com base na receita e no custo.
        lucro = receita - custo
        return lucro
