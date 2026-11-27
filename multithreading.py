import time
import threading

def bigfunction():
    print("loading.....")
    time.sleep(10)
    print("loading complete")

def smallfunction():
    time.sleep(5)
    print("small done")

t1 = threading.Thread(target = smallfunction)
t1.start()
bigfunction()
smallfunction()

#multithreading is a method of manually creating a new thread to do multitasking