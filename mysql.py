import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

conn = pymysql.connect(host=os.environ.get("host"), 
                       user=os.environ.get("username"),
                       password=os.environ.get("password"),
                       port=3306,
                       db=os.environ.get("database"), 
                       )
cur = conn.cursor()
# <user table>
# chat_id int NOT NULL // 채팅 아이디
# user_name char(20)// tele 아이디
# first_name char(20)// tele 닉네임
# languge_code char(10) // 언어
# count_request int // 요청횟수
# stake_key char(50)// wallet 주소


# cur.execute()

# stake key 입력
stake_key = "insert into user (chat_id, user_name, first_name, languge_code, stake_key) values(%s, %s, %s, %s, %s)"
# cur.execute(stake_key, (3, 'dori', 'khosla', 'ko', 1, 'slakfjs'))
#start_value = (chat_id, user_name, first_name, lan_code, count_request, stake_key)
# cur.execute(start)



# get balance

# UPDATE user SET count_request = count_request + 1 WHERE chat_id = 12


# about wallet

# # donate
# conn.commit()
# conn.close()