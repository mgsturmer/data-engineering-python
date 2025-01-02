#Estruturando o código atráves de funções

#Segue uma estrutura identada semelhante aos ifs e fors já estudados

def exibir_ola_mundo():
        print("Olá mundo!")

def exibir_mensagem(mensagem = "Nenhuma mensagem"):
        print(f"A sua mensagem é: {mensagem}")

#Define um valor padrão para o argumento caso não for passado um nome.
def exibir_nome(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}")


exibir_ola_mundo
exibir_mensagem("Aprendendo funcoes em Python")
exibir_nome("Matheus")
exibir_nome()

#Funções com retorno:
def soma(numeros):
    return sum(numeros)

print(soma([4,5,6]))

#Retornando mais de um valor:
def retorna_antecessor_e_suicessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

antecessor, sucessor = retorna_antecessor_e_suicessor(5)
print(antecessor)
print(sucessor)

#Agora com argumentos nomeados:
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! \n{marca} \n{modelo} \n{ano} \n{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

salvar_carro(modelo="Ka", marca="Ford", ano=2015, placa="DCE-4321")

#Funções com #args e ##kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-feira, 03 de Setembro de 2024","Zen of Python", "Beatifull is better than ugly", autor="Tim Peters", ano=1999)

