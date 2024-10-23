import threading
from threading import*
import time

mutex=Semaphore()
rc=0
wrt=Semaphore()

str=0
counter=0

class Writer(threading.Thread):
    def run(self):
        global mutex,rc,wrt,str,counter
        while 1:
            wrt.acquire()
            str=counter
            print("")
            print(f"Total no of reader : {rc}")
            print(f"writer are writing : {str}")
            counter+=1
            wrt.release()
            time.sleep(1)

class Reader(threading.Thread):
    def run(self):
        global mutex,rc,wrt,str,counter
        while 1:
            mutex.acquire()
            rc+=1
            if (rc==1) :
                wrt.acquire()
            mutex.release()
            print("")
            print(f"Total no of reader : {rc}")
            print(f"Reader are reading : {str}")
            mutex.acquire()
            rc-=1
            if(rc==0):
                wrt.release()
            mutex.release()
            time.sleep(1)

if __name__=='__main__':
    writer=Writer()
    reader=Reader()

    writer.start()
    reader.start()

    writer.join()
    reader.join()