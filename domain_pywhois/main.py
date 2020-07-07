from bs4 import BeautifulSoup
import time
import pymysql
import requests
import json
import whois
import datetime
import os
import app.try_ssl as try_ssl

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#測試
def whoistest(DNS):
    my_header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    }
    #cookies = {
    #    'Cookie': 'w365_lang=tw; _ga=GA1.2.1571032952.1590997335; _gid=GA1.2.1442033473.1590997335; w365id=2ktpleq6s81bkjmfd9aqa1hcu7'
    #}
    data = {
        'lang': 'tw',
        'task': 'domain',
        'search': '{}'.format(DNS),
        'submit': '查詢'
    }
    #session 長時回話
    s = requests.session()
    #第一次會話連接
    r = s.get('https://www.whois365.com', headers = my_header)
    ## 上面的session会保存会话，往下发送请求，直接使用session即可
    r = s.post('https://www.whois365.com/index.php', headers = my_header, data = data)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.find_all('p', class_='raw_data1')        
    #文字格式回傳
    return t

class domain_search:
    def __init__(self):
        pass                  
    def find_db(self, sql):
        #打開數據庫連結
        db = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '@Go2lixin',
            db = 'webit-v2',
            port = 3306,
            charset = 'utf8'
        )
        #使用cursor方式獲取操作
        cursor = db.cursor()
        #數據庫操作
        cursor.execute(sql)
        #關閉DB
        db.close()
        #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        #獲取所有紀錄
        return cursor.fetchall()

    def webit_search(self, ID):
        my_payload = {
            'password': "88f6b9fd6796391d1fc2b2092f95a284ed2e13b9d328eb009ffaf65f06a7e29c",
            'username': "admin"
        }
        s = requests.session()
        #request payload JSON格式
        r = s.post('https://webit.a45.me/login', json=my_payload)
        x_session_id = r.json()['results']
        my_header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'accept': 'application/json',
            'x-session-id': '{}'.format(x_session_id)
        }
        r = s.get('https://webit.a45.me/cloud/{}/dns/'.format(ID), headers = my_header).json()
        return r

    def whoistry(self, domain):
        result = ''
        try:
            d = whois.whois('%s' % domain)
            today = datetime.datetime.today()
            result = d['expiration_date'] - today
            return result.days
        except Exception:
            pass
    #目前未使用
    def ssltry(self, domain, port):
        result = ''
        try:
            a = try_ssl.get_SSL_Expiry_Date(domain, port)
            t = try_ssl.ssl_end_date(a)
            today = datetime.datetime.today()
            result = t - today
            return result.days
        except Exception:
            pass
        
    def slack(self, token, message):
        my_header = {
            'Content-type': 'application/json'
        }
        r = requests.post(token, json = {'text': message}, headers = my_header)
        return r.text


if __name__ == '__main__':
    #取得dns webit id  
    token = 'https://hooks.slack.com/services/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'  
    sql_id = []                            #製作列表
    domain = []
    sql = r"SELECT  `id` FROM `webit-v2`.`cloud` LIMIT 1000;"
    a = domain_search()
    id_result = list(a.find_db(sql))
    for i in id_result:
        sql_id.append('%s' % i)
    for i in sql_id:
        json_domain = a.webit_search(i)
        #json為字典
        for i in range(len(json_domain['results'])):
            domain.append(json_domain['results'][i]['name'])

    for i in domain:
        print(i)
        t = a.whoistry(i)
        print(t)
        if t <= 30 and t >= 0:
            messages = '{}此域名還有{}天過期'.format(i, t)
            a.slack(token, messages)
        elif t < 0:
            messages = '{}此此域名過期了，請續費'.format(i)
            a.slack(token, messages)
        time.sleep(7)
        

        
