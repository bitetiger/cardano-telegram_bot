# cardano-telegram_bot

## description
- Cardano wallet을 확인할 수 있는 텔레그램 봇
- 특정 지갑의 자산과 Pool, 스테이킹 수익을 모두 확인가능

## Structure
![image](https://user-images.githubusercontent.com/89952061/187059030-4b1b16f6-dd7f-49e3-a227-771d9910fec3.png)   
1) Updater는 사용자로부터 새로운 메시지가 왔는지를 주기적으로 확인(Polling)한다.  
2) 사용자로부터 어떤 명령어나 메시지가 왔다면 이를 Queue에 저장한 후, Dispatcher는 Update가 Queue에 넣어둔 사용자의 명령이나 메시지를 가져가서 처리한다.    
3)  이때 각 요청에 대한 처리를 담당할 핸들러(Handler) 객체를 미리 지정해두고 요청이 들어오면 지정된 핸들러를 통해 처리한다.   

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

## MySQL Database
### default
- database : cardano_bot
- table : user(봇 사용자), transaction(봇 사용자 트랜잭션)
```
$ create user 'userID'@'%' identified by 'passwd';

$ grant all privileges on *.* to 'userID'@'%';
// admin 접속 (sudo mysql -u userID -p 'passwd')

$ create database cardano_bot;

$ use cardano_bot;

$ create table user(
    chat_id int NOT NULL,   
    user_name char(20),   
    first_name char(20),  
    languge_code char(10), 
    count_request int, 
    stake_key char(50),
    primary key(chat_id)
);

$ create table transaction(
    chat_id int NOT NULL,
    user_name char(20),
    stake_key char(50),
    command char(30)
);

```
### user table
- chat_id int NOT NULL // 채팅방 아이디   
- user_name char(20) // telegram 아이디   
- first_name char(20) // telegram 닉네임   
- languge_code char(10) // 언어  
- count_request int // 요청 횟수   
- stake_key char(50) // wallet 주소  

### transaction table
- chat_id int NOT NULL
- user_name char(20)
- stake_key char(50)
- command char(30) // 요청 명령어

## Environmnet
PROJECT_ID= // blockfrost project id
STAKE_ADDRESS= // test용 stake address
TOKEN= // telegram bot token
DONATION_ADDRESS= // donation address

host= // db host url
port=  // db port, 3006
database= // dbname
username= // username
password=  // password
