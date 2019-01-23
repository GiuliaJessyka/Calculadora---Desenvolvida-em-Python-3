# Calculadora em Python

print("\n******************* Python Calculator *******************")


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


def potenciacao(x, y):
    return x ** y


def resto(x, y):
    return x % y


def calculadora():

    print("\nAbaixo as opções disponíveis em nossa calculadora:\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Resto da Divisão(Mod)")

    while True:
        try:
            escolher_opcao_calculo = int(input("\nDigite a opção da operação desejada (1/2/3/4/5/6): "))
            if not 1 <= escolher_opcao_calculo <= 6:
                print("Você não digitou uma opção válida. Por favor informar uma opção entre 1 e 6")
                continue
        except ValueError:
            print("Você não digitou um número!")
            continue
        else:
            break

    while True:
        try:
            num1 = int(input("\nDigite o primeiro número: "))
        except ValueError:
            print("Você não digitou um número!")
            continue
        else:
            break

    while True:
        try:
            num2 = int(input("\nDigite o segundo número: "))
        except ValueError:
            print("Você não digitou um número!")
            continue
        else:
            break

    if escolher_opcao_calculo == 1:
        print("\n")
        print("Adição:", num1, "+", num2, "=", adicao(num1, num2))
        print("\n")

    elif escolher_opcao_calculo == 2:
        print("\n")
        print("Subtração:", num1, "-", num2, "=", subtracao(num1, num2))
        print("\n")

    elif escolher_opcao_calculo == 3:
        print("\n")
        print("Multiplicação:", num1, "*", num2, "=", multiplicacao(num1, num2))
        print("\n")

    elif escolher_opcao_calculo == 4:
        while True:
            try:
                print("\n")
                print("Divisão:", num1, "/", num2, "=", divisao(num1, num2))
                print("\n")
            except ZeroDivisionError:
                print("Não é possível divisão por zero!")
                break
            else:
                break

    elif escolher_opcao_calculo == 5:
        print("\n")
        print("Potenciação:", num1, "elevado a", num2, "=", potenciacao(num1, num2))
        print("\n")

    elif escolher_opcao_calculo == 6:
        while True:
            try:
                print("\n")
                print("Resto da divisão(mod):", num1, "/", num2, "=", resto(num1, num2), "é o resto")
                print("\n")
            except ZeroDivisionError:
                print("Não é possível divisão por zero!")
                break
            else:
                break


calculadora()


def finalizacao():

    print("Deseja realizar um novo cálculo?\n")
    print("1 - Sim")
    print("2 - Não")

    while True:
        try:
            escolher_opcao_final = int(input("\nDigite sua opção (1/2): "))
            if not 1 <= escolher_opcao_final <= 2:
                print("Você não digitou uma opção válida. Por favor informar uma opção entre 1 e 2")
                continue
        except ValueError:
            print("Você não digitou um número!")
            continue
        else:
            break

    if escolher_opcao_final == 1:
        calculadora()
        finalizacao()

    elif escolher_opcao_final == 2:
        print("Obrigada por utilizar nossa calculadora!")
        exit(0)


finalizacao()
