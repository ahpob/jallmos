import requests,os
import json,telegram,schedule,time

token = os.environ['TELEGRAM_TOKEN']
id = os.environ['TELEGRAM_ID']
 
bot = telegram.Bot(token)
url = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=207212&pocCode=SC0002&scheduleNo=100004&seatGradeNo=&corpCodeNo='
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
res = requests.get(url, headers=headers)
main_data = res.json()['summary']

initial = list(map(lambda x: (x['rank'],x['keyword']),main_data))
floorNo = main_data['floorNo']

while True:
    
    try:
        res = requests.get(url, headers=headers)
        main_data1 = res.json()['summary']
        initial = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk']),main_data1))

        time.sleep(0.5)

        res = requests.get(url, headers=headers)
        main_data2 = res.json()['summary']
        after = list(map(lambda x: (x['floorNo'],x['areaNo'],x['realSeatCntlk']),main_data2))
        
        changes = []
        for i in range(len(initial)):
            seat_before = initial[i][2]
            seat_after = after[i][2]
            
            if seat_before != seat_after:
                changes.append(after[i])
        bot.sendMessage(chat_id=id, text=changes)
    
    except Exception as e:
        print("error")                

