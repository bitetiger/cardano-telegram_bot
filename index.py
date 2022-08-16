import telegram
from telegram.ext import Updater
import cardano_api
import json

from telegram.ext import MessageHandler, Filters
from telegram import ParseMode
from dotenv import load_dotenv
import os
load_dotenv()

bot = telegram.Bot(token=os.environ.get("TOKEN"))
chat_id = token=os.environ.get("CHAT_ID")

main_menu_keyboard = [[telegram.KeyboardButton('about wallet')], [telegram.KeyboardButton('get balance'), telegram.KeyboardButton('donation')], [telegram.KeyboardButton('register/change wallet')]]
reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True, one_time_keyboard=False)
bot.sendMessage(chat_id=os.environ.get("CHAT_ID"), text="명령어 입력해주세요", reply_markup=reply_kb_markup)

updater = Updater(token=os.environ.get("TOKEN"), use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장
    if user_text == "about wallet": # 지갑 정보 확인
        bot.send_message(chat_id=os.environ.get("CHAT_ID"), 
                         text=cardano_api.ada_accounts_result,
                         parse_mode=ParseMode.HTML,
                         disable_web_page_preview=True) # 답장 보내기
        
    elif user_text == "get balance": # 지갑의 assets 확인
        result = json.dumps(cardano_api.ada_addresses_assets)
        bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=result) # 답장 보내기
        
    elif user_text == "donation": # 사용자가 보낸 메세지가 "뭐해"면?
        result = "Donate ADA to support us \n＊ address : {}" .format(os.environ.get("DONATION_ADDRESS"))
        bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=result) # 답장 보내기
        
    elif user_text == "register/change wallet": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='stake_wallet 주소를 적어 주세요.') # 답장 보내기
        
    elif user_text.startswith('stake'):
        cardano_api.user_wallet = user_text
        bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='your stake_wallet : {}' .format(user_text))
        
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

# # first_name으로 사용자 확인가능
# updates = bot.getUpdates()
# for u in updates:
#     print(u.message)
    
