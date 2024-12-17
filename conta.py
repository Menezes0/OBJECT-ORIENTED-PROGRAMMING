#Assoçiação entre Conta e AlunoRepresentante, pois ele/a podem acessar as informações da conta
#A Conta também possue uma associação com Rifa, pois nela serão arrecadadas os valores da Rifa
from usuarios import AlunoRepresentante
class Conta:
    def __init__(self, banco, conta, agencia, chavePix, valorInicial, valorFinal, adm):
        self.__conta = conta
        self.__agencia = agencia
        self.__banco = banco
        self.chavePix = chavePix
        self.__valorInicial = valorInicial
        self.__valor = valorFinal
        self.adm = None

    def getConta(self):
        return self.__conta

    def setConta(self):
        return self.__conta

    def getAgencia(self):
        return self.__agencia

    def setAgencia(self):
        return self.__agencia

    def getBanco(self):
        return self.__banco

    def setBanco(self):
        return self.__banco

    def getChavePix(self):
        return self.chavePix

    def setChavePix(self):
        return self.chavePix

    def getvalorInicial(self):
        return self.__valorInicial

    def setvalorFinal(self):
        return self.__valor
######################################################################
    def exibirChave(self):
        print(f"Banco: {self.__banco}")
        print(f"Chave Pix: {self.chavePix}")

    def adicionarValor(self, valor):
        if valor > 0:
            self.__valor += valor

    def exibirSaldo(self):
        print(f"Saldo atual: {self.__valor}")

    def retirarValor(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O valor para retirada deve ser maior que zero.")

            if valor > self.__valor:
                raise ValueError("Saldo insuficiente para a retirada.")

            self.__valor -= valor
            print(f"Valor retirado: {valor}")

        except ValueError as e:
            print(f"Erro: {e}")
        else:
            print("Retirada realizada com sucesso.")
        finally:
            print("Processo de retirada concluído.")
