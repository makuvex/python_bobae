from bs4 import BeautifulSoup
from urllib.request import urlopen

# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

with urlopen('http://makuvex7.cafe24.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    file = open('a.txt','w')
    for anchor in soup.select('div.terms_body'):
        print(anchor.text)
        file.write(anchor.text)
    file.close()    
        
            







# import greet

# greet.hello('홍채리')
# greet.niceMeet('장수연')


# from greet import hello, niceMeet

# hello('홍')
# niceMeet('채')

# import math
# print('3.6의 소수점 절삭 : %.1f' % math.floor(3.6))

# import random
# for i in range(1, 10):
#     print(random.randint(1, 3))


# from random import randint
# for i in range(1, 10):
#     print(randint(1, 3))

# import random
# list = ['1','2','3','4']
# for n in range(1, 10):
#     print(random.choice(list))


# from datetime import datetime
# today = datetime.now()
# print(today)
# # print(type(today))

# today_str = today.strftime('%Y/%m/%d %H:%M:%S') 
# print(today_str)
