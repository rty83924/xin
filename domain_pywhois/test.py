from bs4 import BeautifulSoup
import time
import pymysql
import requests
import json
import whois
import datetime
import os
import app.try_ssl as try_ssl
def ssltry(domain, port):
    result = ''
    try:
        a = try_ssl.get_SSL_Expiry_Date(domain, port)
        t = try_ssl.ssl_end_date(a)
        today = datetime.datetime.today()
        result = t - today
        return result.days
    except Exception:
        pass

print(ssltry('tieyideng.com.cn', 443))