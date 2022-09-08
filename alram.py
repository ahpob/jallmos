import requests,os
import json,schedule,time
from discord import SyncWebhook

# token = os.environ['TELEGRAM_TOKEN']
# id = os.environ['TELEGRAM_ID']
 
# bot = telegram.Bot(token)
discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)

url = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=207126&pocCode=SC0002&scheduleNo=100001&seatGradeNo=&corpCodeNo='
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
res = requests.get(url, headers=headers)
main_data = res.json()['summary']

initial = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk']),main_data))

while True:
    
    try:
        res = requests.get(url, headers=headers)
        main_data1 = res.json()['summary']
        initial = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk'],x['seatGradeName']),main_data1))
        third_floora = list(map(lambda x: (x['seatGradeName']),main_data1))
        
        time.sleep(0.4)

        res = requests.get(url, headers=headers)
        main_data2 = res.json()['summary']
        after = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk'],x['seatGradeName']),main_data2))
        third_floorb = list(map(lambda x: (x['seatGradeName']),main_data2))
        
            
        for i in range(len(main_data2)):
            seat_before = initial[i][2]
            seat_after = after[i][2]
            third_floor1 = third_floora[i]
            third_floor2 = third_floorb[i]
           

            if seat_before == seat_after and third_floor1 == third_floor2:
                continue
            elif seat_after == 0:
                continue
            else:
                webhook.send(after[i])
             
             
             
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
