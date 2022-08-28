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

# INSERT IGNORE INTO 'table name' (column1, column2)
# VALUES (11, 13)

# cur.execute()

# stake key 입력
stake_key = "insert into user (chat_id, user_name, first_name, languge_code, stake_key) values(%s, %s, %s, %s, %s)"

# get balance

# UPDATE user SET count_request = count_request + 1 WHERE chat_id = 12


# about wallet

# # donate
# conn.commit()
# conn.close()