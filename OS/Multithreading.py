import threading
import time

def func(seconds):
    print(f"slepping for {seconds} seconds")
    time.sleep(seconds)

# time1=time.perf_counter()
# func(4)
# func(1)
# func(2)
# time2=time.perf_counter()
# print(time2-time1)


time1=time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[1])
t3 = threading.Thread(target=func, args=[2])
t4 = threading.Thread(target=func, args=[2])
t5 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()
t3.start()
# t4.start()
# t5.start()
t1.join()
t2.join()
t3.join()
# t4.join()
# t5.join()


# t1.start()
# t1.join()
# t2.start()
# t2.join()
# t3.start()
# t3.join()

time2=time.perf_counter()
print(time2-time1)