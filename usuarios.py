from abc import ABC, abstractmethod

# Classe abstrata Pessoa
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
        if not isinstance(senha, str):
            raise TypeError("A senha deve ser uma string.")
        return self.__senha == senha

    def mostrar_nome(self):
        return self.nome

    def get_cpf(self):
        if not self.__cpf:
            raise ValueError("CPF inválido ou não definido.")
        return self.__cpf

    def get_email(self):
        if not self.__email:
            raise ValueError("Email inválido ou não definido.")
        return self.__email

# Aluno herda os atributos e métodos da classe Pessoa
class AlunoRepresentante(Pessoa):
    def __init__(self, nome, senha, cpf, email, turma, conta):
        super().__init__(nome, senha, cpf, email)
        if not isinstance(turma, str):
            raise TypeError("A turma deve ser uma string.")
        self.turma = turma
        self.conta = conta

    def exibirConta(self):
        if not self.conta:
            raise ValueError("Conta não definida.")
        return f"{self.conta.exibirChave()}"

    def exibir_info(self):
        return f'''
Aluno representante: {self.nome}
Turma: {self.turma}
CPF: {self.get_cpf()}
Email: {self.get_email()}
'''

    def dividirValor(self, total: int, divisor: int) -> int:
        # Divide um valor total por um divisor e retorna o valor dividido.
        try:
            if not isinstance(total, int) or not isinstance(divisor, int):
                raise TypeError("Os valores total e divisor devem ser inteiros.")
            if divisor == 0:
                raise ZeroDivisionError("Divisor não pode ser zero.")
            return total // divisor
        except Exception as e:
            print(f"Erro ao dividir valor: {e}")
            return 0

    def calcularLucro(self, receita: int, custo: int) -> int:
        # Calcula o lucro com base na receita e no custo.
        try:
            if not isinstance(receita, int) or not isinstance(custo, int):
                raise TypeError("Receita e custo devem ser números inteiros.")
            lucro = receita - custo
            return lucro
        except Exception as e:
            print(f"Erro ao calcular lucro: {e}")
            return 0