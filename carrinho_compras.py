cart = []
# for i in range(3)

id_user = input('Insira o id do usuário: ')
id_produto = input('Insira o id do produto: ')
price_product = float(input('Insira o preço do produto: '))
quantity_product = int(input('Insira a quantidade de produtos: '))

item = [id_user, id_produto, price_product, quantity_product]

#criar uma lista para cada item. Item1 = ['usuário', 'produto', preço, qtdade]
#cart = [item1, item2]
#print(cart)
#Adiciona na lista com o FOR
#for c in cart
# a A letra "c" vai correr a lista do item1 e depois a do item2


#Criar função para adicionar item no carrinho
def add_item_cart(item):
    cart.append(item)
    return cart

# retorne todos os itens do carrinho
def get_all_items_cart():
    return cart
    
# trazer todos os itens do carrinho pelos itens do produto
def get_item_card_by_id(id_product):
    new_lista = [item for item in cart if item[0] == '123']
print(new_lista[0])

#remover o item do carrinho que tem esse produto
def remove_item_id(id_product):
    pass