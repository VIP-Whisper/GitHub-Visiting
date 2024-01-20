import requests,threading
def whisper():
 while True:
  res=requests.get(f'https://api.visitorbadge.io/api/VisitorHit?user={username}&countColorcountColor&countColor=%23FF0000',headers={"Host": "api.visitorbadge.io","sec-ch-ua": "\"Not_A Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"120\", \"Google Chrome\";v\u003d\"120\"","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q\u003d0.8","sec-fetch-site": "cross-site","sec-fetch-mode": "no-cors","sec-fetch-dest": "image","referer": "https://github.com/","accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"}).text
  try:
   v=(res.split('<title>visitors: ')[1].split('<')[0])
   print(f'[+] Visitors : {v}')
  except:
   pass
username=input(f'[+] GitHub UserName : ')
td=int(input(f'[+] Threading : '))
for i in range(td):
 t = threading.Thread(target=whisper).start()