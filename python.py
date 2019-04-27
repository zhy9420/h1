# 1:用户登录,判断用户登录成功还是失败
import getpass

userdb = {}

def register():
    user = input('用户名: ').strip()
    if user and user not in userdb:
        passwd = input('密码: ')
        userdb[user] = passwd
    else:
        print('用户名不能为空，或用户名已存在')

def login():
    user = input('用户名: ')
    passwd = getpass.getpass('密码: ')   # abc
    if userdb.get(user) == passwd: # 如果用户不在字典中返回值为None，否则返回它>的密码
        print('登陆成功')
    else:
        print('登陆失败')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的选择，请重试。')
            continue

        if choice == '2':
            print('Bye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()




# 2.将unix的文件转换成linux文件

import sys

def unix2dos(fname):
    unix2dos(sys.argv[1])
    dst_fname = fname + '.txt'

    with open(fname) as src_fobj:
        with open(dst_fname,'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'
                dst_fobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1])



# 3.在屏幕上打印20个#号,符号从20个#号穿过,档@符号到达尾部,在重头开始

import time

n = 0
print('#' * 20, end='')
while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
    n += 1
    if n == 20:
        n = 0
    time.sleep(0.4)




# 4.改变因输入不当的报错,以及报错也会执行的代码

try:                                   #把可能发生异常的代码放入try中执行
    num = int(input('number:'))
    result = 100 / num
    print(result)
except (ZeroDivisionError,ValueError):  #except捕获异常,做出相应的反应,相同的异常,可以写在一起
    print('无效的数字')
except (EOFError,KeyboardInterrupt):
    print('\nBye.bye')
finally:                        #不管是否发生异常,都会执行的操作
    print('Done')




# 5.假设在记账时，有一万元钱
# 无论是开销还是收入都要进行记账
# 记账内容包括时间、金额和说明等
# 记账数据要求永久存储

import os
import pickle
from time import strftime

def save(fname):
    amount = int(input('金额: '))
    comment = input('说明: ')
    date = strftime('%Y-%m-%d')   # 获取当前日期
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)      # 从文件中取出全部记录
        balance = data[-1][-2] + amount   # 文件最后一行的倒数第2项是余额

    line = [date, amount, 0, balance, comment]
    data.append(line)  # 把最新记录加入到大列表

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)  # 把大列表写到文件

def cost(fname):
    amount = int(input('金额: '))
    comment = input('说明: ')
    date = strftime('%Y-%m-%d')  # 获取当前日期
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)  # 从文件中取出全部记录
        balance = data[-1][-2] - amount  # 文件最后一行的倒数第2项是余额

    line = [date, 0, amount, balance, comment]
    data.append(line)  # 把最新记录加入到大列表

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)  # 把大列表写到文件


def query(fname):
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)

    # 打印表头
    print('%-15s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for line in data:
        print('%-15s%-8s%-8s%-12s%-20s' % tuple(line))  # 将列表转成元组


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'record.data'
    if not os.path.exists(fname):
        date = strftime('%Y-%m-%d')
        data = [
            [date, 0, 0, 10000, 'init data']
        ]
        with open(fname, 'wb') as fobj:
            pickle.dump(data, fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()




# 6.随机生成两个100以内的数字
# 随机选择加法或是减法
# 总是使用大的数字减去小的数字
# 如果用户答错三次，程序给出正确答案

from random import randint, choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}       #匿名函数
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列，默认升序
    op = choice('+-')
    result = cmds[op](*nums)   # 将列表拆开
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 算式
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 可以捕获所有异常，但是不推荐
            print()
            continue

        if answer == result:
            print('Very good!!!')
            break

        print('不对哦')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()




# 7.按钮

import tkinter
from functools import partial

window = tkinter.Tk()
lb = tkinter.Label(window, text="Hello World!", font="Arial 20")
# b1 = tkinter.Button(window, fg='white', bg='blue', text='Button 1')
MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 1')
b3 = MyButton(text='Button 1')
qb = MyButton(text='QUIT', command=window.quit)

lb.pack()
b1.pack()
b2.pack()
qb.pack()

window.mainloop()





# 8.校验文件md5sum值

import hashlib
import sys
import os

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except IndexError:
        print('Usage: %s filename' % sys.argv[0])
        exit(1)   # $?的值为1
    if not os.path.isfile(fname):
        print('No such file: %s' % fname)
        exit(2)
    print(check_md5(fname))







# 9.备份程序(增量/差异备份)

import os
import tarfile
import pickle
# from check_md5 import check_md5         #上面写的MD5校验程序
from time import strftime

def full_backup(src, dst, md5file):
    # 生成压缩包的绝对路径
    fname = os.path.basename(src)      #只保留路径最后
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)  # 拼接绝对路径

    # 打包文件
    tar = tarfile.open(fname, 'w:gz')      #先告诉压缩后的存放路径
    tar.add(src)                #在将需要压缩的文件路径添加
    tar.close()             #关闭

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):       #遍历目录
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将字典写入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


