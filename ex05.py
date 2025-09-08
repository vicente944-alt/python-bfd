class Produto:
    def __init__(self, nome=str, preco=int, qntd=int):
        self.nome = nome
        self.preco = preco
        self.qntd = qntd


class Estoque:
    def __init__(self, produtos=list, nome=str, preco=int, qntd=int):
        self.produtos = produtos
        Produto.__init__(self, nome=str, preco=int, qntd=int)

    def adicionar(self, nome):
        self.produtos.append(nome)

    def remover(self, nome):
        self.produtos.remove(nome)

    def listar(self):
        print(self.produtos)


def main():
    print("___Lista de produtos___")
    lista = Estoque()
    while True:
        produto = Produto(input("Produto: "), 0, 0)
        print("1. Adicionar produto\n2. Remover produto\n3. Verificar lista")
        entrada = input('Digite o número da ação ou digite "/exit" para parar: ')
        if entrada == "1" or entrada == "1.":
            lista.adicionar(produto.nome)
        elif entrada == "2" or entrada == "2.":
            lista.remover(produto.nome)
        elif entrada == "3" or entrada == "3.":
            lista.listar()
        elif entrada == "/exit":
            break
        else:
            print("Comando inválido.")


main()