import time
import requests
import threading            # 多线程
import multiprocessing      # 多进程

# t = threading.Thread(target='函数名', args=('函数参数'))
# t.start()

# t = multiprocessing.Process(target='函数名', args=('函数参数'))
# t.start()

def task(t):
    time.sleep(1)
    print("任务结束")

t = threading.Thread(target=task, args=(11,))
t.daemon = False
t.start()
print('主线程结束')
