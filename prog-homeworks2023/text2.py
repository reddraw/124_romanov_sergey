sentence=str(input("Введите ваш текст"))
if len(sentence)>800:
    print("Ошибка, в тексте больше 800 символов")
else:
    a=sentence.split()
    print(len(a))