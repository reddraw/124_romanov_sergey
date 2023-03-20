spisok=["Мавпродош".casefold(), "Лорнектиф".casefold(), "Древерол".casefold(), "Фиригарпиг".casefold(), "Клодобродыч".casefold()]
a=input("Введите свой ник")
if a.casefold() in spisok:
    print("Ты – свой. Приветствую, любезный", a)
else:
    print("Тут ничего нет. Еще есть вопросы?")