nome = "Matheus"
idade = 28
profissao = "Data Engineer"
curso = "Python"

#Diversas maneiras de fazer isso
print("Olá, me chamo %s. eu tenho %d anos de idade, sou %s e estou matriculado no curso de %s." %(nome, idade, profissao, curso))

#Outro exemplo
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos e estou estudando {curso}")

PI = 3.14159

#PI com 2 decimais.
print(f"valor de PI: {PI: .2f}")

#PI com espaçamento a esquerda (preenchendo com espaços)
print(f"valor de PI: {PI: 10.2f}")