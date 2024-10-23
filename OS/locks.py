from threading import*
import time

lock = Lock()
count=0

def task(x,y):
    # lock.acquire()
    global count
    for i in range(1000000):
        count+=1
    # lock.release()

if __name__ == '__main__':
    t1=Thread(target=task,args=('d','7'))
    t2=Thread(target=task,args=('d','7'))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count)
