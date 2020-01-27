from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

'''
import urllib.request 
from bs4 import BeautifulSoup 

if __name__ == "__main__": 
    print("Hello World") 
    req = urllib.request.Request("http://www.naver.com");
    data = urllib.request.urlopen(req).read() 
    bs = BeautifulSoup(data, 'html.parser') 
    l = bs.find_all('a') 
    idx = 0 
    for s in l: 
        try: 
            print("%d : %s" % (idx, str(s))) 
        except UnicodeEncodeError: 
            print("Errror : %d" % (idx)) 
        finally: 
            idx += 1
'''




if __name__ == "__main__":   
    context = ssl._create_unverified_context()
    with urlopen('https://www.bobaedream.co.kr/list?code=girl', context=context) as response:
        soup = BeautifulSoup(response, 'html.parser')
        file = open('bobae.txt','w')
        idx = 0 
        for anchor in soup.find_all('a'):
            try:
                print("%d : %s" % (idx, str(anchor))) 
                file.write("%d : %s" % (idx, str(anchor)))
            except UnicodeEncodeError:
                print("Errror") 
            finally:
                idx += 1
        file.close()                
           