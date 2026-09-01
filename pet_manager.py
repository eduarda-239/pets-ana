from pet import Pet

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

