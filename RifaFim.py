import random

# 📝 Controle de Rifas 🎟️
print("🗒️˖  ་ : Controle de rifas 𖦆 ⏱️ ぃ ˑ   ֺ 𖥻 ִ ۫  ּ  𖥔 𓄼 ֗  𖥔")

# Exceções personalizadas
class NumeroIndisponivelError(Exception):
    def __init__(self, numero):
        self.numero = numero

class LimiteVendasExcedidoError(Exception):
    def __init__(self, limite):
        super().__init__(f"Ops! O limite de venda de {limite} números foi atingido.")
        self.limite = limite

# Classe Rifa
class Rifa:
    def __init__(self, nome, qntdNumeros, precoNumero):
        self.nome = nome
        self.qntdNumeros = qntdNumeros
        self.precoNumero = precoNumero
        self.numerosVendidos = []  # Lista para armazenar os números vendidos

    # Métodos getters e setters
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_qntd_numeros(self):
        return self.qntdNumeros

    def set_qntd_numeros(self, qntdNumeros):
        self.qntdNumeros = qntdNumeros

    def get_preco_numero(self):
        return self.precoNumero

    def set_preco_numero(self, precoNumero):
        self.precoNumero = precoNumero

    def get_numeros_vendidos(self):
        return self.numerosVendidos

    def set_numeros_vendidos(self, numerosVendidos):
        self.numerosVendidos = numerosVendidos

    # Método para exibir as informações da rifa
    def exibir_rifa(self):
        print(f'''
Rifa: {self.nome}
Total de Números Disponíveis: {self.qntdNumeros}
Preço por número: {self.precoNumero}''')

    # Método para vender um número
    def vender_numero(self, numero):
        """Método para vender um número da rifa com verificações de erro."""
        try:
            # Verificando se o limite de vendas foi atingido
            if len(self.numerosVendidos) >= self.qntdNumeros:
                raise LimiteVendasExcedidoError(self.qntdNumeros)

            # Verificando se o número já foi vendido
            if numero in self.numerosVendidos:
                raise NumeroIndisponivelError(numero)

            # Adicionando o número vendido à lista
            self.numerosVendidos.append(numero)
            print(f"Sucesso! O número {numero} foi vendido com sucesso.")
        
        except NumeroIndisponivelError as erro:
            print(f"Erro! O número {erro.numero} já foi vendido ou não está disponível.")
        except LimiteVendasExcedidoError as erro:
            print(erro)  # Exibe o erro personalizado de limite excedido
        finally:
            print("Venda finalizada (ou tentativa concluída).")

    # Método para exibir números vendidos e disponíveis
    def exibir_numeros(self):
        """Exibe os números vendidos e a quantidade de números restantes."""
        if self.numerosVendidos:
            print("Números vendidos:", self.numerosVendidos)
        else:
            print("Nenhum número foi vendido ainda.")
        print(f"Números disponíveis: {self.qntdNumeros - len(self.numerosVendidos)}")

    # Método para sortear um vencedor
    def sortear_vencedor(self):
        """Sorteia um vencedor entre os números vendidos."""
        if self.numerosVendidos:
            vencedor = random.choice(self.numerosVendidos)
            print(f"O vencedor da rifa é o número: {vencedor}")
        else:
            print("Nenhum número foi vendido. Não é possível realizar o sorteio.")

# Função para exibir o menu com opções para o usuário
def exibir_menu():
    print("\nEscolha uma das opções:")
    print("1. Exibir informações da rifa")
    print("2. Vender um número")
    print("3. Exibir números vendidos")
    print("4. Sortear um vencedor")
    print("5. Sair")

# Exemplo de uso
rifa = Rifa("Rifa de Natal 🎅", 100, 10.0)

while True:
    exibir_menu()  # Exibe o menu para o usuário
    try:
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            rifa.exibir_rifa()  # Exibe as informações da rifa
        elif escolha == 2:
            numero = int(input("Digite o número a ser vendido: "))
            rifa.vender_numero(numero)  # Realiza a venda
        elif escolha == 3:
            rifa.exibir_numeros()  # Exibe números vendidos
        elif escolha == 4:
            rifa.sortear_vencedor()  # Sorteia um vencedor
        elif escolha == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")