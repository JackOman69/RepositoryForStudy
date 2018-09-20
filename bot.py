import telebot
import os
import urllib.request as urllib2
import consts

bot = telebot.TeleBot(consts.token)

@bot.message_handler(commands=["start"])
def handle_start(message):

		user_markup = telebot.types.ReplyKeyboardMarkup(True) 
		user_markup.row('/start', '/stop')
		user_markup.row('Фото', 'Аудио', 'Документы')
		user_markup.row('Стикер', 'Видео', 'Голос', 'Локации')
		bot.send_message(message.from_user.id, "Добро пожаловать...", reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):

		hide_markup = telebot.types.ReplyKeyboardRemove()
		bot.send_message(message.from_user.id, "До встречи!", reply_markup = hide_markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):

		if message.text == "Фото":
				url = "https://habrastorage.org/storage2/145/277/c3e/145277c3ef9795a38135b6718eb7169c.png"
				urllib2.urlretrieve(url, "image.jpg")
				img = open("image.jpg", "rb")
				bot.send_chat_action(message.from_user.id, "upload_photo")
				bot.send_photo(message.from_user.id, img)
				img.close()
		elif message.text == "Аудио":
				audio = open("C:/Users/Public/Music/Sample Music/Kalimba.mp3", "rb")
				bot.send_chat_action(message.from_user.id, "upload_audio")
				bot.send_audio(message.from_user.id, audio)
				audio.close()



bot.polling(none_stop=True)


































# @bot.message_handler(content_types = ["text"])
# def handle_text(message):
# 		if message.text == "Привет!":
# 				bot.send_message(message.from_user.id, "Здравствуй!")
# 		elif message.text == "Пока":
# 				bot.send_message(message.from_user.id, "Ну пока :c")		
# 		else:
# 				bot.send_message(message.from_user.id, "Попробуй еще раз!")


#upd = bot.get_updates()
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)
