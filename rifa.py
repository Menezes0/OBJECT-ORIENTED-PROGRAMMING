import random

# Exceção personalizada
class RifaException(Exception):
    pass

class Rifa:
    def __init__(self, nome, qntdNumeros, precoNumero):
        if qntdNumeros <= 0 or precoNumero <= 0:
            raise ValueError("Quantidade de números e preço devem ser maiores que zero.")
        self.nome = nome
        self.qntdNumeros = qntdNumeros
        self.precoNumero = precoNumero
        self.numerosVendidos = []

    def exibirRifa(self):
        print(f'''
Rifa: {self.nome}
Quantidade de números disponíveis: {self.qntdNumeros}
Preço por número: R$ {self.precoNumero:.2f}''')

    def venderNumero(self, numero): 
        try:
            if numero <= 0 or numero > self.qntdNumeros:
                raise RifaException(f"Número inválido. Escolha entre 1 e {self.qntdNumeros}.")
            if numero in self.numerosVendidos:
                raise RifaException(f"O número {numero} já foi vendido.")
            if len(self.numerosVendidos) >= self.qntdNumeros:
                raise RifaException("Todos os números já foram vendidos.")
            
            self.numerosVendidos.append(numero)
            print(f"Número {numero} vendido com sucesso!")
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Finalizando operação de venda.\n")

    def exibirNumeros(self): 
        try:
            if not self.numerosVendidos:
                raise RifaException("Nenhum número foi vendido até o momento.")
            print("Números vendidos:", ", ".join(map(str, self.numerosVendidos)))
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Finalizando operação de exibição.\n")

    def sortearVencedor(self): 
        try:
            if not self.numerosVendidos:
                raise RifaException("Nenhum número vendido. Não é possível realizar o sorteio.")
            
            vencedor = random.choice(self.numerosVendidos)
            print(f"Parabéns! O número vencedor é: {vencedor}")
        except RifaException as e:
            print(f"Erro: {e}")
        finally:
            print("Finalizando operação de sorteio.\n")

    def exibirStatusCompleto(self):
        self.exibirRifa()
        self.exibirNumeros()
        print(f"Total arrecadado: R$ {len(self.numerosVendidos) * self.precoNumero:.2f}\n")

# Exemplo de uso
rifa = Rifa("Rifa Solidária", 5, 10.0)

rifa.exibirStatusCompleto()
rifa.venderNumero(1)
rifa.venderNumero(1)  # Tentativa de venda repetida
rifa.venderNumero(6)  # Número fora do intervalo
rifa.venderNumero(3)  # Venda válida
rifa.exibirNumeros()
rifa.sortearVencedor()
rifa.venderNumero(2)
rifa.exibirStatusCompleto()
