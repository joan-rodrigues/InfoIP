#!/bin/python3

import ipinfo
from time import sleep
import os

def main():
    os.system('clear')
    print('''\033[1m
*-------------------------------------------------------------------*
|            ___            __           ___   ____                 |  
|           |_ _|  _ __    / _|   ___   |_ _| |  _ \                | 
|            | |  | \'_ \  | |_   / _ \   | |  | |_) |               |
|            | |  | | | | |  _| | (_) |  | |  |  __/                |
|           |___| |_| |_| |_|    \___/  |___| |_|                   |
|                                                                   |
|                  Bem-vindo ao InfoIP - v2.0.0                     |
|                                                                   |
|      Developed by: Joan Rodrigues - Language Python - 2020        |
|                                                                   |
|  E-mail: joanrodrigues0611@gmail.com - Telegram: @joan_rodrigues  |
|                                                                   |
|     Instagram: @joan.dev - Facebook: fb.com/joanrodrigue0611      |
|                                                                   |
|               GitHub: github.com/joan-rodrigues                   |
|                                                                   |
|                                                     Deus é Fiel...|
*-------------------------------------------------------------------*
\033[m''')
    ip_address = input('\n\033[1mDigite um endereço IP e pressione <ENTER>:\033[m ')
    access_token = 'd62fceaae70fb9'
    
    print('\n\033[1mDescobrindo informações sobre o IP...\n')

    os.system('ping -b -c 1 %s | grep -E -B1 "[1-9][0-9]{1,3}\." | cut -d"(" -f2 | cut -d")" -f1 | sed -n "1p" > temp/ip' %ip_address)
    ip_file = open('temp/ip', 'r')
    ip_end = ip_file.read()
    ip_file.close()
    
    print('IP/DNS: ' + ip_end)

    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_end)

    os.system('clear')

    print('\nInformações:\n')
    print('IP/DNS:\033[m ' + details.ip)

    try:
        print('\033[1mHostname:\033[m ' + details.hostname)
    
    except AttributeError:
        pass
    
    try:
        print('\033[1mPaís\033[m: ' + details.country)
        print('\033[1mCidade:\033[m ' + details.city)
        print('\033[1mRegião:\033[m ' + details.region)
        print('\033[1mLocalização:\033[m ' + details.loc)

        print('\033[1m\n\nServidor:\n')
        print('Nome: \033[m ' + details.org)
        print('\033[1mPostal:\033[m ' + details.postal)
        print('\033[1mTimezone:\033[m ' + details.timezone)
        print('\033[1mPaís:\033[m ' + details.country_name)
        print('\033[1mLatitude:\033[m ' + details.latitude)
        print('\n\n\033[1mBye, Bye!')
        print('\n╭∩╮( º.º )╭∩╮\033[m')

    except AttributeError:
        print('\n\n\n\033[1;91mALGO DE ERRADO ACONTECEU!!! TENTE NOVAMENTE POR FAVOR.\033[m')
        sleep(6)
        main()

main()
