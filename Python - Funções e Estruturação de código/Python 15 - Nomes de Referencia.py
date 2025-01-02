def somar(a, b):
    return a+b

def subtrair(a,b):
    return a-b

def realizar_op_matematica(a,b,operacao):
    resultado = operacao(a,b)
    print(f"O resultado da operação é de: {resultado}")

op = somar

realizar_op_matematica(10,5,somar)
realizar_op_matematica(10,5,subtrair)

realizar_op_matematica(10,5,op)