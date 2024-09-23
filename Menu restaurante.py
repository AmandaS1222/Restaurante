print("""
    Menu:
    1 - Strogonoff - 15
    2 - Feijoada - 10
    3 - Lasanha - 18
    4 - Moqueca - 25
    5 - Pizza - 30
    6 - Churrasco - 19
    7 - Sushi -20
""")

armazenamento = []

while True:
    prato = int(input("Digite o código do prato desejado: "))
    armazenamento.append(prato)

    if prato < 1 or prato > 7:
        print("Código inválido")
        break

    resposta = float(input("Deseja adicionar outro pedido? "))
    
    if resposta == "sim":
        Pedido_extra = int(input("Digite o código do prato que deseja: "))
        armazenamento.append(0)
    else:
        resposta == "não"
        break
        
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

    for prato in armazenamento:
        print(f"Valores: {prato}")