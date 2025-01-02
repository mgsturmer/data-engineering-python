#Caixa alta, caixa baixa e título.

curso = "PyThOn"
nome = "matheus gabriel sturmer"
nome_espacos_antes = "   Matheus"
nome_espacos_depois = "Matheus   "
nome_entre_espacos = "   Matheus   "


#CAIXA ALTA
print(curso.upper())

#caixa baixa
print(curso.lower())

#Para Títulos (Primeira Letra Maiuscula)
print(curso.title())

#Vai corrigir as letras maiúsculas de um título.
print(nome.title())

#Eliminando espaços

#Remove espaços
print(nome_entre_espacos.strip())
#Remove espaços no LeftSide
print(nome_espacos_antes.lstrip())
#Remove espaços no RightSide
print(nome_espacos_depois.rstrip())

#Preencher com caracteres
print(nome.center(30, "#"))

#Adicionar caracteres intermediários
print(".".join(curso))