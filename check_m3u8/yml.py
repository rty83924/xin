import yaml
import os
a = os.path.dirname(os.path.abspath(__file__))
# Loader=yaml.FullLoader 取消yml.load 不安全僅告
class sendurl:
    def __init__(self):
        pass
        stream_name = list()
        domain_name = list()
        stream_app = list()
        self.stream_name = stream_name
        self.domain_name = domain_name
        self.stream_app = stream_app
    def domain(self):
        with open('{}/config/domain.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        #data = dict(data)
        for i in data.values():
            self.domain_name = i 
        return self.domain_name
    def streamName(self):
        with open('{}/config/stream.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        #data = dict(data)
        for i in data.keys():
            self.stream_name.append(i)
        return self.stream_name
    def streamApp(self):
        with open('{}/config/stream.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        for i in data.values():
            self.stream_app = i
        return self.stream_app


class saveurl:
    #sendurl = sendurl(self)
    def __init__(self):
        pass
    def tryurl(self):
        urllist= list()
        domain = sendurl().domain()
        streamApp = sendurl().streamApp()
        streamName = sendurl().streamName()
        for i in domain:
            for y in streamApp:
                for j in streamName:
                    urllist.append('https://{}/{}/{}'.format(i, y, j))
        return urllist

if __name__ == '__main__':
#    sendurl = sendurl()
#   print(sendurl.domain())
#    print(sendurl.streamApp())
    saveurl = saveurl()
    print(saveurl.tryurl())