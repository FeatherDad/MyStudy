"""
线程创建示例2
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("线程函数参数")
    sleep(sec)
    print("%s执行完毕"%name)

# 创建5个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),
               kwargs={'name':'T%d'%i})
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
