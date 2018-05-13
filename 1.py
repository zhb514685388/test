'''year = int(input('请输入年份：'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))

for i in range(101):
    if i % 2 != 0:
        print(i,end=' ')

for i in range(1000):
    if i %2 == 1 and i %3 == 2 and i %5 == 4 and i %6 == 5 and i %7 == 0:
        print(i)

for i in range(100,1000):
    a = i // 100
    b = i // 10 %10
    c = i % 10
    if i == pow(a,3) + pow(b,3) + pow(c,3):
        print(i)

x = '红'
y = '黄'
z = '蓝'
for x in range(0,4):
    for y in range(0,4):
        for z in range(2,7):
            if x + y + z == 8:
                print(x,'\t',y,'\t',z)

def power(x,y):
    s = 1
    while y > 0:
        s = s * x
        y = y -1
    return s

def GCU(m, n):
    if not m:
        return n
    elif not n:
        return m
    elif m is n:
        return m

    while m%n:
        m, n = n, m%n

    return n

#二进制求法
def Bin(n):
    a = []
    result = ''
    if n == 1 or n == 0:
        print('{}的二进制是{}'.format(n,n))
    while n:
        a.append(n % 2)
        n = n // 2
    
    while a:
        result += str(a.pop())
    return result

#判断回文联
def Hui(str1):
    result = ''
    temp = list(str1)
    while temp:
        result += temp.pop()
    if str1 == result:
        print('是回文联')
    else:
        print('不是回文联')

str1 = input('请输入一句话：')
Hui(str1)

#统计数字，字母空格数量
def Count(*str1):
    length = len(str1)
    for i in range(length):
        alpha = 0
        digit = 0
        space = 0
        others = 0
        for each in str1[i]:
            if each.isalpha():
                alpha += 1
            elif each.isdigit():
                digit += 1
            elif each.isspace():
                space += 1
            else:
                others += 1
        print('第{}个字符串：有字母{}个，有数字{}个，有空格{}个，有字符{}个'.format(i+1,alpha,digit,space,others))
                

#str1 = input('请输入字符串：')
Count('my name is hon333..','hello  is love you33')

def funx():
    x = 5
    def funY():
        nonlocal x
        x = x + 1
        return x
    return funY

def fibs(n):
    result = [0,1]
    for x in range(2,n):
        result.append(result[x-2] + result[x-1])
    print(result)

def fibs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)

def fac(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum

def fac(n):
    if n ==1:
        return 1
    else:
        return n * fac(n -1)

#二进制递归
def Dec2Bin(dec):
    result = ''

    if dec:
        result = Dec2Bin(dec//2)
        return result + str(dec % 2)
    else:
        return result

#将每个位的数字分解
def get_digits(n):
    a = []
    while n:
        a.append(n % 10)
        n = n // 10
    a.reverse()
    return a

def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1) + 2

#模拟用户登入
def Login():
    while True:
        print('\t|--- 新建用户：N/n ---|')
        print('\t|--- 登入帐号：E/e ---|')
        print('\t|--- 退出程序：Q/q ---|')
        com = input('\t|--- 请输入指令代码：')
        if com == 'N' or com == 'n':
            new_user()
        if  com == 'E' or com == 'e':
            old_user()
        if  com == 'Q' or com == 'q':
            break

def new_user():
    print('新建帐号')
    while True:
        username = input('请输入用户名：')
        if username in dict1:
            print('此用户名以被使用')
            continue
        else:
            break
    password = input('请输入密码：')
    dict1[username] = password
    print('注册成功，请登入吧')

def old_user():
    print('登入帐号')
    while True:
        username = input('请输入用户名：')
        if username not in dict1:
            print('你输入的用户名不存在，请重新输入')
            continue
        else:
            break
    while True:
        password = input('请输入密码：')
        if password != dict1.get(username):
            print('密码不对，请重新输入')
            continue
                
        else:
            print('登入成功')
            break
            
    
dict1 = {}
Login()


def savefile(filename):
    f = open(filename,'x')
    print('请输入内容【单独输入":w"保存退出】')
    while True:
        content = input()
        if content != ':w':
            f.write(content + '\n')
        else:
            break

    f.close()
filename = input('请输入文件名：')
savefile(filename)

#比较文件不同
def compare_file(name1,name2):
    f1 = open(name1,'r')
    f2 = open(name2,'r')
    count = 0
    for i in f1:
        count = count + 1
        if i != f2.readline():
            differ.append(count)
    f1.close()
    f2.close()

name1 = input('请输入需要比较的头一个文件名：')
name2 = input('请输入需要比较的另一个文件名：')
differ = []
compare_file(name1,name2)        
length = len(differ)
if length == 0:
    print('两个文件完全一样')
else：
    print('两个文件共有{}处不一样'.format(length))
    for line in differ:
        print('第{}行不一样'.format(line))

#读出文件的前N行
def file(name,line):
    f = open(name)
    print('文件{}的前{}行的内容如下:'.format(name,line))
    for i in range(line):
        print(f.readline(),end='')
    f.close()

name = input('请输入要打开的文件：')
line = int(input('请输入需要显示该文件前几行：'))
file(name,line)

#读出不同行
def view_file(name,line):
    f = open(name)
    list1 = line.split(":")
    line1 = list1[0]
    line2 = list1[1]
    if line1 == ''and line2 != '':
        for i in f.readlines()[:int(line2)]:
            print(i,end='')
    if line1 != ''and line2 != '':
        for i in f.readlines()[int(line1)-1:int(line2)]:
            print(i,end='')
    if line1 != '' and line2 == '':
        for i in f.readlines()[int(line1)-1:]:
            print(i,end='')
    f.close()

name = input('请输入要打开的文件：')
line = input('请输入需要显示的行数:')
view_file(name,line)

def word_sub(file_name,old_word,new_word):
    f = open(file_name)
    shu = 0
    content = []
    for i in f:
        if old_word in i:
            ss = i.count(old_word)
            
            i = i.replace(old_word,new_word)
        shu = shu + ss
        content.append(i)

    decide = input('文件{}共有{}个{}\n你确定要把所有的{}替换为{}吗?\n【Yes/No】:'.\
                   format(file_name,shu,old_word,old_word,new_word))

    if decide in ['Yes','yes','YES']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()
    f.close()
            
    
file_name = input('请输入文件名：')
old_word = input('请输入要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
word_sub(file_name,old_word,new_word)


#统计各种文件的数量 
import os

all_files = os.listdir(r'E:\python file')
type_dict = {}

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext,0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【{}】的文件{}个'.format(each_type,type_dict[each_type]))


#计算当前文件夹下所有文件大小
import os

file_dict = {}
all_files = os.listdir(r'E:\python file')
for each_file in all_files:
    if  os.path.isfile(each_file):
        file_dict[each_file] = os.path.getsize(each_file)

for i,j in file_dict.items():
    print('{} 【{}bytes】'.format(i,j))

#搜索文件
import os

def search_file(catalog,file):
    os.chdir(catalog)
    for each_file in os.listdir(os.curdir):
        if each_file == file:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file,file)
            os.chdir(os.pardir)#返回上一级目录
    
    
catalog = input('请输入待查找的初始目录：')
file = input('请输入要查找的目标文件：')
search_file(catalog,file)

#搜索指定文件
import os

def search_file(catalog):
    os.chdir(catalog)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            list1 = os.path.splitext(each_file)
            if list1[1] in form:
                path = os.getcwd() + os.sep + each_file + '\n'
                target.append(path)
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)
    
catalog = input('请输入待查找的初始目录：')
form = ['.txt','.py']
target = []
search_file(catalog)
with open(r'e:\python_file\test.txt','w') as f:
    f.writelines(target)


#将不同的对话分割出来
import pickle
def save_file(A,B):
    A_file = open('A.txt','wb')
    B_file = open('B.txt','wb')
    pickle.dump(A,A_file)
    pickle.dump(B,B_file)
    A_file.close()
    B_file.close()

def split_file(file_name):
    count = 1
    A = []
    B = []
    f = open(file_name)
    for each_line in f:
        (role,line_spoken) = each_line.split(':',1)
        if role == 'A':
            A.append(line_spoken)
        if role == 'B':
            B.append(line_spoken)

    save_file(A,B)
    f.close()

split_file(r'f.txt')
f = open('A.txt','rb')
content = pickle.load(f)
print(content)
f.close()'''

'''
class Person():
    def printname(self,name):
        self.name = name
        print('hi:',self.name)'

class Rectangle():
    long = 5.00
    width = 4.00
    
    def setRect(self):
        print('请输入矩形的长和宽')
        long = input('长：')
        width = input('宽:')
        self.long = float(long)
        self.width = float(width)
        
    def getRect(self):
        print('这个矩形的长是{.2f}，宽是{.2f}'.format(self.long,self.width))

    def getArea(self):
        area = self.long * self.width
        print(area)'''

class Ticket():
    
    def __int__(self,ordinary,weekend,child):
        self.ordinary = ordinary
        self.weekend = weekend
        self.child = child

    def money(self):
        money = 2 * self.ordinary + self.ordinary/2
        print('money')
        
    
