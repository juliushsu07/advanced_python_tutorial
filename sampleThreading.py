import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
	print("timer: " + name + " Started")
	tLock.acquire()
	print(name+" has acuire the lock.")
	while repeat > 0:
		time.sleep(delay)
		print(name + ": "+str(time.ctime(time.time())))
		repeat -= 1
	print(name+" is releasing the lock")
	tLock.release()
	print("Timer: "+name+" Completed")

def Main():
	t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
	t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
	t1.start()
	t2.start()

	print("Main completed")

Main()