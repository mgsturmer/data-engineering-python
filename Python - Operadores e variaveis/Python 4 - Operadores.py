#Operadores AND, OR e outros em Python

saldo = 1000
saque = 200
limite_diario = 200

print(saldo >= saque and saque <= limite_diario)
#True

print(saldo == saque or saque <= limite_diario)
#True

print(not saque >= saque)
#False

print(not False)

#Sequencias vazias são falso em Python
print(not "")