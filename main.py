def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa():
    print("= RSA Алгоритм =")

    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("phi =", phi)

    while True:
        e = int(input("Введите e: "))
        if gcd(e, phi) == 1:
            break
        print("e не взаимно просто с phi! Попробуйте другое.")

    d = find_d(e, phi)
    print("Закрытый ключ (d, n):", (d, n))

    m = int(input("Введите число для шифрования (m): "))
    c = (m ** e) % n
    print("Зашифрованное сообщение:", c)

    m_decrypted = (c ** d) % n
    print("Расшифрованное сообщение:", m_decrypted)

def diff_hell():
    print("= Протокол Диффи-Хеллмана =")

    g = int(input("Введите g (основание): "))
    p = int(input("Введите p (модуль): "))
    a = int(input("Секретный ключ A: "))
    b = int(input("Секретный ключ B: "))

    A = (g ** a) % p
    B = (g ** b) % p

    print("Открытый ключ A:", A)
    print("Открытый ключ B:", B)

    Ka = (B ** a) % p
    Kb = (A ** b) % p

    print("Общий ключ (вычислен A):", Ka)
    print("Общий ключ (вычислен B):", Kb)

    if Ka == Kb:
        print("Общий секретный ключ:", Ka)
    else:
        print("Ключи не совпадают.")


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