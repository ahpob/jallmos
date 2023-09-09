import requests,os
import json,schedule,time
import datetime
from discord import SyncWebhook

# token = os.environ['TELEGRAM_TOKEN']
# id = os.environ['TELEGRAM_ID']
 
# bot = telegram.Bot(token)
discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)

url = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=208654&pocCode=SC0002&scheduleNo=100001&seatGradeNo=&corpCodeNo='
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
# res = requests.get(url, headers=headers)
# main_data = res.json()['summary']

# initial = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk']),main_data))

while True:
    
    try:
        res = requests.get(url, headers=headers)
        main_data1 = res.json()['summary']
        initial = list(map(lambda x: (x['floorNo'],x['areaNo'],x['lockSeatCntlk'],x['realSeatCntlk']),main_data1))
        
        
            
        for i in range(len(main_data1)):
            lock = initial[i][2]
            real = initial[i][3]
         
         
 
            if lock >0 or real >0:
             # 현재 시간을 시분초 형식으로 얻음
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# webhook.send() 함수 호출 시 시간 정보를 문자열에 포함하여 보냄
webhook.send(f"{current_time} - {after[i]}")
         #       webhook.send(initial[i])   
           
             
             
             
#                 bot.sendMessage(chat_id=id, text=after[i])
              


        
        # if seat_before == seat_after or seat_after == 0:
        #     continue

        # else:
        #     changes = []
        #     for i in range(len(initial)):
        #         changes.append(main_data2[i]['floorNo'],main_data2[i]['areaNo'],main_data2[i]['realSeatCntlk'])

        #     bot.sendMessage(chat_id=id, text=changes)
    
    except Exception as e:
        print("error")                
