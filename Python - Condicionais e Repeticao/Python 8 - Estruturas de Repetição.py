#Estruturas de repetição em Python

#São estruturas utilizadas para repetir um trecho de código a partir
#de um operador lógico.

#For / For-Else, while, dowhile

#Transformando seu texto para UPPERCASE com for

##texto = input("Informe seu texto: ")
texto = "Matheus"
VOGAIS = "AEIOU"

#Para cada
#letra, sendo o nome da variavel que define cada caractere em texto
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    #Ao sair do For, executa
    #Pode sair do laço sem entrar, em caso de texto = "" (vazio)
    print(" ")
    print("Opção Else - Saída do laço sem entrar!")

#Mais um exemplo de for
for numero in range(0,10):
    print(numero, end=" ")

#Mais um exemplo de for com steps (pulando de dois em dois)
#step é o último argumento
for numero in range(0,10,2):
    print(numero, end=" ")  


print()
print() 

opcao = -1
while opcao != 0:
    opcao = int(input("Escolhe entre: \n[0] - Sair\n[1] - Sacar \n[2] - Depositar \n"))

    if opcao == 1:
        print("Realizando saque...")
    elif opcao == 2:
        print("Realizando deposito...")
    else:
        print("Saindo...")

