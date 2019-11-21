#!/bin/python3

import os
from time import sleep

def error():
    print('\n\n\033[1;91mINVALID OPTION!!! TRY AGAIN.\033[m')
    sleep(4)
    main()

def main():
    os.system('clear')
    if os.path.isfile('tools/temp/1'):
        os.system('tools/infoip-pt.py')

    elif os.path.isfile('tools/temp/2'):
        os.system('tools/infoip-en.py')

    else:
        print('''\n\033[1m

                                 ┌─┐　─┐
   　                            │▒│ /▒/
 _   _          _   _  　        │▒│/▒/
| | | |   ___  | | | |   ___   　│▒ /▒/─┬─┐
| |_| |  / _ \ | | | |  / _ \  　│▒│▒|▒│▒│
|  _  | |  __/ | | | | | (_) |   ┌┴─┴─┐-┘─┘
|_| |_|  \___| |_| |_|  \___/    │▒┌──┘▒▒▒│
                                 └┐▒▒▒▒▒▒┌┘
                                 　└┐▒▒▒▒┌┘

        \n''')
        print('1 - English\n2 - Portuguese')
        language = int(input('\n\nSelect the language:\033[m '))

        if language == 1:
            en = open('tools/temp/2', 'w')
            en.write('en-us')
            en.close()
            os.system('tools/infoip-en.py')

        elif language == 2:
            pt = open('tools/temp/1', 'w')
            pt.write('pt-br')
            pt.close()
            os.system('tools/infoip-pt.py')

        else:
            error()
main()