import random

# Início do código
print("🗒️˖  ་ : Controle de rifas 𖦆 ⏱️ ぃ ˑ   ֺ 𖥻 ִ ۫  ּ  𖥔 𓄼 ֗  𖥔")

# Classe Rifa
class Rifa:
    def __init__(self, titulo, totalNumeros):
        self.titulo = titulo
        self.totalNumeros = totalNumeros
        self.numerosReservados = []  # Lista simples para armazenar números reservados

    # Método para exibir informações da rifa
    def mostrarDetalhes(self):
        print(f'Título da Rifa: {self.titulo}')
        print(f'Total de números disponíveis: {self.totalNumeros}')

    # Método para reservar um número
    def reservarNumero(self, numero):
        if numero < 1 or numero > self.totalNumeros:
            print(f"Número {numero} inválido! O número deve estar entre 1 e {self.totalNumeros}.")
        elif numero in self.numerosReservados:
            print(f"Número {numero} já foi reservado.")
        else:
            self.numerosReservados.append(numero)
            print(f"Número {numero} reservado com sucesso!")

# Exemplo de uso
rifa = Rifa("Rifa de Caridade", 100)  # Criando a rifa
rifa.mostrarDetalhes()  # Mostra as informações iniciais
rifa.reservarNumero(10)  # Reservando um número
rifa.reservarNumero(20)  # Reservando outro número