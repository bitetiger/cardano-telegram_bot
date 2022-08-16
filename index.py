import telegram
from blockfrost import BlockFrostApi, ApiError, ApiUrls
from dotenv import load_dotenv
import os
load_dotenv()

bot = telegram.Bot(token=os.environ.get("TOKEN"))
chat_id = 657656740

api = BlockFrostApi(
    project_id=os.environ.get("PROJECT_ID"),
    base_url=ApiUrls.mainnet.value,
)

print(api)

try:
    health = api.health()
    print(health)   
   
    account_rewards = api.account_rewards(
        stake_address=os.environ.get("STAKE_ADDRESS"),
        count=20,
    )
    print(account_rewards)
    
    
    ad = api.accounts(
        stake_address=os.environ.get("STAKE_ADDRESS"),
    )
    print(ad)
    print(ad.withdrawable_amount)
    abc = ad.withdrawable_amount
    bot.sendMessage(chat_id=os.environ.get("CHAT_ID"), text=str(abc))
    

except ApiError as e:
    print(e)



bot.sendMessage(chat_id=environ.get("CHAT_ID"), text="보낼 메세지")