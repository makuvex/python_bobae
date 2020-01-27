'''
name = input('이름 입력: ')

if name == 'asd':
    for x in range(5):
        print('맞다')
elif name == 'zzz':
    print('맞다2')
else:     
    print('틀리다')
    
'''

# sum = 0
# for i in range(1, 10, 2):
#     sum = sum + i
#     print('i %d, sum %d' % (i, sum))
    
# sum = 0
# for i in range(10, 0, -2):
#     sum = sum + i
#     print('i %d, sum %d' % (i, sum))    

'''
sum = 0
j = 0

while True:
    sum = sum + j
    print('j %d, sum %d' % (j, sum))    
    if j == 30:
        break
    else:
        j = j + 1
'''

# color = ['red', 'green', 'blue', 'black', 'white'] 
# #print(color)
# for i in range(len(color)):
#     print(color[i])


# num = list(range(1, 21, 2))
# print(num)

#color = ['red', 'green', 'blue', 'black', 'white'] 
# for c in color:
#     print(c)

# i = 0
# while i < len(color):
#     print(color[i])
#     i = i+1

# color.append('칼라')
# person1 = ['kim', 24, 'kim@naver.com'] 
# s = color + person1
# print(s)

# member = ['황지웅', 20, '경기도 김포시', 'jiwoang@codingschool.info', '123-1234-5678']

# member.remove(20)

# print(member)


# menu = ('짜장', '우동', '짬뽕')
# menu2 = ('123','456')
# print(menu+menu2)


# dic = {'name':'황예린', 'age':22}
# print(dic)
# print(dic['name'])
# print(dic['age'])
# print('길이 %d'%len(dic))

# del dic['name']
# print(dic)

# dic['name'] = 'zzz'
# print(dic)


# phones = {'갤럭시 S5': 2014, '갤럭시 S7': 2016, '갤럭시 노트8': 2017,  '갤럭시 S9': 2018} 
# #print(phones)

# for key in phones:
#     print('key %s, value %s'%(key, phones[key]))

'''
def hello(name):
    print('hello %s'%name)

def even_odd(num):
    if num % 2:
        print('짝수')
    else:
        print('홀수')
        
for n in range(1, 10):
    even_odd(n)
'''



# file = open('sample.txt', 'w')
# file.write('hello')
# file.close
'''
scores = ['안소영 97 80 93 97 93',            '정예린 86 100 93 86 90',            '김세린 91 88 99 79 92',            '연수정 86 100 93 89 92',            '박지아 80 100 95 89 90'] 
#print(scores)

data = ''
for d in scores:
    data = data + d + '\n'

print(data)
file = open('sample.txt', 'w')
file.write(data)
file.close


read = open('sample.txt','r')

lines = read.readlines()
for l in lines:
    print(l)

'''

# class Animal:
#     name = '고양이'
#     def sound(self):
#         print('냐옹')
        
# cat = Animal()

# print(cat.name)
# cat.sound()

# cat.name = '강아지'
# print(cat.name)


class Person:
    def __init__(self, name):
        self.name = name
        print('name %s'%name)

        
a = Person('a')
a.name = 'b'

print(a.name)
















































    