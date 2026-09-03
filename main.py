from pet_manager import cadastrar_pet, listar_pets, buscar_pet, remover_pet, editar_pet


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
        resultado = buscar_pet()
        print(resultado)
    elif opcao == "4":
        resultado = remover_pet()
        print(resultado)
    elif opcao == "5":
        resultado = editar_pet()
        print(resultado)
    elif opcao == "6":
        break
