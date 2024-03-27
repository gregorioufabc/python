def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

print("Selecione a operação desejada:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))

elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif escolha == '4':
    try:
        print(num1, "/", num2, "=", divisao(num1, num2))
    except ValueError as e:
        print(e)
else:
    print("Opção inválida")
