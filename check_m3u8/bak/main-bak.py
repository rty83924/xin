import m3u8
import yml
import time
import threading
import queue

errorurl = list()
my_queue = queue.Queue()
worker_num = 10
class mythread(threading.Thread):
    def __init__(self, job):
        threading.Thread.__init__(self)
        self.job = job
        #self.urllist = urllist
    def run(self):
        try:
            self.job()
        except Exception as f:
            print(f)

def worker():
    global my_queue, errorurl
    while not my_queue.empty():
        item = my_queue.get()
        results = m3u8.compare_m3u8('%s' % item).listm3u8()
        if results['try1'] == False or results['try2'] == False:
            #print(results)
            errorurl.append(item)
        #print(item)
        time.sleep(1)
        #return errorurl

def tests():
    global my_queue
    threads = list()
    tryurl = yml.saveurl().tryurl()
    for i in tryurl:
        my_queue.put(i)
    for i in range(worker_num):
        thread = mythread(worker)
        #thread.start()
        threads.append(thread)
        threads[i].start()
    #for thread in threads:
    #    thread.join()
    for i in range(worker_num):
        threads[i].join()

if __name__ == '__main__':
    tests()
    print(errorurl)