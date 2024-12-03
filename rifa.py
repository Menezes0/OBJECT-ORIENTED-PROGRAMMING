import random
#Rifa tem uma associação com a classe Conta, pois nela serão armazenados os valores arrecadados da rifa

class Rifa:
    def __init__(self, nome, qntdNumeros, precoNumero):
        self.nome = nome
        self.qntdNumeros = qntdNumeros
        self.precoNumero = precoNumero
        self.numerosVendidos = []

    def getNome(self):
        return self.nome

    def setNome(self):
        return self.nome

    def getQntdnumeros(self):
        return self.qntdNumeros

    def setQntdnumeros(self):
        return self.qntdNumeros

    def getPrecoNumero(self):
        return self.precoNumero

    def setPrecoNumero(self):
        return self.precoNumero

    def getNumerosVendidos(self):
        return self.numerosVendidos

    def setNumerosVendidos(self):
        return self.numerosVendidos

    def exibirRifa(self):
        print(f'''
Nome da Rifa: {self.nome}.
Quantidade de números: {self.qntdNumeros}.
Valor por número: {self.precoNumero}''')


    def venderNumero(self, numero): #Vende um número, se ainda não estiver vendido.
        if len(self.numerosVendidos) < self.qntdNumeros: #O len é uma função embutida em Python que retorna o comprimento (ou a quantidade de itens) de um objeto.
            if numero not in self.numerosVendidos:
                self.numerosVendidos.append(numero)
                print(f"Número {numero} vendido com sucesso!")
            else:
                print(f"Número {numero} já foi vendido.")
        else:
            print("Todos os números já foram vendidos.")
    def exibirNumeros(self): #Exibe os números vendidos, pois não há uma um atributo contendo os números não vendidos
        if self.numerosVendidos:
            print("Números vendidos:", self.numerosVendidos)
        else:
            print("Nenhum número vendido até o momento.")
    def sortearVencedor(self): #Sorteia um vencedor entre os números vendidos
        if self.numerosVendidos:
            vencedor = random.choice(self.numerosVendidos)
            print(f"O vencedor é o número: {vencedor}")
        else:
            print("Nenhum número vendido. Não é possível sortear um vencedor.")