# 差备份
def incr_backup(src, dst, md5file):
    # 生成压缩包的绝对路径
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5字典
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 更新md5字典文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

    # 从新字典取出文件名(key)和md5值，和老字典比较，新增的和修改过的需要打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if md5dict[key] != old_md5.get(key):
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src = '/tmp/mydemo/security'
    dst = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)







# 10.快速排序

from random import randint

def qsort(seq):
    if len(seq) < 2:
        return seq

    middle = seq[0]
    smaller = []
    larger = []

    for item in seq[1:]:
        if item <= middle:
            smaller.append(item)
        else:
            larger.append(item)

    return qsort(smaller) + [middle] + qsort(larger)        #使用qsort函数再次对排序的结果排序

if __name__ == '__main__':
    nums = [randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))






# 11.查找access_log日志,每个ip的访问次数,浏览器访问的方式次数

import re

def count_patt(fname, patt):
    patt_dict = {}                  #定义空的字典
    cpatt = re.compile(patt)        #先选择正则匹配的方式
    with open(fname) as fobj:       #打开文件
        for line in fobj:           #遍历1
            m = cpatt.search(line)  #逐行匹配
            if m:  # 如果匹配到内容，更新字典，None表示False
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1      #get查到字典key,便把key的值加1
    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'                #指定文件名
    ip = '^(\d+\.){3}\d+'  # 1.11.123.45,  12345.11111.23423.2535234        #选定义好匹配ip的正则
    br = 'Chrome|Firefox|MSIE'                  #匹配三中浏览器的方法
    print(count_patt(fname, ip))
    print(count_patt(fname, br))






# 12.套接字创建TCP服务器
# tcp_server服务端
import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        print()
        break
    print('客户机: ', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        print(data.decode(), end='')
        sdata = input('> ') + '\r\n'  # input读入的是str类型
        cli_sock.send(sdata.encode())  # 转成bytes类型发送
    cli_sock.close()

s.close()


# tcp_client客户

import socket

server = '192.168.4.254'
port = 12345
addr = (server, port)  # 要连接的服务器地址
c = socket.socket()
c.connect(addr)   # 连接服务器

while True:
    data = input('(quit to end)> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    rdata = c.recv(1024)   # 一次最多接收1024字节数据
    print(rdata.decode(), end='')

c.close()






# 13.UDP套接字通信

# 服务端
host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)  # UDP的type是SOCK_DGRAM
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)


while True:
    try:
        data, cli_addr = s.recvfrom(1024)  # 一次最多接收1024字节数据，返回值是(数据，客户机地址)
    except KeyboardInterrupt:
        print()
        break
    data = data.decode()  # bytes转str
    print(data, end='')
    rdata = '[%s] %s' % (strftime('%H:%M:%S'), data)
    s.sendto(rdata.encode(), cli_addr)  # 向客户机地址发送数据

s.close()




# 客户端
import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)  # 待连接的服务器地址
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)
    # info = c.recvfrom(1024)   # (数据，服务器地址)
    data = c.recvfrom(1024)[0]
    print(data.decode(), end='')

c.close()






# 14.多线程ping

import threading
import subprocess

def ping(host):
    rc = subprocess.run(
        'ping -c2 %s &>/dev/null' % host,shell=True
    )
    if rc.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    iplist = ['176.19.8.%s' % i for i in range(1,255)]
    for ip in iplist:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()





# 15.pymysql模块,连接数据库,创建三张表

import pymysql
# 创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1811',
    charset='utf8'
    )
