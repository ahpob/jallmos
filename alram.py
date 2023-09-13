import requests
import os
import json
import time
import datetime
from discord import SyncWebhook

discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)


url = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=208654&pocCode=SC0002&scheduleNo=100002&seatGradeNo=&corpCodeNo='

headers = {
    'Referer': 'ticket.melon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

while True:
    try:
        res = requests.get(url, headers=headers)
        main_data1 = res.json()['summary']
        initial = list(map(lambda x: (x['seatGradeName'], x['areaNo'], x['lockSeatCntlk'], x['realSeatCntlk']), main_data1))

        for i in range(len(main_data1)):
            lock = initial[i][2]
            real = initial[i][3]

            if lock > 0 or real > 0:
                current_time = datetime.datetime.now()
                adjusted_time = current_time + datetime.timedelta(hours=9)
                formatted_time = adjusted_time.strftime("%H:%M:%S")
                webhook.send(f"{formatted_time} - {initial[i]}")

        time.sleep(0.4)

    except Exception as e:
        print("error")
