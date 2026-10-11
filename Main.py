import telebot
from telebot import types  # Импортируем типы для создания кнопок
from botlogic import gen_pass, gen_emodji, flip_coin, gen_guess

bot = telebot.TeleBot("8843433411:AAHWDmRkJCKADNVeupwPxCWBxzwDqmyhGhI")

# 1. Главное меню при старте бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру, resize_keyboard=True делает кнопки аккуратными
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Создаем кнопки меню
    btn_hello = types.KeyboardButton("👋 Привет")
    btn_pass = types.KeyboardButton("🔑 Сгенерировать пароль")
    btn_emodji = types.KeyboardButton("😊 Рандомный смайлик")
    btn_coin = types.KeyboardButton("🪙 Подбросить монетку")
    btn_guess = types.KeyboardButton("🎲 Угадай число")
    btn_bye = types.KeyboardButton("🚪 Пока")
    
    # Добавляем кнопки в меню
    markup.add(btn_hello, btn_pass, btn_emodji, btn_coin, btn_guess, btn_bye)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Я твой Telegram бот. Выбери нужное действие в меню ниже или используй команды!", 
        reply_markup=markup
    )

# Оставляем поддержку старых текстовых команд на случай, если пользователь введет их руками
@bot.message_handler(commands=['hello'])
def cmd_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def cmd_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def cmd_password(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def cmd_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи: {emodji}")

@bot.message_handler(commands=['coin'])
def cmd_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['guess'])
def cmd_guess(message):
    number = gen_guess()
    bot.reply_to(message, f"Число было такое: {number}")

# 2. Обработка нажатий на кнопки меню (текстовые сообщения)
@bot.message_handler(content_types=['text'])
def handle_menu_buttons(message):
    if message.text == "👋 Привет":
        bot.reply_to(message, "Привет! Как дела?")
        
    elif message.text == "🔑 Сгенерировать пароль":
        password = gen_pass(10)
        bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")
        
    elif message.text == "😊 Рандомный смайлик":
        emodji = gen_emodji()
        bot.reply_to(message, f"Вот эмоджи: {emodji}")
        
    elif message.text == "🪙 Подбросить монетку":
        coin = flip_coin()
        bot.reply_to(message, f"Монетка выпала так: {coin}")
        
    elif message.text == "🎲 Угадай число":
        number = gen_guess()
        bot.reply_to(message, f"Результат игры: {number}")
        
    elif message.text == "🚪 Пока":
        bot.reply_to(message, "Пока! Удачи!")
        
    else:
        bot.reply_to(message, "Я не знаю такой команды. Пожалуйста, используйте кнопки меню.")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
