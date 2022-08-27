# cardano-telegram_bot

## description
- Cardano wallet을 확인할 수 있는 텔레그램 봇
- 특정 지갑의 자산과 Pool, 스테이킹 수익을 모두 확인가능 
## usage
- ![image](https://user-images.githubusercontent.com/89952061/185416915-9ae10b8b-a462-4146-8500-214411242038.png)
- about wallet : wallet에 들어있는 ADA 수량과 스테이킹 수익 및 Pool id 확인
- get balance  : wallet의 전체(NFT, ADA, 기타 토큰)을 확인
- donation : 봇 개발자 기부
- register/chage wallet : wallet 등록 및 변경

## telegram bot webhook
### telegram bot webhook 연결   
![image](https://user-images.githubusercontent.com/89952061/187029716-56d66ac9-2b45-4720-99b4-5e157ffefa2c.png)
- https://api.telegram.org/bot${telegram_token}/setWebhook?url=${callback_url}   
telegram_token = 봇 token   
callback_url = lambda API url
- 연결 성공시 응답   
![image](https://user-images.githubusercontent.com/89952061/187029740-6210d934-f03d-467e-8d96-5b8186aa9d5a.png)

### telegram bot webhook 해제   
https://api.telegram.org/bot${telegram_token}/setWebhook?url=
url만 제거 시 webhook 해제
