# from Projeto1 import db_produtos

# class carrinho:
#     produtos = []
#     total_produtos = 0
    
# def produtos():
#     int(input("Insira o id do produto: "))

db_produtos = ['id', 'nome_produto', 'descricao', 'preco']

qtd_items = int(input("Me diga quantos itens você vai colocar no carrinho: "))

count = 0
while count < qtd_items:
    id_usuario = input("Insira o id do usuário: ")
    id_produto = input("Insira o id do produto: ")
    preco_produto = float(input("Insira o preço do produto: "))
    quantidade_produto = int(input("Insira a quantidade de produto: "))

def produtos():
    int(input("Adicione o id do produto: "))

# {
#     "id": 123,
#     "nome_produto": "Celular",
#     "descricao": "Ultra novo e moderno",
#     "preco": 3000.00
# }