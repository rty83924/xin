import re
import requests
import os
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
#from yml import sendurl

a = os.path.dirname(os.path.abspath(__file__))

class search_m3u8:
    playlist = ''
    def __init__(self, url=None):
        self.url = url
        s = requests.session()
        #Total - 允許的重試次數總數。
        #backoff_factor - 在嘗試之間應用的後退係數
        #status_forcelist - 一組HTTP狀態代碼，我們應該強制重試
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[ 500, 502, 503, 504 ])
        s.mount('http://', HTTPAdapter(max_retries=retries))
        s.mount('https://', HTTPAdapter(max_retries=retries))
        try:
            playlist = s.get(self.url, timeout=5)
            results = '%s' % playlist.text
            #將# 換成''
            results = re.sub('[#]', '', results)
            #利用 \n 分成list
            results = results.split('\n')
            self.results = results
        except requests.exceptions.RequestException:
            self.results = ''
        #pattern = re.compile(r'#EXT-X-MEDIA-SEQUENCE')
    #尋找seq值
    def trym3u8(self):
        m3u8results = dict()
        for i in self.results:
            if 'EXT-X-MEDIA-SEQUENCE' in i:
                #取 : 字串 等同linux cut
                j = i.split(':')[1]
                m3u8results['media'] = int(j)
            elif 'EXT-X-TARGETDURATION' in i:
                j = i.split(':')[1]
                m3u8results['target'] = int(j)
        return m3u8results

class compare_m3u8():
    def __init__(self, url):
        self.url = url
    def listm3u8(self):
        try:
            a = search_m3u8(self.url).trym3u8()
            time.sleep(a['target'] + 1)
            b = search_m3u8(self.url).trym3u8()
            results = {'try1': a['media'], 'try2': b['media']}
            return results
        except Exception:
            return False

#繼承               
#class compare_m3u8(search_m3u8):
#    def __init__(self, url):
#        super().__init__(url)
#    def tests(self):
#        sleeptime = search_m3u8.targetm3u8(self)
#        a = search_m3u8.trym3u8(self)
#        print(a)
if __name__ == '__main__':
    #print(search_m3u8('http://httpstat.us/500').trym3u8())  
    print(compare_m3u8('https://wmvdo.nicejj.cn/live/720p.m3u8').listm3u8())





