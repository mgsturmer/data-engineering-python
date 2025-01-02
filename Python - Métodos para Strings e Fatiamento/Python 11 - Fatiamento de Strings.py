#Técnicas de fatiamento para retornar substrings.

nome = "Matheus Gabriel Sturmer"

#Selecionando só o caractere indice 0 (primeiro)
print(f"A primeira letra do seu nome é {nome[0].upper()}")

#Selecionando os caracteres de 0 até 7 (8 caracteres)
print(nome[:8])

#Selecionando os caracteres de 7 até o fim 
print(nome[8:])

#Selecionando valores intermediários
print(nome[8:15])

#Selecionando com steps, somente os impares:
print(nome[::2])

#Inversão de strings
print(nome[::-1])