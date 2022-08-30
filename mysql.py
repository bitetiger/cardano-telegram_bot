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
# cur.execute()

# /start
# wallet이 등록되어 있는지 확인하기
stake_key_get = "select stake_key from user where chat_id = %s"


# register/change wallet 
# stake key 등록 및 변경하기
stake_key_insert = "insert into user (chat_id, user_name, first_name, stake_key) values(%s, %s, %s, %s) ON DUPLICATE KEY UPDATE stake_key = %s"


# - chat_id int NOT NULL
# - user_name char(20)
# - stake_key char(100)
# - command char(30) // 요청 명령어
# - content varchar(400)

# get balance & about wallet
command_insert = "insert into transaction (chat_id, user_name, stake_key, command) values(%s, %s, %s, %s)"

# UPDATE user SET count_request = count_request + 1 WHERE chat_id = 12



# # donate
# conn.commit()
# conn.close()