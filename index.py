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

def handler(update, context):
    print(update)
    user_chat_id = update.message.chat.id
    user_first_name = update.message.chat.first_name
    user_user_name = update.message.chat.username
    
    
    print(user_chat_id)
    print(user_first_name)
    print(user_user_name)
    
    print(type(user_chat_id))
    print(type(user_first_name))
    print(type(user_user_name))

    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장
    if user_text == "about wallet": # 지갑 정보 확인
        bot.send_message(chat_id=user_chat_id,
                         text=cardano_api.ada_accounts_result,
                         parse_mode=ParseMode.HTML,
                         disable_web_page_preview=True, reply_markup=reply_kb_markup)

    elif user_text == "/start": # 처음 시작 명령어 
        result = '안녕하세요, 카르다노 wallet 관리 봇입니다. 먼저 wallet의 stake address를 등록해주세요.'
        bot.send_message(chat_id=user_chat_id, text=result,
                         reply_markup=reply_kb_markup)
        
    elif user_text == "get balance": # 지갑 자산 리스트 확인
        result = cardano_api.assets_dic
        bot.send_message(chat_id=user_chat_id, text=result,
                         reply_markup=reply_kb_markup)
        
    elif user_text == "donation": # 기부 wallet 호출
        result = "Donate ADA to support us \n＊ address : {}" .format(os.environ.get("DONATION_ADDRESS"))
        bot.send_message(chat_id=user_chat_id, text=result,
                         reply_markup=reply_kb_markup)
        
    elif user_text == "register/change wallet": # 주소 변경
        bot.send_message(
            chat_id=user_chat_id, text='stake_wallet 주소를 적어 주세요.', reply_markup=reply_kb_markup)
        
    elif user_text.startswith('stake'): # 주소 입력시 변경
        cardano_api.user_wallet = user_text
        print(user_text)
        stake_key_vals = (user_chat_id, user_user_name, user_first_name, 'ko' ,user_text)
        mysql.cur.execute(mysql.stake_key, stake_key_vals)
        mysql.conn.commit()
        mysql.conn.close()
        
        bot.send_message(chat_id=user_chat_id,
                         text='your stake_wallet : {}' .format(user_text), reply_markup=reply_kb_markup)
        

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)