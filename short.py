import os
import random
from time import time

# import replit
# import keyboard
import keyboard
from hgtk.text import decompose
from articloid import srt, ko_srt

def hyphen(short, lan):
    global hy_len
    if lan == 'ko':
        hy_len = (len(short) * 2 - 7)
    elif lan == 'en':
        hy_len = len(short)

    for i in range(hy_len):
        print('=', end='')
    print('')


def correct(short, ipt, lan):

    cor_count = 0

    if lan == 'ko':
        sep_srt = decompose(short, compose_code='')
        sep_ipt = decompose(ipt, compose_code='')

        # print(sep_srt)

        for i in range(len(sep_srt)+1):
            if sep_srt[i:i+1] == sep_ipt[i:i+1]:
                cor_count += 1

    else:
        for i in range(len(short)):
            if short[i:i+1] == ipt[i:i+1]:
                cor_count += 1

    if lan == 'ko':
        return cor_count-1
    elif lan == 'en':
        return  cor_count

def red(short, ipt, lan):

    hyphen(short, lan)
    print(short)

    for i in range(len(short) + 1):
        if short[i:i + 1] == ipt[i:i + 1]:
            print(f"{ipt[i:i + 1]}", end='')
        else:
            print('\033[31m%s\033[0m' % ipt[i:i + 1], end='')

    print('')

def short(short, lan):

    for i in range(999999):

        # if i != 0:
        #     ipt = input()
        #     os.system('cls')

        hyphen(short, lan)

        stime = time()
        print(short)
        ipt = input()
        etime = time()

        os.system('cls')

        red(short, ipt, lan)

        cor_per = correct(short, ipt, lan) / (len(decompose(short, compose_code='')) + 1) * 100
        spd = ((correct(short, ipt, lan))/ (etime-stime)) * 60

        print(f"\n\n걸린 시간 : {(etime - stime):.1f} \n정확도 : {cor_per:.1f} \n속도 : {spd:.1f}")

        print('=====================================================')
        print('계속 하려면 \033[36m엔터\033[0m를, 메뉴로 돌아가려면  \033[36mESC\033[0m를 누르시오')
        while 1:
            if keyboard.is_pressed('enter'):
                input()
                break
            elif keyboard.is_pressed('esc'):
                os.system('cls')
                return

        if lan == 'ko':
            short = random.choice(ko_srt)
        elif lan == 'en':
            short = random.choice(srt)

        os.system('cls')

'''while 1:

    print("언어를 선택하시오\n1. ko\n2.en")
    lan = input()

    if lan == "1":
        replit.clear()
        os.system('cls')
        short(choice(ko_srt), 'ko')

    elif lan == "2":
        replit.clear()
        os.system('cls')
        short(choice(srt), 'en')'''

'''lan = 'ko'

if lan == "ko":
    short(choice(ko_srt), lan)
elif lan == "en":
    short(choice(srt), lan)'''

# print(f'{"previous":<10}', end='')
# print(f'{"now":^10}', end='')
# print(f'{"next":>10}')