from database import conectar

def validar_texto(mensagem):
    while True:
        texto = input(mensagem)

        if texto.strip(): # strip tira os espaços incorretos.
            return texto

        print("O campo não pode ficar vazio.")

def validar_idade(mensagem):
    while True:
        try:
            idade = int(input(mensagem))

            if idade < 0:
                print("A idade não pode ser negativa.")
                continue

            if idade > 16:
                print("A idade máxima é 16 anos.")
                continue
            return idade

        except ValueError:
            print("Digite uma idade válida.")

def validar_especie():
    while True:
        especie = input("Espécie do pet: ")

        if especie.lower() == "cachorro":
            return especie.strip().lower()
        print("A espécie deve ser cachorro.")


def cadastrar_pet():
    conexao = conectar() # Abra uma conexão com o banco patinhas.db e guarde essa conexão na variável conexao.

    nome = validar_texto("Nome do pet: ")
    raca = validar_texto("Raça do pet: ")
    especie = validar_especie()
    idade = validar_idade("Idade do pet: ")
    observacoes = validar_texto("Observações: ")
        
    cursor = conexao.cursor()  # Comando que vai permitir conversar com o banco de dados.
    cursor.execute("""
    INSERT INTO pets (nome, raca, especie, idade, observacoes)
    VALUES (?, ?, ?, ?, ?)
""", (nome, raca, especie, idade, observacoes))

    conexao.commit()  # quando alterou dados
    conexao.close()  # terminou de usar


def listar_pets():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets")  # "Me dê todos os pets"
    resultado = cursor.fetchall()  # pega todas as respostas e coloca dentro da variável resultado.

    conexao.close()

    for pet in resultado:
        id, nome, raca, especie, idade, observacoes = pet

        print(f"ID: {id} | Nome: {nome} | Raça: {raca} | Espécie: {especie} | Idade: {idade} | Observações: {observacoes}")


def buscar_pet():
    nome = validar_texto("Digite o nome do pet: ")

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
    nome = validar_texto("Digite o nome do pet: ")

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
    nome = validar_texto("Digite o nome do pet que deseja editar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        novo_nome = validar_texto("Digite um novo nome: ")
        nova_raca = validar_texto("Digite uma nova raça: ")
        nova_especie = validar_texto("Digite uma nova espécie: ")
        nova_idade = validar_idade("Nova idade: ")
        nova_observacoes = validar_texto("Digite suas novas observações: ")

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

