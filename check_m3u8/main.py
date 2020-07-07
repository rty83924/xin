import m3u8
import yml
import time
import threading
import queue
import os
import datetime

errorurl = list()
#建立柱列
my_queue = queue.Queue()
#執行續數量
worker_num = 10
#thread 類別 處理資料
class mythread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        #self.urllist = urllist
    def run(self):
        global errorurl
        #queue.empty 如果對列為空，返回true
        while not self.queue.empty():
            #取出 queue 柱列資料
            item = self.queue.get()
            results = m3u8.compare_m3u8('%s' % item).listm3u8()
            if results == False:
                #print(results)
                errorurl.append(item)
            elif results['try1'] >= results['try2']:
                errorurl.append(item)
            #print(item)
            time.sleep(1)

def worker():
    global my_queue
    threads = list()
    tryurl = yml.saveurl().tryurl()
    #將資料放入柱列
    for i in tryurl:
        my_queue.put(i)
    #建立執行續
    for i in range(worker_num):
        #定義執行續工作
        thread = mythread(my_queue)
        threads.append(thread)
        #啟動執行續
        threads[i].start()
    #等待啟動執行敘結束
    for i in range(worker_num):
        threads[i].join()

if __name__ == '__main__':
    worker()
    a = os.path.dirname(os.path.abspath(__file__))
    oldfile = '{}/log/test.txt'.format(a)
    newfile = '{}/log/m3u8.txt'.format(a)
    oldcheck = list()
    newcheck = list()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        os.remove(newfile)
    except OSError as e:
        print(e)
    #取得第一次查詢false url
    try:
        with open(oldfile, 'r') as f:
            #讀行
            oldcheck = f.read().splitlines()
    except Exception as error:
        print(error)

    for i in errorurl:
        if i in oldcheck:
            newcheck.append('%s' % i)

    with open(newfile, 'w') as f:
        f.write('%s\n' % now)
        for i in newcheck:
                f.write('%stest\n' % i)

    with open(oldfile, 'w') as f:
        for i in errorurl:
            f.write('%s\n' % i)
