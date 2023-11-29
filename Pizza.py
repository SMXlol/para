def end_all():
    print("До свидания, вы лучший клиент!")
    print()

def check_ofline(price):
    print("Введите сумму денег для оплаты:")
    balance = int(input())
    if balance >= price:
        print(f"Оплата прошла успешно!\nВаш чек:")
        print()
        print("_________________________________")
        print("---PAPA--DJONS---")
        print()
        for i in range(len(eat_basket)):
            print(f"{i + 1} | {menu_pizza[eat_basket[i]]}, цена {menu_pizza_cout[menu_pizza[eat_basket[i]]]}")
        for j in range(len(drinks_basket)):
            print(
                f"{i + 1 + j + 1} | {menu_Beverages_[drinks_basket[j]]}, цена {menu_Beverages_cout[menu_Beverages_[drinks_basket[j]]]}")
        print()
        print("_________________________________")
        print()
        print(f"Вся сумма к оплате: {price} рублей")
        print()
        print(f"Ваша сдача {balance-price} рублей")
        print()
        print("Возвращайтесь к нам снова!")
        print("_________________________________")
        print()
        end_all()
    else:
        print("У вас недостаточно денег!")
        print()
        end_all()

def check_online(price):
    print()
    print("_________________________________")
    print("---PAPA--DJONS---")
    print()
    for i in range(len(eat_basket)):
        print(f"{i + 1} | {menu_pizza[eat_basket[i]]}, цена {menu_pizza_cout[menu_pizza[eat_basket[i]]]}")
    for j in range(len(drinks_basket)):
        print(f"{i + 1 + j + 1} | {menu_Beverages_[drinks_basket[j]]}, цена {menu_Beverages_cout[menu_Beverages_[drinks_basket[j]]]}")
    print()
    print("_________________________________")
    print()
    print(f"Вся сумма к оплате: {price} рублей")
    print()
    print("Возвращайтесь к нам снова!")
    print()
    print("_________________________________")
    end_all()
def pay_end(price):
    print("Выберите способ оплаты:")
    print(f"0 - онлайн\n1 - оффлайн")
    choise = int(input())
    if choise == 0:
        print("Оплата завершена, вот ваш чек")
        check_online(price)
    else:
        check_ofline(price)



def payment():
    print("Ваша еда в корзине:")
    for i in range(len(eat_basket)):
        print(f"{i + 1} | {menu_pizza[eat_basket[i]]}, цена {menu_pizza_cout[menu_pizza[eat_basket[i]]]}")
    print()
    print("Ваш напитки в корзине:")
    for i in range(len(drinks_basket)):
        print(
            f"{i + 1} | {menu_Beverages_[drinks_basket[i]]}, цена {menu_Beverages_cout[menu_Beverages_[drinks_basket[i]]]}")
    print()
    price = 0
    for i in range(len(eat_basket_cot)):
        price = price + eat_basket_cot[i]
    for i in range(len(drinks_basket_cot)):
        price = price + drinks_basket_cot[i]
    print(f"Ваш заказ стоит {price} рублей")
    print()
    print("Вы хотите оплатить?")
    print("(введите 0 если нет)")
    print("(введите 1 если хотите)")
    non = int(input())
    if non == 0:
        work()
    else:
        pay_end(price)
def basket_Browse():
    print("Ваша еда в корзине:")
    for j in range(len(eat_basket)):
        print(f"{j + 1} | {menu_pizza[eat_basket[j]]}, цена {menu_pizza_cout[menu_pizza[eat_basket[j]]]}")
    print()
    print("Ваш напитки в корзине:")
    for i in range(len(drinks_basket)):
        print(f"{i + 1} | {menu_Beverages_[drinks_basket[i]]}, цена {menu_Beverages_cout[menu_Beverages_[drinks_basket[i]]]}")
    print()
    price = 0
    for i in range(len(eat_basket_cot)):
        price = price + eat_basket_cot[i]
    for i in range(len(drinks_basket_cot)):
        price = price + drinks_basket_cot[i]
    print(f"Ваш заказ стоит {price} рублей")
    print("Если вы хотите что-то удалить из корзины, то введит его номер, если хотите перестать удалять или просто не "
          "хотите удалять, то введите 0")
    print()
    print("Еда")
    b = int(input("введите номер: "))
    while b !=0:
        eat_basket.pop(b-1)
        b = int(input("введите номер: "))
    print()
    print("Напитки")
    l = int(input("введите номер: "))
    while l != 0:
        drinks_basket.pop(l - 1)
        l = int(input("введите номер: "))
    print()
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)

