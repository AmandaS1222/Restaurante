import os
os.system("cls || clear")

valorbruto = 0
def resultado_final(desc_apli, nome):
    print('-'*27)
    print(f"""========VALOR FINAL========
          {desc_apli} e {nome}""")

valorbruto = 14
soma = 6
valorbruto = valorbruto + soma 
while True:
    pagamento = input(f"Qual seria a forma de pagamento? Caso for á vista, digite 'V'. Caso for credito, digite 'C' ")
    if pagamento == "V":
        valorreal = valorbruto - (valorbruto / 10)
        resultado_final("-","Desconto:")
        break
    elif pagamento == "C":
        valorreal = valorbruto + (valorbruto / 10)
        resultado_final("+","Taxa:")
        break
    else:
        print("CODIGO INCORRETO, UTILIZE 'V' E 'C'")
resultado_final()