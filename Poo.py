import random

# Exceção
class RifaException(Exception):
    pass

class Rifa:
    def __init__(self, nome, qntdNumeros, precoNumero):
        self.nome = nome
        self.qntdNumeros = qntdNumeros
        self.precoNumero = precoNumero
        self.numerosVendidos = []

    def exibirRifa(self):
        print(f'''
Nome da Rifa: {self.nome}.
Quantidade de números: {self.qntdNumeros}.
Valor por número: {self.precoNumero}''')

    def venderNumero(self, numero): 
        try:
            if len(self.numerosVendidos) >= self.qntdNumeros:
                raise RifaException("Todos os números já foram vendidos.")
            if numero in self.numerosVendidos:
                raise RifaException(f"Número {numero} já foi vendido.")
            self.numerosVendidos.append(numero)
            print(f"Número {numero} vendido com sucesso!")
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Operação de venda de número concluída.")

    def exibirNumeros(self): 
        try:
            if not self.numerosVendidos:
                raise RifaException("Nenhum número vendido até o momento.")
            print("Números vendidos:", self.numerosVendidos)
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Operação de exibição de números concluída.")

    def sortearVencedor(self): 
        try:
            if not self.numerosVendidos:
                raise RifaException("Nenhum número vendido. Não é possível sortear um vencedor.")
            vencedor = random.choice(self.numerosVendidos)
            print(f"O vencedor é o número: {vencedor}")
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Operação de sorteio concluída.")

rifa = Rifa("Rifa Solidária", 5, 10.0)

rifa.exibirRifa()
rifa.venderNumero(1)
rifa.venderNumero(1)  # Tentativa de vender número repetido
rifa.venderNumero(6)  # Número válido
rifa.exibirNumeros()
rifa.sortearVencedor()  # Sorteio com números vendidos
rifa.venderNumero(7)  # Venda adicional
rifa.exibirNumeros()
