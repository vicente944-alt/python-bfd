class ContaCorrente:
    def __init__(self, cpf, nomeC, saldo):
        self.cpf = cpf
        self.nomeC = nomeC
        self.saldo = saldo

    def addSaldo(self, valorAdd):
        if valorAdd > 0:
            self.saldo = self.saldo + valorAdd
        else:
            print("Valor inválido.")

    def sacaDinheiro(self, valorSac):
        if self.saldo >= valorSac:
            if valorSac > 0:
                self.saldo = self.saldo - valorSac
            else:
                print("Valor inválido.")
        else:
            print("Saldo insuficiente.")

    def verifSaldo(self):
        print(f"Saldo: R$ {self.saldo}")

def main():
    print("_____Conta Corrente_____")
    conta = ContaCorrente("123.456.789-00", "Fulanelson Silva", int(input("Saldo Incial: R$ ")))
    print(f"Nome: {conta.nomeC}\nCPF: {conta.cpf}")
    while True:
        print("1. Adicionar Saldo\n2. Sacar Dinheiro\n3. Verificar Saldo")
        acao = input('Digite o número da ação a ser realizada ou "/exit" para sair: ')
        if acao == "1" or acao == "1.":
            conta.addSaldo(int(input("Quanto vai adicionar? R$ ")))
        elif acao == "2" or acao == "2.":
            conta.sacaDinheiro(int(input("Quanto vai sacar? R$ ")))
        elif acao == "3" or acao == "3.":
            conta.verifSaldo()
        elif acao == "/exit":
            break
        else:
            print("Comando inválido.")
main()
