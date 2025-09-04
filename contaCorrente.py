class ContaCorrente:
    def __init__(self, cpf, nomeC, saldo):
        self.cpf = cpf
        self.nomeC = nomeC
        self.saldo = saldo

    def addSaldo(self, valorAdd):
        self.saldo = self.saldo + valorAdd

    def sacaDinheiro(self, valorSac):
        if self.saldo >= valorSac:
            self.saldo = self.saldo - valorSac
        else:
            print("Saldo insuficiente.")

    def verifSaldo(self):
        print(f"Saldo: {self.saldo}")

def main():
    print("Conta Corrente")
    conta = ContaCorrente("123.456.789-00", "Fulanelson", int(input("Saldo Incial: ")))
    while True:
        print("1. Adicionar Saldo\n2. Sacar Dinheiro\n3. Verificar Saldo")
        acao = input('Digite o número da ação a ser realizada ou "/exit" para sair: ')
        if acao == "1" or acao == "1.":
            conta.addSaldo(int(input("Quanto vai adicionar? ")))
        elif acao == "2" or acao == "2.":
            conta.sacaDinheiro(int(input("Quanto vai sacar? ")))
        elif acao == "3" or acao == "3.":
            conta.verifSaldo()
        elif acao == "/exit":
            break
        else:
            print("Comando inválido.")
main()