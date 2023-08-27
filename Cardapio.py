total = 0
start = 0


print("Bem-vindo a lanchonete")
print(
    """
    Codigo      descricao  valor
    100          x-tudo     R$ 10,00
    101          x-egg      R$ 20,00
    102          x-salada    R$ 15,00
    """
)

while start == 0:

    print("RODEI PELA PRIMEIRA VEZ")

    pedido = input("entre com o codigo do produto:")

    if pedido == "100":
       total += 10
       print("Voce pediu um x-tudo, no valor de 10 reais\n")
    elif pedido == "101":
        total += 20
        print("Voce pediu um x-egg, no valor de 20 reais\")
    elif pedido == "102":
        total += 15
        print("Voce pediu um x-salada, no valor de 15 reais\n")

    else: 
       print("Código inválido")

    resposta = input("Deseja pedir mais alguma coisa:\n1 - sim\n2 - nao\n")

    if resposta == '2':
        print (total)
        print ("O valor total é:", total)
        start = 1