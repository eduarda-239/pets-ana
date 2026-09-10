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

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE nome = ?", (nome,)) # "Me dê os pets cujo nome seja igual ao nome que o usuário digitou."
    resultado = cursor.fetchone() # Pega uma linha retornada pelo banco e guarda em "resultado".
    conexao.close()

    if resultado:
        id, nome, raca, especie, idade, observacoes = resultado

        print(f"ID: {id} | Nome: {nome} | Raça: {raca} | Espécie: {especie} | Idade: {idade} | Observações: {observacoes}")
    else:
        return "Pet não encontrado."

def remover_pet():
    nome = input("Digite o nome do pet que deseja remover: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        cursor.execute("DELETE FROM pets WHERE id = ?", (resultado[0],))
        conexao.commit()
        conexao.close()
        return "Pet removido com sucesso!"
    
    conexao.close()
    return "Pet não encontrado."
    

def editar_pet():
    nome = input("Digite o nome do pet que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        novo_nome = input("Digite um novo nome: ")
        nova_raca = input("Digite uma nova raça: ")
        nova_especie = input("Digite uma nova espécie: ")
        nova_idade = input("Digite uma nova idade: ")
        nova_observacoes = input("Digite suas novas observações: ")

        cursor.execute("""
                UPDATE pets
                SET nome = ?, raca = ?, especie = ?, idade = ?, observacoes = ?
                WHERE id = ?
            """, (novo_nome, nova_raca, nova_especie, nova_idade, nova_observacoes, resultado[0]))

        conexao.commit()
        conexao.close()
        
        return "Pet atualizado com sucesso!"
    conexao.close()
    return "Pet não encontrado."

