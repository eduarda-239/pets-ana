from pet import Pet
from database import conectar

pets = []

def cadastrar_pet():
    conexao = conectar() # Abra uma conexão com o banco patinhas.db e guarde essa conexão na variável conexao.

    nome = input("Nome do pet: ")
    raca = input("Raça: ")
    especie = input("Espécie: ")
    idade = input("Idade: ")
    observacoes = input("Observações: ")

    cursor = conexao.cursor()  # Comando que vai permitir conversar com o banco de dados.

    cursor.execute("""
    INSERT INTO pets (nome, raca, especie, idade, observacoes)
    VALUES (?, ?, ?, ?, ?)
""", (nome, raca, especie, idade, observacoes))

    conexao.commit()

    pet = Pet(nome, raca, especie, idade, observacoes)
    pets.append(pet)

def listar_pets():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets")  # "Me dê todos os pets"
    resultado = cursor.fetchall()  # pega todas as respostas e coloca dentro da variável resultado.

    for pet in resultado:
        id, nome, raca, especie, idade, observacoes = pet

        print(f"ID: {id} | Nome: {nome} | Raça: {raca} | Espécie: {especie} | Idade: {idade} | Observações: {observacoes}")


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

            nova_especie = input("Digite uma nova raça: ")
            pet._especie = nova_raca

            nova_raca = input("Digite uma nova espécie: ")
            pet._raca = nova_especie

            nova_idade = input("Digite uma nova idade: ")
            pet._idade = nova_idade

            nova_observacoes = input("Digite suas novas observações: ")
            pet._observacoes = nova_observacoes
            return "Pet atualizado com sucesso!"
    return "Pet não encontrado."
