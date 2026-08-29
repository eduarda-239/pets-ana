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

def listar_pets():
    for pet in pets:
        print(pet)


def buscar_pet():
    nome = input("Digite o nome do pet: ")

    for pet in pets:
        if nome == pet._nome:
            return pet 
    return "Pet não encontrado."


def remover_pet():
    nome = input("Digite o nome do pet que deseja remover: ")

    for pet in pets:
        if nome == pet._nome:
            pets.remove(pet)
            return "Pet removido com sucesso!"

    return "Pet não encontrado."

def editar_pet():
    nome = input("Digite o nome do pet que deseja editar: ")

    for pet in pets:
        if nome == pet._nome:
            novo_nome = input("Digite um novo nome: ")
            pet._nome = novo_nome

            nova_especie = input("Digite uma nova espécie: ")
            pet._especie = nova_especie

            nova_raca = input("Digite uma nova raça: ")
            pet._raca = nova_raca

            nova_idade = input("Digite uma nova idade: ")
            pet._idade = nova_idade

            nova_observacoes = input("Digite suas novas observações: ")
            pet._observacoes = nova_observacoes



while True:
    print("=== PATINHAS DA ANA ===")
    print("1 - Cadastrar pet")
    print("2 - Listar pets")
    print("3 - Buscar pet")
    print("4 - Remover pet")
    print("5 - Editar pet")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pet()
    elif opcao == "2":
        listar_pets()
    elif opcao == "3":
        buscar_pet()
    elif opcao == "4":
        remover_pet()
    elif opcao == "5":
        editar_pet()
    elif opcao == "6":
        break
