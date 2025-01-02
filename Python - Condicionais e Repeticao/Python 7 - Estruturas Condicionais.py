#Estruturas condicionais e Python

#estruturas condicionais são comandos que desviam o fluxo de controle
#de acordo com determinadas expressões lógicas.

idade = int(input("Informe a sua idade: "))
            
MAIORIDADE = 18

if(idade > MAIORIDADE):
    print("Você já pode tirar habilitação.")
elif(idade == MAIORIDADE): 
    print("Você tem exatamente 18 anos. Parabéns pela maioridade, você já pode tirar habilitação")
else:
    print("Você ainda é menor idade e não pode tirar Habilitação")




