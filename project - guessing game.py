from random import randint

print("Добро пожаловать в числовую угадайку!")

def is_valid(m):
    while not m.isdigit() or int(m) > 100:
        print("А может быть все-таки введем целое число от 1 до 100?")
        m = input()
    return [True, int(m)]

def main():
    print("Введите число от 1 до 100")
    n = randint(1, 100)
    m = input()
    cnt = 1
    l = is_valid(m)
    if l[0]:
        m = l[1]
        while int(m) != n:
            cnt += 1
            if int(m) > n:
                print("Ваше число больше загаданного, попробуйте еще разок")
                m = input()
                if not is_valid(m)[0]:
                    m = l[1]
            elif int(m) < n:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                m = input()
                if not is_valid(m)[0]:
                    m = l[1]
    print("Вы угадали, поздравляем! Количество попыток:", cnt)        
    print("Спасибо, что играли в числовую угадайку. Еще увидимся... Хотите сыграть снова?")


main()

while input() == "Да":
    main()
print("Хорошо, спасибо за участие!")