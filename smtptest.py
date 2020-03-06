#!/usr/bin/env python
# encoding: utf-8
import smtplib,os,random,time
from time import strftime
import sys
from optparse import OptionParser
from colorama import init, Fore, Style
from threading import Thread

#Color script
init(autoreset=True)
HEADER = Fore.LIGHTMAGENTA_EX
OKBLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.LIGHTGREEN_EX
WARNING = Fore.LIGHTYELLOW_EX

def banner():
    print('{}         -----------------------------------  '.format(WARNING))
    print('       {1}-=[     {0}SMTP Test{1}                   ]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Contact FB: Rahman Gunawan{1}    ]=-'.format(GREEN, WARNING))
    print('       {1}-=[   {0}Created by Rahman Gunawan{1}     ]=-'.format(GREEN, WARNING))
    print('       {1}-=[        {0}Version : 3.0{1}            ]=-'.format(GREEN, WARNING))
    print('         {}-----------------------------------  '.format(WARNING))
    print('          [!] Note : domain|ip|user|pass')
    print('')
    

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

cls()
banner()
address =input('Enter Ur Email Address: ')
a = input('Enter List Smtp: ')
ob = open(a,'r')
lists = ob.readlines()
list1 = []
i = 0
for i in range(len(lists)):
    list1.append(lists[i].strip('\n'))
count = 0
for site in (list1):
    ur = site.rstrip()
    ch= ur.split('\n')[0].split('|')
    serveraddr=ch[0]
    toaddr=address
    fromaddr=ch[2]
    serverport=ch[1]
    SMTP_USER=ch[2]
    SMTP_PASS=ch[3]
    now = strftime("%Y-%m-%d %H:%M:%S")
    msg =  "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s"  % (fromaddr, toaddr, now, now)
    server = smtplib.SMTP()
    try:
        server.connect(serveraddr, serverport)
    except:
        print( "FAILED ===> "+ur)
        print ('\n')
        continue  
    server.ehlo()
    server.ehlo()
    if SMTP_USER != "": 
        try: 
            server.login(SMTP_USER, SMTP_PASS)
        except:
            print ("FAILED ===> "+ur)
            print ('\n')
            continue
    server.sendmail(fromaddr, toaddr, msg)
    print ("SUCCESS ===> "+ur+'\n') 
    zzz=open('Valid.txt','a')
    zzz.write(site+'\n')
    server.quit()
