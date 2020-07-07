import re
import requests
import os
import time
#from yml import sendurl

a = os.path.dirname(os.path.abspath(__file__))

class search_m3u8:
    playlist = ''
    def __init__(self, url=None):
        self.url = url
        try:
            playlist = requests.get(self.url)
            results = '%s' % playlist.text
            #將# 換成''
            results = re.sub('[#]', '', results)
            #利用 \n 分成list
            results = results.split('\n')
            self.results = results
            #print(self.results)
        except requests.exceptions.RequestException:
            pass

        #pattern = re.compile(r'#EXT-X-MEDIA-SEQUENCE')
    #尋找seq值
    def trym3u8(self):
        try:
            for i in self.results:
                if 'EXT-X-MEDIA-SEQUENCE' in i:
                    results = i
            return int(results.split(':')[1])
        except Exception:
            return False
    #尋找target秒數
    def targetm3u8(self):
        try:
            for i in self.results:
                if 'EXT-X-TARGETDURATION' in i:
                    results = i
            return int(results.split(':')[1])
        except Exception:
            return False

class compare_m3u8():
    def __init__(self, url):
        self.url = url
        #search_m3u8 = search_m3u8(self.url)
    def listm3u8(self):
        sleeptime = search_m3u8(self.url).targetm3u8()
        a = search_m3u8(self.url).trym3u8()
        time.sleep(sleeptime + 1)
        b = search_m3u8(self.url).trym3u8()
        results = {'try1': int(a), 'try2': int(b)}
        return results

#繼承               
#class compare_m3u8(search_m3u8):
#    def __init__(self, url):
#        super().__init__(url)
#    def tests(self):
#        sleeptime = search_m3u8.targetm3u8(self)
#        a = search_m3u8.trym3u8(self)
#        print(a)
if __name__ == '__main__':
    #compare_m3u8 = compare_m3u8('https://wmvdo.nicejj.cn/live5/720p.m3u8')
    print(compare_m3u8('https://wmvdo.nicejj.cn/live5/720p.m3u8').listm3u8())
    #if compare_m3u8.listm3u8()['try1'] == False:
    #    print('notok')
##print(search_m3u8('https://wmvdo.nicejj.cn/live6/720p.m3u8').num())




