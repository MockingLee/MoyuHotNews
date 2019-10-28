import requests
import json
import pymysql
import time


db = pymysql.connect(host='db.pkmgtdz.top',
                             port=3306,
                             user='lee',
                             password='123',
                             db='MoyuHotNews',
                             charset='utf8mb4')

cursor = db.cursor()


def goV2ex():
    '''
    v2ex spider
    :return: null
    '''
    cursor.execute('select max(generation) from api_news where site_type = \'v2ex\'')

    cur_generation = cursor.fetchone()[0]

    url = 'https://www.v2ex.com/api/topics/hot.json'
    response = requests.get(url)

    response = json.loads(response.text)
    cur = 1
    for i in response:
        sql = 'insert into api_news (title, url, create_time, site_type, rank, generation) values (\'%s\', \'%s\', NOW(), \'%s\', %s, %s)' % (
        i['title'], i['url'], 'v2ex', cur, cur_generation + 1)
        # print(sql)
        cursor.execute(sql)
        cur += 1

    db.commit()
    print('[INFO]' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ' v2ex hot catch success: total ' + str(cur) + '.')



def goZhihu():
    from bs4 import BeautifulSoup
    link = 'https://www.zhihu.com/hot'
    hd = {
        'cookie': '_zap=cdfc7edf-5c16-4e12-b3ce-988729dc88a6; _xsrf=ZHfN4whtJD3ULibsyuzlYPtqgHCp5UbP; d_c0="AGBjL3xj8w-PTv5JXnfl6oxC3ukTZCr_ds0=|1566811571"; tst=h; tshl=; q_c1=15cef7987a53446eb263dfe3966b0e9a|1569826716000|1566811745000; l_n_c=1; l_cap_id="MTUzYzg4N2EwNGRhNDQxZjg1MDRmOTQ4NzAyNjRjMmQ=|1569941288|c89cc1f1284137bee3b5418af7c07da3ed35feed"; r_cap_id="MDBlNDg2NWViOGExNDg1ZWJjMzVlN2Q3ZDg0OGJhYzQ=|1569941288|99407178efd3345297d2656714b2fc8736d3dd73"; cap_id="ZmRiYTJiNDk3MDA1NDdlM2E0ZWMyOTQzYjE1ZDRlZTc=|1569941288|16067c72e3efff0d948d69080c55b7a4c505cb5a"; n_c=1; __utma=51854390.927648456.1569941292.1569941292.1569941292.1; __utmb=51854390.0.10.1569941292; __utmc=51854390; __utmz=51854390.1569941292.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190826=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569902375,1569918896,1569940740,1569941393; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; capsion_ticket="2|1:0|10:1569941986|14:capsion_ticket|44:ZjgxZWY2MTkxZDY1NGZlMWI4OTVhZTkyY2Y0MzdiNWE=|9bb4fc6da1c2dfb98e0379fbea796bed1b39be37484362dcc8fe0c9e8d7f3857"; z_c0="2|1:0|10:1569942016|4:z_c0|92:Mi4xNTlxRkFnQUFBQUFBWUdNdmZHUHpEeVlBQUFCZ0FsVk5BTGlBWGdDQU9lTW80R0VzSHNDamxpRTFWV3c4V1I5MmtR|d6feb65a1a46e27dadd58c3982c19b4bb6408570034b00011882b8b8c9896e01"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569942027',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    r = requests.get(link, headers=hd)
    soup = BeautifulSoup(r.text, 'lxml')
    title_list = soup.find_all('section', class_='HotItem')
    cur = 1
    cursor.execute('select max(generation) from api_news where site_type = \'zhihu\'')
    cur_generation = cursor.fetchone()[0]
    for each in title_list:
        index = each.find('div', class_='HotItem-rank').text
        title = each.find('h2', class_='HotItem-title').text
        url = each.find(class_='HotItem-content').contents[0]['href']
        # print(index, title, url)
        sql = 'insert into api_news (title, url, create_time, site_type, rank, generation) values (\'%s\', \'%s\', NOW(), \'%s\', %s, %s)' % (title, url, 'zhihu', cur, cur_generation + 1)
        # print(sql)
        cursor.execute(sql)
        cur += 1

    db.commit()
    print('[INFO]' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ' zhihu hot catch success: total ' + str(cur) + '.')


if __name__ == '__main__':
    while True:
        goV2ex()
        goZhihu()
        time.sleep(1800)





