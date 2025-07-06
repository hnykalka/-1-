def rsa():
    print("= RSA Алгоритм =")
    # заглушка

def diff_hell():
    print("= Протокол Диффи-Хеллмана =")
    # заглушка

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