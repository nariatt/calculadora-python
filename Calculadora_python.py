# Operações da calc.

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def RaizQuadrada(x):
    return x ** (1/2)

print("Selecione a operação.")
print("1: somar")
print("2: subtrair")
print('3: multiplicar')
print("4: dividir")
print("5: raiz")

while True:
    escolha = input("Escolha uma das cinco operações: ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        if escolha == '1':
            print(num1, '+', num2, '=', somar(num1, num2))
        elif escolha == '2':
            print(num1, '-', num2, '=', subtrair(num1, num2))
        elif escolha == '3':
            print(num1, '*', num2, '=', multiplicar(num1, num2))
        elif escolha == '4':
            print(num1, '/', num2, '=', dividir(num1, num2))

        próximo_cálculo = input("Quer fazer outro cálculo? ")
        if próximo_cálculo == 'não':
            break
    elif escolha in ('5'):
        try:
            num1 = float(input("Digite seu número: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        if escolha == '5':
            print(num1, '**', '1/2', '=', RaizQuadrada(num1))

    else:
        print("Valor inválido")