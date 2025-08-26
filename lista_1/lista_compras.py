#  Crie uma lista com 5 itens de compra e use um
#  loop for para exibir os itens da lista

lista_compras = []

for numero_item in range(5):
    item_lista = input("adicione o item da lista: ")
    lista_compras.append(item_lista)

print("eis a lista de compras para a janta: ", lista_compras)