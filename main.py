#Vahle v0.1
#Solar

import requests

url = ''
user = ''
passwd = ''
voucher = ''
session = requests.Session()

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://192.168.10.1:8000/',
    'Origin': 'http://192.168.10.1:8000/',
    'DNT': '1',
    'Connection': 'keep-alive'
})

responseurl = session.get(url)

login_url = responseurl.url
form_data = {
    'auth_user': user,
    'auth_pass': passwd,
    'auth_voucher': voucher,
    'redirurl': url,
    'accept': 'Weiter',
}

response1 = session.post(login_url, data=form_data)

if response1.status_code == 200 and 'Logout' not in response1.text:
    pass
else:
     while 0==0:
        response2 = session.post(login_url, data=form_data)
        if response2.status_code == 200 and 'Logout' not in response2.text:
            break
            print("login successful")
