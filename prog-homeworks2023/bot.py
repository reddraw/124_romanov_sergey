import telebot
import random
bot=telebot.TeleBot(input("Введите токен вашего бота"))
@bot.message_handler(commands=['start'])
def start(start):
    imya=start.from_user.username
    bot.send_message(start.chat.id, "Здравствуйте "+str(imya)+", я загадал число, введите ваш вариант. ")
    chislo=random.randint(1,101)
    counter=0
    def igra():
        @bot.message_handler(content_types=["text"])
        def proverka(message):
            nonlocal chislo
            nonlocal counter
            nonlocal imya
            try:
                variant = int(message.text)
            except ValueError:
                bot.send_message(message.chat.id, 'Вы ввели некорректное значение числа')
                igra()
                return 0
            if variant > 101 or variant < 1:
                bot.send_message(message.chat.id, 'Вы ввели некорректное значение числа')
                igra()
                return 0
            elif variant > chislo:
                bot.send_message(message.chat.id, 'Ваше число больше загаданного')
                counter += 1
                igra()
                return 0
            elif variant < chislo:
                bot.send_message(message.chat.id, 'Ваше число меньше загаданного')
                counter += 1
                igra()
                return 0
            else:
                counter += 1
                bot.send_message(message.chat.id, 'Поздравляю, '+ str(imya)+' вы угадали за ' + str(counter) + ' попыток')
                chislo = random.randint(1, 101)
                counter = 0

    igra()



bot.polling()


