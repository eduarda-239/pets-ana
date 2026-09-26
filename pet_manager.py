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

def validar_raca():
    while True:
        raca = input("Raça do pet: ")

        if raca.strip() and any(letra.isalpha() for letra in raca): 
    # strip() remove os espaços do começo e do final.
    # any() verifica se existe pelo menos uma letra dentro da raça.
    # isalpha() verifica se um caractere é uma letra.
    # O "and" exige que as duas condições sejam verdadeiras.
            return raca

        print("Digite uma raça válida.")

def validar_nome():
    while True:
        nome = input("Nome do pet: ")

        if nome.strip() and any(letra.isalpha() for letra in nome):
            # strip() verifica se o nome não está vazio ou composto apenas por espaços.
            # any() verifica se existe pelo menos uma letra dentro do nome.
            # isalpha() verifica se cada caractere analisado é uma letra.
            # O "and" exige que as duas condições sejam verdadeiras.
            
            return nome.strip().lower()

        print("Digite um nome válido.")


def cadastrar_pet():
    conexao = conectar() # Abra uma conexão com o banco patinhas.db e guarde essa conexão na variável conexao.

    nome = validar_nome()
    raca = validar_raca()
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
    nome = validar_nome()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE LOWER(nome) = ?", (nome,)) # "Me dê os pets cujo nome seja igual ao nome que o usuário digitou."
    resultado = cursor.fetchone() # Pega uma linha retornada pelo banco e guarda em "resultado".
    conexao.close()

    if resultado:
        id, nome, raca, especie, idade, observacoes = resultado

        return(f"ID: {id} | Nome: {nome} | Raça: {raca} | Espécie: {especie} | Idade: {idade} | Observações: {observacoes}")  # print = mostra | return = devolve
    else:
        return "Pet não encontrado."

def remover_pet():
    nome = validar_nome()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE LOWER(nome) = ?", (nome,))
    resultados = cursor.fetchall()

    if not resultados:
        conexao.close()
        return "Pet não encontrado."
    if len(resultados) == 1:
        pet = resultados[0]
        cursor.execute("DELETE FROM pets WHERE id = ?", (pet[0],))
        conexao.commit()
        conexao.close()
        return "Pet removido com sucesso!" 
    if len(resultados) > 1:
        print("Encontramos mais de um pet com esse nome.")

        for pet in resultados:
            print(f"ID: {pet[0]} | Nome: {pet[1]} | Raça: {pet[2]} | Idade: {pet[4]}")
        
        id_pet = int(input("Digite o ID do pet que deseja remover: "))
        if any(pet[0] == id_pet for pet in resultados):
            # Verifica se o ID digitado pertence a algum dos pets encontrados.
            cursor.execute("DELETE FROM pets WHERE id = ?", (id_pet,))
            conexao.commit()
            conexao.close()
            return "Pet removido com sucesso!"
        print("ID inválido.")
        conexao.close()
        return "Nenhum pet foi removido."
    

def editar_pet():
    nome = validar_nome()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets WHERE LOWER(nome) = ?", (nome,))
    resultados = cursor.fetchall()


    if not resultados:
        conexao.close()
        return "Pet não encontrado."
    
    if len(resultados) == 1:
        pet = resultados[0]
        novo_nome = validar_nome()
        nova_raca = validar_raca()
        nova_especie = validar_especie()
        nova_idade = validar_idade("Nova idade: ")
        nova_observacoes = validar_texto("Digite suas novas observações: ")

        cursor.execute("""
            UPDATE pets
            SET nome = ?, raca = ?, especie = ?, idade = ?, observacoes = ?
            WHERE id = ?
        """, (novo_nome, nova_raca, nova_especie, nova_idade, nova_observacoes, pet[0]))
        
        conexao.commit()
        conexao.close()
        
        return "Pet atualizado com sucesso!"

    if len(resultados) > 1:
        print("Encontramos mais de um pet com esse nome.")

        for pet in resultados:
            print(f"ID: {pet[0]} | Nome: {pet[1]} | Raça: {pet[2]} | Idade: {pet[4]}")

        id_pet = int(input("Digite o ID do pet que deseja editar: "))

        if any(pet[0] == id_pet for pet in resultados):
            novo_nome = validar_nome()
            nova_raca = validar_raca()
            nova_especie = validar_especie()
            nova_idade = validar_idade("Nova idade: ")
            nova_observacoes = validar_texto("Digite suas novas observações: ")
            cursor.execute("""
                UPDATE pets
                SET nome = ?, raca = ?, especie = ?, idade = ?, observacoes = ?
                WHERE id = ?
            """, (novo_nome, nova_raca, nova_especie, nova_idade, nova_observacoes, id_pet))

            conexao.commit()
            conexao.close()
            return "Pet atualizado com sucesso!"
        print("ID inválido.")
        conexao.close()
        return "Nenhum pet foi atualizado."

