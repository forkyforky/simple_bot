import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(update: Updater, context: CallbackContext):
	print(update)
	mytext = """Hello {}
	I have only /start command! =)""".format(update.message.chat.first_name)
	logging.info('User {} press /start'.format(update.message.chat.username))
	update.message.reply_text(mytext)

	print("Hello")

def chat(update: Updater, context: CallbackContext):
	text = update.message.text
	#записывает в логи вводимое сообщение
	logging.info(text)

	update.message.reply_text(text)


def main():
	updtr = Updater(settings.TOKEN_TELEGRAMM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	#отвечает вводимым текстом
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == '__main__':
	logging.info('Bot started')
	main()