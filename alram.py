import requests,os
import json,schedule,time
import datetime
from discord import SyncWebhook

discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)
current_time = datetime.datetime.now()
adjusted_time = current_time + datetime.timedelta(hours=9)
formatted_time = adjusted_time.strftime("%H:%M:%S")
                
url1 = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=207126&pocCode=SC0002&scheduleNo=100001&seatGradeNo=&corpCodeNo='
url2 = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=207126&pocCode=SC0002&scheduleNo=100002&seatGradeNo=&corpCodeNo='
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
res1 = requests.get(url1, headers=headers)
main_data1 = res1.json()['summary']
initial1 = list(map(lambda x: (x['areaNo'],x['lockSeatCntlk'],x['realSeatCntlk']),main_data1))
time.sleep(0.3)
res2 = requests.get(url2, headers=headers)
main_data2 = res2.json()['summary']
initial2 = list(map(lambda x: (x['areaNo'],x['lockSeatCntlk'],x['realSeatCntlk']),main_data2))

while true:
    if initial1 == initial2 :
        continue
    else
        after = list(set(initial2)-set(initial1))
        webhook.send(f"{formatted_time} - {after}")
