#coding=utf-8
import requests
import json
import urllib
from lxml import etree

class Sina_gk():

    def __init__(self):
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        self.i=0

    def college_id_name(self):
        ar=[]
        url='http://kaoshi.edu.sina.com.cn/?p=college&s=api2015&a=getAllCollege'
        res=requests.get(url,self.header)
        res.encoding='utf-8'
        data=res.json()
        res.close()
        for i in range(1,33):
            dic=data['data'][str(i)]
            for k in dic['college'].values():
                ar.append(k)
        return ar

def paser(college_name):
    print college_name
    url='http://gaokao.chsi.com.cn/lqfs/query.do?ssdm=34&year=2017&kldm=15&score=&ranger=10&type=1&'.format(college_name)
    res=requests.get(url)
    res.encoding='utf-8'
    html=etree.HTML(res.text)
    res.close()
    seletor=html.xpath()


if __name__=='__main__':
    gk=Sina_gk()
    for k in gk.college_id_name():
        v=k.encode('utf-8')
        ur=urllib.urlencode({'yxmc':v})
        paser(ur)