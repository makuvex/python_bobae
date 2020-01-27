from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import ssl
import os
import pymysql
import time
from datetime import datetime

#<img onclick="image_pop(this.width,this.height,this.src);" style="cursor:pointer;" alt="클릭하시면 원본 이미지를 보실 수 있습니다." src="https://file1.bobaedream.co.kr/girl/2020/01/19/17/ehda1579424073_10070165.gif">
#<img onclick="image_pop(this.width,this.height,this.src);" style="cursor:pointer;" alt="클릭하시면 원본 이미지를 보실 수 있습니다." src="https://file1.bobaedream.co.kr/girl/2020/01/19/17/ehda1579424077_158547272.gif">

def makeDir(name):
    try:
        mydir = "./download/" + name
        if not(os.path.isdir(mydir)):
            print("make dir")
            os.makedirs(os.path.join(mydir))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("failed to create dir")
            raise
    
    
def detail(url, folder):
    context = ssl._create_unverified_context()
    with urlopen(url, context=context) as response:
        soup = BeautifulSoup(response, 'html.parser')
        count = 0
        for link in soup.find_all('img', {'alt':'클릭하시면 원본 이미지를 보실 수 있습니다.'}):
            if count == 3:
                break
                
            try:
                img = link.get('src')
                print('download %s'%img)        
                if img == None:
                    break
                sep = img.split('/')
                #print(sep[len(sep)-1])
                file = "./download/" + folder + "/" + sep[len(sep)-1]
                print('file %s'%file)        
                urlretrieve(img, file)
            except UnicodeEncodeError:
                print("Errror") 
            finally:
                count += 1


def getLink(url):
    context = ssl._create_unverified_context()
    with urlopen(url, context=context) as response:
        soup = BeautifulSoup(response, 'html.parser')
        linkList = ""
        count = 0
        
        for link in soup.find_all('img', {'alt':'클릭하시면 원본 이미지를 보실 수 있습니다.'}):
            
            # if count == 3:
            #     break
                
            try:
                img = link.get('src')
                
                #print('download %s'%img)        
                if img == None:
                    break
                    
                linkList += img + "\n"
                
                # sep = img.split('/')
                # #print(sep[len(sep)-1])
                # file = "./download/" + folder + "/" + sep[len(sep)-1]
                # print('file %s'%file)        
                # urlretrieve(img, file)
            except:
                print("Errror") 
            finally:
                count += 1                
        return linkList
        
        
if __name__ == "__main__":   
    con = pymysql.connect(host='localhost', user='makuvex7', password='malice77', db='bobae', charset='utf8')
    cur = con.cursor()
    
    while True:
        try:
            context = ssl._create_unverified_context()
            # https://www.bobaedream.co.kr/list.php?code=girl&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=5&info3=&noticeShow=&bestCode=&bestDays=&bestbbs=&vdate=&ndate=&nmdate=&s_select=Subject&s_key=
            #with urlopen('https://www.bobaedream.co.kr/list?code=girl', context=context) as response:
            with urlopen('https://www.bobaedream.co.kr/list.php?code=girl&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=10&info3=&noticeShow=&bestCode=&bestDays=&bestbbs=&vdate=&ndate=&nmdate=&s_select=Subject&s_key=', context=context) as response:    
                soup = BeautifulSoup(response, 'html.parser')
                size = 0
                #print(type(size))

                for tr in soup.find_all('tr', {'itemtype':'http://schema.org/Article'}):
                    try:
                        sno = tr.find('td', {'class': 'num01'})
                        #print('=================== num01 sno %s'%(sno.text))

                        subject = tr.find('a', {'class':'bsubject', 'itemprop':'name'})
                        #print('=================== subject.text %s'%(subject.text))
                        href = "https://www.bobaedream.co.kr" + subject.get('href')
                        #print('href = %s'%href)    
                        #makeDir(subject.text)
                        #사진 다운로드
                        #detail(href, subject.text)

                        author = tr.find('td', {'class': 'author02'}).find('span', {'class': 'author'})
                        #print('=================== author %s'%(author.text))

                        date = tr.find('td', {'class': 'date'})
                        #print('=================== date %s'%(date.text))

                        recomm = tr.find('td', {'class': 'recomm'})
                        #print('=================== recomm %s'%(recomm.text))

                        count = tr.find('td', {'class': 'count'})
                        #print('=================== count %s'%(count.text))

                        linkList = getLink(href)
                        #print('=================== linkList len %d'%len(linkList))

                        sql = """insert into girl(sno,subject,author,link,regdate,recomm,viewcount) values (%s, %s, %s, %s, %s, %s, %s)"""

                        isno = int(sno.text)
                        #print(type(isno))
                        cur.execute(sql, (isno, subject.text, author.text, linkList, date.text, recomm.text, count.text))
                        con.commit()

                    except Exception as e:
                        #print("=========== Errror %s ==========="%e) 
                        continue
                    finally:
                        size += 1
                #print('size %d'%size)          
            #print(datetime.now())
            print("%s, sno %d, subject %s"%(datetime.now(),isno,subject.text))
        except Exception as e:
            #print("=========== Errror %s ==========="%e) 
            continue
        time.sleep(60)
        
