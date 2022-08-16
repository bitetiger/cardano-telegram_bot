import telegram
from blockfrost import BlockFrostApi, ApiError, ApiUrls
from dotenv import load_dotenv
import os
load_dotenv()

bot = telegram.Bot(token=os.environ.get("TOKEN"))
chat_id = 657656740

api = BlockFrostApi(
    project_id=os.environ.get("PROJECT_ID"),  # or export environment variable BLOCKFROST_PROJECT_ID
    # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
    base_url=ApiUrls.mainnet.value,
)

print(api)

try:
    health = api.health()
    print(health)   # prints object:    HealthResponse(is_healthy=True)
   
    # https://cardano-mainnet.blockfrost.io/api/v0/accounts/{stake_address}/rewards
    account_rewards = api.account_rewards(
        stake_address='stake1uy9hdxvl76uzs4fuklvlrdwc040js5wt42dt2p6huhe409qptkur3',
        count=20,
    )
    print(account_rewards)
    
    
    ad = api.accounts(
        stake_address='stake1uy9hdxvl76uzs4fuklvlrdwc040js5wt42dt2p6huhe409qptkur3',
    )
    print(ad)
    print(ad.withdrawable_amount)
    abc = ad.withdrawable_amount
    bot.sendMessage(chat_id=os.environ.get("CHAT_ID"), text=str(abc))
    

except ApiError as e:
    print(e)



bot.sendMessage(chat_id=environ.get("CHAT_ID"), text="보낼 메세지")