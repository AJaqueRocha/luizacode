# Usuario = []
# Endereco = []
# Produto = []

# def cadastro_usuario():
#     while True:
#         print("Informe o usuário: ")
#         #verificar como criar um id para cada usuário
#         dados = {} #Aqui vai criar um dicionário com todos os dados
#         dados["Nome completo"] = (input("Nome: "))
#         dados["e-mail"] = (input("e-mail: "))
        
from carrinho_class import CarrinhoDeCompras

qtdade_produto = int(input("Quantos produtos você deseja colocar no carrinho? "))

count = 0
while count < qtdade_produto:
    id_usuario = input("Insira o id do usuário: ")
    id_produto = input("Insira o id do produto: ")
    preco_produto = float(input("Insira o preço do produto: "))
    qtdade_produto = int(input("Insira a quantidade de produto: "))
    CarrinhoDeCompras.adiciona_item_carrinho(id_produto,  id_usuario, preco_produto, qtdade_produto)
    count += 1
    
print("Itens no carrinho: ", CarrinhoDeCompras.carrinho)

id_produto_buscar = input("Insira o id do produto que você deseja buscar: ")
item = CarrinhoDeCompras.get_item_por_produto(id_produto_buscar)
print('Item buscado', item)

id_produto_remove = input("Insira o id do produto que você deseja remover do carrinho: ")
item = CarrinhoDeCompras.remove_item_id_produto(id_produto_remove)
print("Carrinho de compras atual:", CarrinhoDeCompras.carrinho)

#calcular o total do carrinho       
        