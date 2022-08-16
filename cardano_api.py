from blockfrost import BlockFrostApi, ApiError, ApiUrls
from dotenv import load_dotenv
import os
load_dotenv()

user_wallet = ''
print(user_wallet)

api = BlockFrostApi(
    project_id=os.environ.get("PROJECT_ID"),
    base_url=ApiUrls.mainnet.value,
)

#지갑 정보
ada_accounts = api.accounts(
    stake_address=os.environ.get("STAKE_ADDRESS"),
    )
ada_amount = format(int(ada_accounts.controlled_amount) / 1000000, ',')
ada_rewards = format(int(ada_accounts.rewards_sum) / 1000000, ',')
ada_accounts_result = "＊ Stake_address: <a href='https://cardanoscan.io/stakekey/{stake_key}'>{stake_key}</a> \n＊ ADA_amount: {amount} \n＊ ADA_staking_rewards: {rewards} \n＊ Pool_id: <a href='https://cardanoscan.io/pool/{pool}'>{pool}</a> \n" .format(stake_key = ada_accounts.stake_address, amount = ada_amount, rewards = ada_rewards, pool = ada_accounts.pool_id)
print(ada_accounts)


#지갑 자산 리스트
ada_addresses_assets = api.account_addresses_assets(
    stake_address=os.environ.get("STAKE_ADDRESS"),
)
print(ada_addresses_assets)

# ada_addresses_total = api.account_addresses_total(
#     stake_address=os.environ.get("STAKE_ADDRESS"),
# )
# print(ada_addresses_total)
str1 = "stake1uy9hdxvl76uzs4fuklvlrdwc040js5wt42dt2p6huhe409qptkur3"
print(str1.startswith('stake'))
