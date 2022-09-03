carts = [['123', '1', 100.00, 2], ['456', '2', 899.00, 1]]

#Quero o produto que é o tênis, que tem o código '123'
# new_lista=[]
# for item in carts:
#     if item[0] == '123':
#         new_lista.append(item)
        
# print(new_lista[0])

new_lista = [item for item in carts if item[0] == '123']
print(new_lista[0])

# def filtra_item(item, produto):
#     if item[0] == produto:
#         return item
