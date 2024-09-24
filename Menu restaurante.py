import os
os.system("cls || clear")

print("""
    código: 1 nome: Lasanha / preço: 30.0
    código: 2 nome: Pizza / preço: 25.0
    código: 3 nome: Burger / preço: 20.0
    código: 4 nome: Salada / preço: 15.0
    código: 5 nome: Sushi / preço: 50.0
    código: 6 nome: Tacos / preço: 18.0
    código: 7 nome: Frutos do Mar / preço: 45.0
""")

pedidos = []
precos = {
    1: 30.0,
    2: 25.0,
    3: 20.0,
    4: 15.0,
    5: 50.0,
    6: 18.0,
    7: 45.0
}

while True:
    codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))
    
    if codigo == 0:
        break
    
    match codigo:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7:
            pedidos.append(codigo)
        case _:
            print("Código inválido, por favor tente novamente.")

    continuar = input("Deseja fazer outro pedido?: ")
    if continuar.lower() != 'sim':
        break

    print("\nVocê fez os seguintes pedidos:")
    total = 0

for codigo in pedidos:
    match codigo:
        case 1:
            nome = "Lasanha"
        case 2:
            nome = "Pizza"
        case 3:
            nome = "Burger"
        case 4:
            nome = "Salada"
        case 5:
            nome = "Sushi"
        case 6:
            nome = "Tacos"
        case 7:
            nome = "Frutos do Mar"
    
    preco = precos[codigo]
    print(f"Código: {codigo}, Nome: {nome}, Preço: R${preco:.2f}")
    total += preco

print(f"\nTotal a pagar: R${total:.2f}")