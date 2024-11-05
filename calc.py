operation = input('escolha a operação, +, -, * e /: ')

allowedOperations = ['+', '-', '*', '/']

while operation not in allowedOperations:
    print("digite uma operacao valida")
    operation = input('escolha a operação, +, -, * e /: ')

valueAmount = int(input("quantos digitos vao ter a operacao: "))

acc = float(input("digitos da operacao: "))

for _ in range (1, valueAmount):
    value = float(input("digitos da operacao: "))
    match operation:
        case '+':
            acc += value
        case '-':
            acc -= value
        case '*':
            acc *= value
        case '/':
            acc /= value
        case _:
            print('operacao invalida')

print(acc)
