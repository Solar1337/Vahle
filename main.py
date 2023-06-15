#Vahle v0.2
#Solar

import os, requests

def start():
    if os.path.exists('config.py') == True:
        main()
    else:
        url = input("IP: ")
        if url == "":
            print("You have to set a Server IP-Address.")
            start()
        else:
            pass
        f = open("config.py", "w+")
        f.write("url = 'http://" + url + "'\n")
        user = input("Username (leave blank if not present): ")
        f.write("user = '" + user + "'\n")
        passwd = input("Password (leave blank if not present): ")
        f.write("passwd = '" + passwd + "'\n")
        voucher = input("Voucher (leave blank if not present): ")
        f.write("voucher = '" + voucher + "'")
        f.close()
        main()

def main():
    from config import url, user, passwd, voucher
    session = requests.Session()

    session.headers.update({
        'User-Agent':      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept':          '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"',
        'Accept-Language': 'en-US',
        'Accept-Encoding': 'gzip, deflate',
        'Referer':         url,
        'Origin':          url,
        'DNT':             '1',
        'Connection':      'keep-alive'
    })

    responseurl = session.get(url)
    print(responseurl)

    login_url = responseurl.url
    form_data = {
        'auth_user':    user,
        'auth_pass':    passwd,
        'auth_voucher': voucher,
        'redirurl':     url,
        'accept':       'Weiter',
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

start()
