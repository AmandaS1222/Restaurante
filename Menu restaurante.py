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
    codigo = int(input("Digite o código do prato desejado: "))
    
    if codigo < 1:
        print("Código inválido")
        break
    else:
        codigo > 7
        print("Código inválido")

