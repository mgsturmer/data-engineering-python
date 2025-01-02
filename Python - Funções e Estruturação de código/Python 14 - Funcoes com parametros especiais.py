#Aprendendo sobre parametros nomeados e posicionais

#Exemplo
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    #      | Posicao           |          nomeados         |
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
##
## Não posso escrever modelo="Palio", são posicionais
## criar_carro(modelo="Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
## Da erro posicional

#Mas podemos escrever
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#Os Argumentos na definição da função após a barra podem ser nomeados.

#agora se adicionarmos um asterisco na funcao todo mundo precisa ser nomeado:

def criar_carro2(*,modelo, ano, placa, marca, motor, combustivel):
    #      | Keywords only                                         |
    print(modelo, ano, placa, marca, motor, combustivel)

#Precisa chamar assim
criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
