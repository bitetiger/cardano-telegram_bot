import telegram
from telegram.ext import Updater
import cardano_api
import mysql

from telegram.ext import MessageHandler, Filters
from telegram import ParseMode
from dotenv import load_dotenv
import os
load_dotenv()

bot = telegram.Bot(token=os.environ.get("TOKEN"))
# chat_id = token=os.environ.get("CHAT_ID")

main_menu_keyboard = [[telegram.KeyboardButton('about wallet')], [telegram.KeyboardButton('get balance'), telegram.KeyboardButton('donation')], [telegram.KeyboardButton('register/change wallet')]]
reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True, one_time_keyboard=False)

updater = Updater(token=os.environ.get("TOKEN"), use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
user_stake_key = ''

def check_stake_key(chat_id):
    mysql.cur.execute(mysql.stake_key_get, chat_id)
    result = mysql.cur.fetchone()
    user_stake_key=result[0]
    return result[0]
    
def handler(update, context):
    print(update)
    user_chat_id = update.message.chat.id
    user_first_name = update.message.chat.first_name
    user_user_name = update.message.chat.username
    user_message_id = update.message.message_id
    print(user_chat_id)
    print(user_first_name)
    print(user_user_name)
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장
    
    if user_text == "/start":  # 처음 시작 명령어
            text = 'stake~로 시작하는 본인 wallet의 stake_key address를 등록해주세요.'
            bot.send_message(chat_id=user_chat_id, text=text, reply_markup=reply_kb_markup)
    
    elif user_text == "donation":  # 기부 wallet 호출
            result = "Donate ADA to support us \n＊ address : {}" .format(
            os.environ.get("DONATION_ADDRESS"))
            bot.send_message(chat_id=user_chat_id, text=result,
                         reply_markup=reply_kb_markup)

    elif user_text == "register/change wallet":  # 주소 변경
            bot.send_message(
            chat_id=user_chat_id, text='등록하거나 변경할 새 stake_wallet 주소를 주세요.', reply_markup=reply_kb_markup)
            
    elif user_text.startswith('stake'):  # 주소 입력시 변경
                cardano_api.user_wallet = user_text
                stake_key_vals = (user_chat_id, user_user_name,user_first_name, user_text, user_text)

                try:
                    mysql.cur.execute(mysql.stake_key_insert, stake_key_vals)
                    mysql.conn.commit()
                finally:
                    mysql.conn.close()

                bot.send_message(chat_id=user_chat_id,
                text='your stake_wallet : {}' .format(user_text), reply_markup=reply_kb_markup)
                print('등록 성공')
                
    else:
        try: # chat_id에 맞는 stake_key가 db에 저장되어 있는지 확인
            check_stake_key(user_chat_id)
            print('스테이크 키가 있다!!!!!!!!!')
            print(check_stake_key)
        except: # stake_key가 db에 없을 경우
            bot.send_message(chat_id=user_chat_id, text='등록하거나 변경할 새 stake_wallet 주소를 주세요.', reply_markup=reply_kb_markup)
        
        # command_insert = "insert into transaction (chat_id, user_name, stake_key, command, content) values(%s, %s, %s, %s, %s)"

        else:  # stake_Key가 db에 있을 경우
            if user_text == "about wallet":  # 지갑 정보 확인
                result = cardano_api.about_wallet(check_stake_key(user_chat_id))
                print(result)
                db_vals = (user_chat_id, user_user_name, check_stake_key(user_chat_id), 'about wallet')
                try:
                    mysql.cur.execute(mysql.command_insert, db_vals)
                    mysql.conn.commit()
                finally:
                    # mysql.conn.close()
                    bot.send_message(chat_id=user_chat_id,
                             text=result,
                             parse_mode=ParseMode.HTML,
                             disable_web_page_preview=True, reply_markup=reply_kb_markup)

            elif user_text == "get balance":  # 지갑 자산 리스트 확인
                result = cardano_api.assets(check_stake_key(user_chat_id))
                print(result)
                db_vals = (user_chat_id, user_user_name, check_stake_key(user_chat_id),'get balance')
                try:
                    mysql.cur.execute(mysql.command_insert, db_vals)
                    mysql.conn.commit()
                finally:
                    # mysql.conn.close()
                    bot.send_message(chat_id=user_chat_id, text=result,
                         reply_markup=reply_kb_markup)
                
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)