def main():
    print("Выберите алгоритм:")
    print("1 - RSA")
    print("2 - Диффи-Хеллман")
    choice = input("Ваш выбор: ")

    if choice == "1":
        print("Выбран RSA")
    elif choice == "2":
        print("Выбран Диффи-Хеллман")
    else:
        print("Неверный выбор!")

main()