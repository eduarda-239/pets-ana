class Pet:
    def __init__(self, nome, raca, especie, idade, observacoes):
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._idade = idade
        self._observacoes = observacoes

belinha = Pet("Belinha", "pinsher", "cachorro",12," ela morde")
meg = belinha = Pet("Meg", "vira-lata", "cachorro",9," dócil ")
print(meg._nome)
        