'''
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| sno       | int(11)      | NO   | PRI | NULL    |       |
| subject   | varchar(255) | YES  |     | NULL    |       |
| author    | varchar(255) | YES  |     | NULL    |       |
| link      | varchar(255) | YES  |     | NULL    |       |
| regdate   | varchar(100) | YES  |     | NULL    |       |
| recomm    | varchar(10)  | YES  |     | NULL    |       |
| viewcount | varchar(10)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+      
'''    

                
'''
if __name__ == "__main__":   
    con = pymysql.connect(host='localhost', user='makuvex7', password='malice77', db='bobae', charset='utf8')
    cur = con.cursor()
    context = ssl._create_unverified_context()
    with urlopen('https://www.bobaedream.co.kr/list?code=girl', context=context) as response:
        soup = BeautifulSoup(response, 'html.parser')
        count = 0
        for link in soup.find_all('a', {'class':'bsubject', 'itemprop':'name'}):
            try:
                print('=================== link.text %s'%(link.text))
                href = "https://www.bobaedream.co.kr" + link.get('href')
                print('href = %s'%href)    
                makeDir(link.text)
                
                #사진 다운로드
                #detail(href, link.text)
                
                if(count == 0):
                    v = link.get('href').split('&')
                    no = ""
                    for s in v:
                        if "No=" in s:
                            print('================== s %s'%s)
                            no = s.split('=')
                    print('============= no %s'%(no[1]))
                    intV = int(no[1])
                    print(type(intV))
                    print('============= link %s'%(link.text))
                    #idx = int(no)
                    sql = """insert into girl(sno,name,regdate) values (%s, %s, %s)"""
                   # sql = "insert into board_tb (sno, name, regdate) values(no, link.text, '')"
                    cur.execute(sql, (intV, link.text, ''))
                    con.commit()
            except UnicodeEncodeError:
                print("=========== Errror ===========") 
            finally:
                count += 1
        print('count %d'%count)                
        
'''
'''
+---------+-----------+------+-----+---------+-------+                                                                                                                                                                       | Field   | Type      | Null | Key | Default | Extra |                                                                                                                                                                       +---------+-----------+------+-----+---------+-------+                                                                                                                                                                       | sno     | int(11)   | NO   | PRI | NULL    |       |                                                                                                                                                                       | name    | char(100) | YES  |     | NULL    |       |                                                                                                                                                                       | regdate | char(100) | YES  |     | NULL    |       |                                                                                                                                                                       +---------+-----------+------+-----+---------+-------+        
'''

#https://www.bobaedream.co.kr/list?code=girl      
#https://www.bobaedream.co.kr/view?code=girl&No=875317&bm=1

