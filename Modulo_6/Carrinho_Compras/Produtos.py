products = (
    {
    "id": 123,
    "nome_produto": "Celular",
    "descricao": "Ultra novo e moderno",
    "preco": 3000.00
    },
    
    {
    "id": 456,
    "nome": "Bola",
    "descricao": "Bola de praia da copa",
    "preco": 400.00
    },
    
    {
    "id": 789,
    "nome": "Forno",
    "descricao": "Forno Elétrico Supersônico",
    "preco": 800.00
    }
)

cart = []

def showOptions():
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Exibir produtos e valor total")
    print("4 - Limpar carrinho")
    print("5 - Sair")
    
def showProducts():
    for p in products:
        print("Id: {0} - nome: {1} - descricao: {2} - preco: {3}\n".format(p["Id"], p["nome"], p["descricao"], p["preco"]))
    
option = "1"  

#print(Mensagem de boas vindas????)

while option != 5:
    showOptions()
    option = input("Digite a opção desejada: ")
    
    if(option == "1"):
        print("Digite o id do produto: ")
