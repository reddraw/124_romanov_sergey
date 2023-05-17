import telebot
import random
bot=telebot.TeleBot(input("Введите токен вашего бота"))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет, поиграем в игру? Сейчас я загадаю число, вам надо угадать" )
    chislo=random.randint(1, 101)
    count=0
    bot.send_message(start.chat.id, "Угадайте число!")
    def igra():
        @bot.message_handler(content_types=["text"])
        def check_chislo(message):
            bot.send_message(message.chat.id, "Введите число")
            if variant != chislo:
                if variant > chislo:
                    bot.send_message(message.chat.id, "Ваше число больше задуманного")
                    count += 1
                    check_chislo()
                else:
                    bot.send_message(message.chat.id, "Ваше число меньше задуманного")
                    count += 1
                    check_chislo()
            else:
                count += 1
                bot.send_message(message.chat.id, "Поздравляю, вы выиграли за " + str(count) + "попыток/ки")
                start()

        check_chislo()
    igra()



bot.polling()