def basket_add(Choice):
    if Choice == 0:
        print("Что вы хотите добавть в корзину из еды?")
        print("Чтобы остановиться в выборе введите 0")
        a = int(input("Введите номер блюда: "))
        while a != 0:
            eat_basket.append(a)
            eat_basket_cot.append(menu_pizza_cout[menu_pizza[a]])
            a = int(input("Введите номер блюда: "))


    else:
        print("Что вы хотите добавть в корзину из напитков?")
        print("Чтобы остановиться в выборе введите 0")
        a = int(input("Введите номер напитка: "))
        while a != 0:
            drinks_basket.append(a)
            drinks_basket_cot.append(menu_Beverages_cout[menu_Beverages_[a]])
            a = int(input("Введите номер блюда: "))
    print()
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)


def menu_Food(menu_pizza_cout, menu_pizza):
    print("Наше меню еды:")
    for i in range(len(menu_pizza)):
        print(f"{i + 1} | {menu_pizza[i + 1]}, цена {menu_pizza_cout[menu_pizza[i + 1]]}")
    print()
    Choice = 0
    basket_add(Choice)
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)


def menu_Beverages(menu_Beverages_cout, menu_Beverages_):
    print("Наше меню напитков:")
    for i in range(len(menu_Beverages_)):
        print(f"{i + 1} | {menu_Beverages_[i + 1]}, цена {menu_Beverages_cout[menu_Beverages_[i + 1]]}")
    print()
    Choice = 1
    basket_add(Choice)
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)


def hi(menu_pizza, menu_pizza_cout, menu_Beverages_cout, menu_Beverages_):
    name = str(input("Пожалуйста введите своё имя: "))
    print(f"Здравствуйте {name}, вас приветствует пицерия папа джонс!")
    print()
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)


def work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_):
    print("Что вы хотите сделать?")
    print(f"1 - меню еды, 2 - меню напитков, 3 - корзина, 4 - оплата")
    n = int(input())
    print()

    if n == 1:
        menu_Food(menu_pizza, menu_pizza_cout)
    elif n == 2:
        menu_Beverages(menu_Beverages_cout, menu_Beverages_)
    elif n == 3:
        basket_Browse()
    elif n == 4:
        payment()


menu_pizza_cout = {"Пеперони": 599, "5 Сыров": 299, "Пицца с грушей и голубым сыром": 549,
                   "Сливочная с креветками": 599,
                   "Томатная с креветками": 599, "Пепперони Грин": 399, "Гавайская": 299}
menu_pizza = {1: "Пеперони", 2: "5 Сыров", 3: "Пицца с грушей и голубым сыром", 4: "Сливочная с креветками",
              5: "Томатная с креветками", 6: "Пепперони Грин", 7: "Гавайская"}
menu_Beverages_cout = {"Кола": 100, "Виски": 299, "Гинтвейн": 599, "Водка": 599, "Чай с грибочками": 250, "Кофе": 39,
                       "Лате на кокосовом с мятным сиропом": 299}
menu_Beverages_ = {1: "Кола", 2: "Виски", 3: "Гинтвейн", 4: "Водка", 5: "Чай с грибочками", 6: "Кофе",
                   7: "Лате на кокосовом с мятным сиропом"}
eat_basket = []
eat_basket_cot = []
drinks_basket = []
drinks_basket_cot = []

hi(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)
print(menu_pizza[1])
