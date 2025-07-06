def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rsa():
    print("=== RSA Алгоритм ===")

    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("phi =", phi)

    while True:
        e = int(input("Введите e (взаимно просто с phi): "))
        if gcd(e, phi) == 1:
            break
        print("e не взаимно просто с phi! Попробуйте другое.")

    print("Открытый ключ (e, n):", (e, n))

def diff_hell():
    print("= Протокол Диффи-Хеллмана =")
    # заглушка

def rsa():
    print("=== RSA Алгоритм ===")

    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("phi =", phi)

def main():
    print("Выберите алгоритм:")
    print("1 - RSA")
    print("2 - Диффи-Хеллман")
    choice = input("Ваш выбор: ")

    if choice == "1":
        rsa()
    elif choice == "2":
        diff_hell()
    else:
        print("Неверный выбор :(")

main()