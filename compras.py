def produtos():
    print('''
    ---Produtos---
    [0] - Notebook: R$ 3500,00
    [1] - Smartphone: R$ 2000,00
    [2] - Fone de Ouvido: R$ 150,00
    [3] - Carregador: R$ 90,00
    [4] - Cabo USB: R$ 30,00
    ''')
def menu():
    print('''
    [0] - Ver Produtos
    [1] - Adicionar produtos ao carrinho
    [2] - Ver o Carrinho
    [3] - Mostrar valor Total
    [4] - Finalizar Compras
    ''')
def mostrar_produtos(q=0):
    produtos()
def adionar_ao_carrinho(q=1):
    while True:
        pergunta = int(input('Digite o número respectivo ao produto desejado:'))
        if pergunta < 0 or pergunta > 4:
            print('Valor digitado inválido')
        else:
            c.append(p[pergunta])
        pergunta2 = str(input('Deseja escolher algo mais? (S/N): ')).upper()
        if pergunta2 == 'N':
            break
        elif pergunta2 == 'S':
            continue
        else:
            print('Resposta não identificada')
            break
def ver_carrinho(q=2):
    if len(c) == 0:
        print('\nCarrinho Vazio\n')
    else:
        print('Carrinho:\n', c)
def ver_total_da_compra(q=3):
    total = sum(p[1] for p in c)
    print('\nTotal da Compra: R$', total)
def finalizar_compra(q=4):
    total = sum(p[1] for p in c)
    print('\nTotal da compra: R$', total, '\nProdutos Escolhidos:\n', c)

c=[]
p=[
    ('[0]-Notebook', 3500.00),
    ('[1]-Smartphone', 2000.00),
    ('[2]-Fone de Ouvido', 150.00),
    ('[3]-Carregador', 90.00),
    ('[4]-Cabo USB', 30.00)
]
while True:
    m=[
        ('[0]-Ver produtos'),
        ('[1]-Adicionar produtos ao carrinho'),
        ('[2]-Ver Carrinho'),
        ('[3]-Ver total da compra'),
        ('[4]-Finalizar Compra')
    ]
    print('---Armazém Mataraca---')
    menu()
    q=int(input('Digite o número relativo a função desejada:'))
    if q<0 or q>4:
        print('Valor digitado inválido')
    elif q==0:
       mostrar_produtos()
    elif q==1:
       adionar_ao_carrinho()
    elif q==2:
        ver_carrinho()
    elif q==3:
       ver_total_da_compra()
    elif q==4:
        break
finalizar_compra()