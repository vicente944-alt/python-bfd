class Produto:
    def __init__(self, item, preco, qntd):
        self.item = item
        self.preco = preco
        self.qntd = qntd


class Estoque:
    def __init__(self, lista=[]):
        self.lista = lista

    def adicionar(self, item=Produto):
        self.lista.append(item)

    def remover(self, item):
        if item not in self.lista:
            print("Isso não está na lista.")
        else:
            self.lista.remove(item)

    def listar(self):
        print(self.lista)


def main():
    print("___Lista de produtos___")
    lista = Estoque()
    while True:
        print("1. Adicionar produto\n2. Remover produto\n3. Verificar lista")
        entrada = input('Digite o número da ação ou digite "/exit" para parar: ')

        if entrada == "1" or entrada == "1.":
            produto = Produto(input("Produto: ").title(), 0, 0)
            lista.adicionar(produto.item)

        elif entrada == "2" or entrada == "2.":
            produto = Produto(input("Produto: ").title(), 0, 0)
            lista.remover(produto.item)

        elif entrada == "3" or entrada == "3.":
            lista.listar()

        elif entrada == "/exit":
            break

        else:
            print("Comando inválido.")


main()
