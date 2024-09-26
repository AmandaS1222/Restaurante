import os
os.system("cls || clear")

def exibir_menu():
    print("""\
    código: 1 nome: Lasanha / preço: 30.0
    código: 2 nome: Pizza / preço: 25.0
    código: 3 nome: Burger / preço: 20.0
    código: 4 nome: Salada / preço: 15.0
    código: 5 nome: Sushi / preço: 50.0
    código: 6 nome: Tacos / preço: 18.0
    código: 7 nome: Frutos do Mar / preço: 45.0
    """)

def obter_nome_prato(codigo):
    match codigo:
        case 1:
            return "Lasanha"
        case 2:
            return "Pizza"
        case 3:
            return "Burger"
        case 4:
            return "Salada"
        case 5:
            return "Sushi"
        case 6:
            return "Tacos"
        case 7:
            return "Frutos do Mar"
        case _:
            return None

def main():
    exibir_menu()

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

        continuar = input("Deseja fazer outro pedido? (sim/não): ")
        if continuar.lower() != 'sim':
            break

        print("\nVocê fez os seguintes pedidos:")
        total = 0
    
        for codigo in pedidos:
            nome = obter_nome_prato(codigo)
            preco = precos[codigo]
            print(f"Código: {codigo}, Nome: {nome}, Preço: R${preco:.2f}")
            total += preco
            valorreal = 0
    while True:
        pagamento = input(f"\nQual seria a forma de pagamento? Caso for á vista, digite 'V'. Caso for credito, digite 'C': ")
        if pagamento == "V":
            valorreal = total - (total / 10)
            des_acr = "sem desconto"
            print("Pagamento escolhido: Á Vista")
            print(f"Valor do desconto: -{total / 10} ")
            break
        elif pagamento == "C":
            valorreal = total + (total / 10)
            des_acr = "sem taxa"
            print("Pagamento escolhido: Crédito")
            print(f"Valor da taxa: +{total / 10} ")
            break
        else:
            print("CODIGO INCORRETO, UTILIZE 'V' E 'C'")
    
    print(f"""Valor {des_acr}: {total:.2f}
\nTotal a pagar: R${valorreal:.2f}
""")


main()