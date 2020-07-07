import pymysql
import yaml

delet_port = [80, 1935]
sql_zone_id = r"SELECT `id` FROM `webit-v2`.`whitelist_zone`WHERE namespace LIKE 'base\_live%';"
#sql_search_port = "SELECT  `value` FROM `whitelist_port` ORDER BY `zone_id` ASC, `value` DESC LIMIT 1000;"
zone_id = []                            #製作列表
port = []                               #製作列表
def find_db(sql):
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
    #獲取所有紀錄
    #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    return cursor.fetchall()
    

zone_result = find_db(sql_zone_id)
zone_results = list(zone_result)

for i in zone_results:
    zone_id.append('%s' % i)

zone_id = list(set(zone_id))    #刪除重複

for i in zone_id:
    sql_search_port = "SELECT  `value` FROM `whitelist_port` WHERE zone_id LIKE '{}%';".format(i)
    port_result = find_db(sql_search_port) 
    port_results = list(port_result)
    for j in port_results:
        port.append('%d' % j)

port = list(set(port))
port = list(map(int, port)) #list string to int
for i in delet_port:
    prot = port.remove(i)
#方法2
#for i in range(0, len(port)):
#    port[i] = int(port[i])

port.sort()    #小->大排序
with open('./config/haproxy.yml', 'w') as f:
    f.write('base_port:\n')
    yml_file = yaml.dump(port, f)

   

