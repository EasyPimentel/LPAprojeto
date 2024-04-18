def calcular_potencia(x, y):
    return x ** y


def solicitar_numeros():
    x = int(input("Digite o primeiro número inteiro maior que 1: "))
    y = int(input("Digite o segundo número inteiro maior que 1: "))
    return x, y


def main():
    while True:
        x, y = solicitar_numeros()

        if x <= 1 or y <= 1:
            print("Os números digitados estão incorretos. Ambos devem ser maiores do que 1.")
        else:
            resultado = calcular_potencia(x, y)
            print(f"O resultado de {x} elevado a {y} é: {resultado}")

        resposta = input("Deseja realizar um novo cálculo? (Sim/Não): ")
        if resposta.lower() != "sim":
            print("Programa encerrado.")
            break


if __name__ == "__main__":
    main()
