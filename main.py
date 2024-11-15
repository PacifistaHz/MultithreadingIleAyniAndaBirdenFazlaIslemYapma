import threading
import time

def kanal1(threadName):
    while True:
        time.sleep(1)
        print(threadName+" çalışıyor: "+time.ctime(time.time()))

def kanal2(threadName):
    while True:
        time.sleep(1)
        print(threadName+" çalışıyor: "+time.ctime(time.time()))

t1= threading.Thread(target=kanal1, args=('Kanal 1 ',))
t2= threading.Thread(target=kanal2, args=('Kanal 2 ',))

t1.start()
t2.start()
