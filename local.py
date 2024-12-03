#Local possue um relaciona de agregação com Evento, pois não há Evento sem um Local

class Local:
    def __init__(self, logradouro, bairro, cidade, capacidade):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.capacidade = capacidade


    def getLogradouro(self):
        return self.logradouro

    def setLogradouro(self):
        return self.logradouro

    def getBairro(self):
        return self.bairro

    def setBairro(self):
        return self.bairro

    def getCidade(self):
        return self.cidade

    def setCidade(self):
        return self.cidade

    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self):
        return self.capacidade


    def ExibirLocal(self):
        return f'''{self.logradouro}, {self.bairro}, {self.cidade}'''

