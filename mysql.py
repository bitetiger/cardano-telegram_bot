import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root', password=os.environ.get("DB_PW"), db='telegram_user', charset='utf8')
cur = conn.cursor()
