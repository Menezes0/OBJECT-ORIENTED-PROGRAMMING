from local import Local
#Evento possue um relacionamento de agregação com Local, pois não há Evento sem um Local
class Evento:
    def __init__(self, nome, data, local, horarioInicial, horarioFinal ):
        self.nome = nome
        self.data = data
        self.local = local #Local está agregado ao Evento
        self.horarioInicial = horarioInicial
        self.horarioFinal = horarioFinal


    def getNome(self):
        return self.nome

    def setNome(self):
        return self.nome

    def getData(self):
        return self.data

    def setData(self):
        return self.data

    def getHorarioInicial(self):
        return self.horarioInicial

    def setHorarioInicial(self):
        return self.horarioInicial

    def getHorarioFinal(self):
        return self.horarioFinal

    def setHorarioFinal(self):
        return self.horarioFinal


    def detalhes(self):
        #agregação
        return f"Evento: {self.nome} \nData: {self.data} \nLocal: {self.local.ExibirLocal()}"


