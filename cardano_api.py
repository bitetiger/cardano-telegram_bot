from blockfrost import BlockFrostApi, ApiError, ApiUrls
from dotenv import load_dotenv
import os
import index
load_dotenv()

api = BlockFrostApi(
    project_id=os.environ.get("PROJECT_ID"),
    base_url=ApiUrls.mainnet.value,
)

# about wallet 지갑 정보를 위한
def about_wallet():
    ada_accounts = api.accounts(
    stake_address=index.user_stake_key)
    ada_amount = format(int(ada_accounts.controlled_amount) / 1000000, ',')
    ada_rewards = format(int(ada_accounts.rewards_sum) / 1000000, ',')
    ada_accounts_result = "＊ Stake_address: <a href='https://cardanoscan.io/stakekey/{stake_key}'>{stake_key}</a> \n＊ ADA_amount: {amount} \n＊ ADA_staking_rewards: {rewards} \n＊ Pool_id: <a href='https://cardanoscan.io/pool/{pool}'>{pool}</a> \n" .format(
        stake_key=ada_accounts.stake_address, amount=ada_amount, rewards=ada_rewards, pool=ada_accounts.pool_id)
    return ada_accounts_result

# get balance 지갑 자산 리스트
def get_balance():
    ada_addresses_assets = api.account_addresses_assets(
        stake_address=index.user_stake_key,
    )
    return ada_addresses_assets

# addresses_assets 지갑 자산 리스트
def assets():
    assets_dic = {}

    for asset in get_balance():
        # print(asset.unit)
        # print(asset.quantity)
        assets_dic[asset.unit]= asset.quantity
    return assets_dic
