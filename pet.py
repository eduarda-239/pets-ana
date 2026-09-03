class Pet:
    def __init__(self, nome, raca, especie, idade, observacoes):
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._idade = idade
        self._observacoes = observacoes

    def __str__(self):
        return f"Nome: {self._nome} | Raça: {self._raca} | Espécie: {self._especie} | Idade: {self._idade} | Observações: {self._observacoes}"

