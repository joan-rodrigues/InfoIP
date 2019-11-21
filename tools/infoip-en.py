#!/bin/python3

import ipinfo
from time import sleep
import os

def main():
    os.system('clear')
    print('''\033[1m
*-------------------------------------------------------------------*
|             ___            __           ___   ____                |  
|            |_ _|  _ __    / _|   ___   |_ _| |  _ \               | 
|             | |  | \'_ \  | |_   / _ \   | |  | |_) |              |
|             | |  | | | | |  _| | (_) |  | |  |  __/               |
|            |___| |_| |_| |_|    \___/  |___| |_|                  |
|                                                                   |
|                   Welcome to InfoIP - v1.0.0                      |
|                                                                   |
|      Developed by: Joan Rodrigues - Language Python - 2019        |
|                                                                   |
|  E-mail: joanrodrigues0611@gmail.com - Telegram: @joan_rodrigues  |
|                                                                   |
|     Instagram: @joan.dev - Facebook: fb.com/joan-rodrigues        |
|                                                                   |
|                 GitHub: github.com/joan-rodrigues                 |
|                                                                   |
|                                                 God is Faithful...|
*-------------------------------------------------------------------*
\033[m''')
    ip_address = input('\n\033[1mEnter an IP address and press <ENTER>:\033[m ')

    access_token = 'd62fceaae70fb9'
    print('\n\033[1mFinding IP Information...\n')

    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)

    os.system('clear')

    print('\nInformations:\n')
    print('IP/DNS:\033[m ' + details.ip)

    try:
        print('\033[1mHostname:\033[m ' + details.hostname)
    
    except AttributeError:
        pass
    
    try:
        print('\033[1mCountry:\033[m: ' + details.country)
        print('\033[1mCity:\033[m ' + details.city)
        print('\033[1mRegion:\033[m ' + details.region)
        print('\033[1mLocation:\033[m ' + details.loc)

        print('\033[1m\n\nServer:\n')
        print('Name: \033[m ' + details.org)
        print('\033[1mPostal:\033[m ' + details.postal)
        print('\033[1mTimezone:\033[m ' + details.timezone)
        print('\033[1mCountry:\033[m ' + details.country_name)
        print('\033[1mLatitude:\033[m ' + details.latitude)
        print('\033[1mLongitude:\033[m ' + details.longitude)
        print('\n\n\033[1mBye, Bye!')
        print('\n╭∩╮( º.º )╭∩╮\033[m')
        
    except AttributeError:
        print('\n\n\n\033[1;91mSOMETHING WRONG HAPPENED !!! TRY AGAIN PLEASE.\033[m')
        sleep(6)
        main()

main()