cursor = conn.cursor()  # 创建游标
# SQL语句
# create_dep = '''CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(20),
# PRIMARY KEY(dep_id)
# )'''
# cursor.execute(create_dep)   # 执行sql语句
# create_emps = '''CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(20), email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )'''
# cursor.execute(create_emps)
create_sal = '''CREATE TABLE salary(
auto_id INT, emp_id INT, date DATE, basic INT, awards INT,
PRIMARY KEY(auto_id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''
cursor.execute(create_sal)
conn.commit()    # 提交改动
cursor.close()   # 关闭游标
conn.close()     # 关闭连接





# 16.爬取图片

from urllib import request
import sys

def download(url, fname):
    r = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = r.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])

import re
import requests

url = 'http://www.163.com'    #直接下载网站地址
r = requests.get(url).txt
asd = re.findall("http[^\s*?\.jpeg]",r)
asd = set(asd)
for i in asd:
    print(i)


from urllib import request, error     #将图片下载到文件内
import re
import os

def download(url, fname):
    r = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = r.read(1024)
            if not data:
                break
            fobj.write(data)

def get_patt(fname, patt, encoding='utf8'):
    cpatt = re.compile(patt)
    patt_list = []
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

if __name__ == '__main__':
    url163 = 'http://www.163.com'
    fname163 = '/tmp/163.html'
    download(url163, fname163)
    img_patt = 'http://[\w/.-]+\.(jpg|png|jpeg|gif)'
    img_urls = get_patt(fname163, img_patt, 'gbk')
    img_dir = '/tmp/163'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    for url in img_urls:
        img_fname = url.split('/')[-1]   # 取出网址中的文件名
        img_fname = os.path.join(img_dir, img_fname)
        try:
            download(url, img_fname)
        except error.HTTPError:
            pass  # 需到异常，不采取任何操作




# 17.使用位子变量,paramiko模块,对多个主机执行操作
import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user='root', passwd=None, port=22, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    error = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if error:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, error.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command'" % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('No such file:', ipfile)
        exit(2)
    passwd = getpass.getpass()
    command = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, passwd=passwd, cmd=command)
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'cmd': command})
            t.start()
            # target(*args, **kwargs)
            # target(ip, passwd=passwd, cmd=command)
#位子变量1:需要操作的ip地址,位子变量2,需要对这些主机执行的命令






# 18.使用邮件服务器

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_email(msg, subject, sender, receivers, host, passwd):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    msg = 'python smtplib 邮件测试\r\n'
    subject = 'py mail test'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    host = 'smtp.126.com'
    passwd = getpass.getpass()
    send_email(msg, subject, sender, receivers, host, passwd)






# 19.钉钉机器人

# 钉钉机器人：
# 1、搜索 钉钉开放平台，找到开发者手册地址：
# https://open-doc.dingtalk.com/
# 点击“移动应用接入”，再从右上角搜索“自定义机器人”
# 2、在钉钉中创建一个群，添加群聊机器人，类型是webhook，
# 将群聊机器人的webhook网址复制下来，这个是机器人聊天的授权地址

import json
import requests
import sys
import getpass

def dingtalk(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }

    # "msgtype": "link",                line(链接)方式,替换上面的格式即可
    # "link": {
    #     "text": "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。而在此之前，每当面
    #     临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？",
    #                                         "title": "时代的火车向前开",
    # "picUrl": "https://upload.jianshu.io/users/upload_avatars/12347101/6b21f2d2-de50-4c8f-ba23-bf7f80ba77aa.jpg",
    # "messageUrl": "http://www.tmooc.cn"           此处url地址可自定义
    # }
    # }



    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['18211722856']  # 特殊提醒要查看的人,就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=9aac2aaedb555456f25ff6da2c673734c10ef3ae4864ac35f830ecb723dacfc6'   #填写webhool地址
    # url = getpass.getpass()           #webhook地址不方便别人看见时使用
    print(dingtalk(url, reminders, msg))






# 20.zabbix连接,监控各项指标

import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'           #该地址为主机安装zabbix的web页面
headers = {'Content-Type':      'application/json-rpc'}

# data = {
#     "jsonrpc": "2.0",   # jsonrpc版本，固定的
#     "method": "apiinfo.version",  # 手册页上提供的
#     "params": [],
#     "id": 1   # 随便给定一个数字，表示作业号
# }

###############################
# 获取管理员的授权码
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 81811480951b5ad9594f004573c99414
###############################
###############################
# 获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#                 "web1"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
###############################
# 获取Linux servers组的ID号
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
# 2
###############################
# 获取Template os linux模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
# 10001
###############################
# 创建主机web2，它在2号组中，使用10001模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web2",
        "interfaces": [   # 定义通过什么方式进行监控
            {
                "type": 1,  # 1号类型是zabbix agent
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.4",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,   # 主机资产记录
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "81811480951b5ad9594f004573c99414",
    "id": 1
}

###############################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要是result部分





# 21.






