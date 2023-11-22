def menu_Food(menu_pizza_cout, menu_pizza):
    print("Наше меню напитков:")
    for i in range(len(menu_Beverages_)):
        print(f"{i + 1} | {menu_pizza[i + 1]}, цена {menu_pizza_cout[menu_pizza[i + 1]]}")


def menu_Beverages(menu_Beverages_cout, menu_Beverages_):
    print("Наше меню напитков:")
    for i in range(len(menu_Beverages_)):
        print(f"{i + 1} | {menu_Beverages_[i + 1]}, цена {menu_Beverages_cout[menu_Beverages_[i + 1]]}")


def hi(menu_pizza, menu_pizza_cout, menu_Beverages_cout, menu_Beverages_):
    name = str(input("Пожалуйста введите своё имя: "))
    print(f"Здравствуйте {name}, вас приветствует пицерия папа джонс!")
    print()
    work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)


def work(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_):
    print("Что вы хотите сделать?")
    print(f"1 - меню еды, 2 - меню напитков, 3 - корзина, 4 - оплата")
    n = int(input())

    if n == 1:
        menu_Food(menu_pizza, menu_pizza_cout)
    elif n == 2:
        menu_Beverages(menu_Beverages_cout, menu_Beverages_)
    # elif input("Что вы выбрали?") == 3:
    # elif input("Что вы выбрали?") == 4:

menu_pizza_cout = {"Пеперони": 599, "5 Сыров": 299, "С грушей и голубым сыром": 549, "Сливочная с креветками": 599,
                   "Томатная с креветками": 599, "Пепперони Грин": 399, "Гавайская": 299}
menu_pizza = {1: "Пеперони", 2: "5 Сыров", 3: "С грушей и голубым сыром", 4: "Сливочная с креветками",
              5: "Томатная с креветками", 6: "Пепперони Грин", 7: "Гавайская"}
menu_Beverages_cout = {"Кола": 100, "Виски": 299, "Гинтвейн": 599, "Водка": 599, "Чай с грибочками": 250, "Кофе": 39,
                       "Лате на кокосовом с мятным сиропом": 299}
menu_Beverages_ = {1: "Кола", 2: "Виски", 3: "Гинтвейн", 4: "Водка", 5: "Чай с грибочками", 6: "Кофе",
                  7: "Лате на кокосовом с мятным сиропом"}

hi(menu_pizza_cout, menu_pizza, menu_Beverages_cout, menu_Beverages_)
print(menu_pizza[1])
