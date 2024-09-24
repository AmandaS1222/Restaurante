# cardapio
def definir_cardapio():
    return {
        1: {"nome": "Lasagna", "preco": 30.0},
        2: {"nome": "Pizza Margherita", "preco": 25.0},
        3: {"nome": "Burger", "preco": 20.0},
        4: {"nome": "Salada Caesar", "preco": 15.0},
        5: {"nome": "Sushi", "preco": 50.0},
        6: {"nome": "Tacos", "preco": 18.0},
        7: {"nome": "Frutos do Mar", "preco": 45.0},
    }

# menu
def exibir_cardapio(cardapio):
    print("Cardápio:")
    for codigo, info in cardapio.items():
        print(f"{codigo}: {info['nome']} - R$ {info['preco']:.2f}")

# pedidos
def fazer_pedido(cardapio):
    pedidos = []
    while True:
        codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))
        if codigo == 0:
            break
        elif codigo in cardapio:
            pedidos.append(cardapio[codigo])
        else:
            print("Código inválido, por favor tente novamente.")
    return pedidos