class DivisorInvalidoError(Exception):
    def __init__(self, mensagem="O divisor não pode ser zero!"):
        super().__init__(mensagem)