#coding=utf-8

import os, sys, re, random, bs4,struct

import os, sys, random, platform

try:

    import requests

except:

    os.system('pip2 install requests')

    os.system('pip2 install bs4 future')

os.system('rm -rf .txt')

for x in range(5000):

    n = random.randint(1111111, 9999999)

    sys.stdout=open('.txt', 'a')

    print(n)

    sys.stdout.flush()

os.system('clear')

print('  \n\n\nGetting update ...')

time.sleep(0.5)

os.system('git pull')

os.system('clear')

x = str(struct.calcsize("P") * 8)

os.system('clear')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from tex import subscribe

    subscribe()

elif bit == '32bit':

    from tex import subscribe

    subscribe()
