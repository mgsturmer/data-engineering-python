#Operadores de identidade em Python

curso = "Curso de Python"
nome_aula = "Operadores de Identidade em Python"
saldo, limite = 200, 200

print(saldo is limite)
#True

print(curso is nome_aula)
#False

print(curso is "Curso de Python")
#true

print(saldo is not limite)
#False
