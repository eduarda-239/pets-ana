class Pet:
    def __init__(self, nome, raca, especie, idade, observacoes):
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._idade = idade
        self._observacoes = observacoes

    def __str__(self):
        return f"Nome: {self._nome} | Raça: {self._raca} | Espécie: {self._especie} | Idade: {self._idade} | Observações: {self._observacoes}"


pets = []


def cadastrar_pet():
    nome = input("Nome do pet: ")
    raca = input("Raça: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")
    observacoes = input("Observações: ")

    pet = Pet(nome, raca, especie, idade, observacoes)
    pets.append(pet)

cadastrar_pet()

while True:

    continuar = input("Deseja cadastrar outro? (s/n): ").lower()

    if continuar == "n":
        break

    cadastrar_pet()

def listar_pets():
    for pet in pets:
        print(pet)

listar_pets()

def buscar_pet():
    nome = input("Digite o nome do pet: ")

    for pet in pets:
        if nome == pet._nome:
            return pet 
    return "Pet não encontrado."

resultado = buscar_pet()
print(str(resultado))

