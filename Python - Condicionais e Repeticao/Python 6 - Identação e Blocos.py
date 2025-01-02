#Em Python, identação define blocos de execução além de 
# deixar o código mais legível e manutenível. 

#A convenção define 4 espaços em branco por nível de identação

#Método para Saque
def sacar(valor): #início do método sacar
    saldo = 500

    if saldo >= valor: #início do bloco if
        saldo -= valor
        print("Valor sacado com sucesso!")

    #fim do if 
#fim do bloco do método sacar
sacar(200)

#Método para Deposito
def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor depositado com sucesso!")

depositar(200)