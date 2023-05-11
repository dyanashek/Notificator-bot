import telebot
import logging
import inspect

import config


logging.basicConfig(level=logging.INFO, 
                    filename="py_log.log", 
                    filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    )

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Handles text messages and analyzes if there are keywords.
    Deletes the message and inform manager if there are.
    """

    for keyword in config.keywords:

        if keyword in message.text:
            chat_title = message.chat.title
            logging.info(f'{inspect.currentframe().f_code.co_name}: Ключевое слово {keyword} в "{chat_title}".')

            try:
                bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            except:
                logging.error(f'{inspect.currentframe().f_code.co_name}: Нет прав для удаления сообщений.')

            try:
                url = bot.export_chat_invite_link(message.chat.id)
            except:
                url = 'не удалось определить ссылку.'

            reply_text = f'Ситуация - {config.keywords[keyword]}. {url}'

            try:
                bot.send_message(chat_id=config.DIRECTOR_ID,
                                 text=reply_text,
                                 )
                bot.send_message(chat_id=config.DIRECTOR_ID,
                                 text=message.chat.title,
                                 )
                logging.info(f'{inspect.currentframe().f_code.co_name}: Менеджер уведомлен {config.keywords[keyword]} в "{chat_title}".')

            except Exception as ex:
                logging.error(f'{inspect.currentframe().f_code.co_name}: Уведомление не доставлено {config.keywords[keyword]} в "{chat_title}". {ex}')

if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except:
            pass
                
