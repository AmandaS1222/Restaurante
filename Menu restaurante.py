print("""
    Menu:
    1 - Strogonoff
    2 - Feijoada
    3 - Lasanha
    4 - Moqueca
    5 - Pizza
    6 - Churrasco
    7 - Sushi
""")

while True:
    prato = int(input("Digite o código do prato desejado: "))
    
    if prato < 1:
        print("Código inválido, escreve um código válido")
        break
    else:
        prato > 7
        print("Código inválido, escreve um código válido")

    int(input("Deseja adicionar outro pedido? "))
    Pedido_extra = int(input("Digite o código do prato que deseja: "))
    
    match(Pedido_extra):
        case "1":
            nome = "Strogonoff"
            codigo = 1 
        case "2":
            nome = "Feijoada"
            codigo = 2
        case "3":
            nome = "Lasanha"
            codigo = 3
        case "4":
            nome = "Moqueca"
            codigo = 4
        case "5":
            nome = "Pizza"
            codigo = 5
        case "6":
            nome = "Churrasco"
            codigo = 6
        case "7":
            nome = "Sushi"
            codigo = 7