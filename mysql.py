import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

host = "localhost"
port = 3306
database = "user"
username = "user"
password = 6589

conn = pymysql.connect(host='localhost', user='root',
                       password='6589', db='sys')
cur = conn.cursor()
# <user table>
# chat_id int NOT NULL // 채팅 아이디
# user_name char(20)// tele 아이디
# first_name char(20)// tele 닉네임
# languge_code char(10) // 언어
# count_request int // 요청횟수
# stake_key char(50)// wallet 주소


# cur.execute()

# /start stake key 입력
start = "insert into user values(%d, %s, %s, %s, %d, %s)"
#start_value = (chat_id, user_name, first_name, lan_code, count_request, stake_key)
start_values = (12412, 'user_name', 'first_name', 'ko', 1, 'stake_key')

cur.execute(start, start_values)

# get balance

# about wallet

# donate
