#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import StringIO
import urllib
import re
import json
import model
class Crawler():
    def __init__(self,base_url):
        self.base_url = base_url
        self.buf_1 = StringIO.StringIO()
        self.buf_2 = StringIO.StringIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.CONNECTTIMEOUT,5)
        self.curl.setopt(pycurl.TIMEOUT,8)
        self.curl.setopt(pycurl.COOKIEFILE,'')
        self.curl.setopt(pycurl.FAILONERROR,True)
    
    def get_data
    def wencai_crawler(self):
        self.values = {
        'typed':'1',
        'preParams':'',
        'ts':'1',
        'f':'1',
        'qs':'1',
        'selfsectsn':'',
        'querytype':'',
        'searchfilter':'',
        'tid':'stockpick',
        'w':'pe',
        }
        
        #第一次请求获取含token的JSON
        url = base_url+'/search?%s'%(urllib.urlencode(values))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_1.write)#设置回调
        self.curl.perform()
        
        res = re.findall(u'var allResult = (.*)?;',self.buf_1.getvalue())
        assert 1 == len(res)#应该只有一个符合结果
        token_obj = json.loads(res[0])
        
        #获取含token后请求一次拉取所有股票
        args = {
        'token': token_obj['token'],#token
        'p':1,#第几页
        'perpage':token_obj['total'],#每页多少股票
        }
        url = base_url+'/cache?%s'%(urllib.urlencode(args))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_2.write)#设置回调
        self.curl.perform()
        
        response = self.buf_2.getvalue()
        all_result = json.loads(response)
        data = all_result['list']
        
        self.save = []
        for item in data:
            arr = []
            item[0] = item[0].split('.')[0]
            arr.append(item[0])
            for id in range(1,8):
                if cmp('--',item[id]) == 0:
                    item[id] = -9999999
                arr.append(item[id])
            self.save.append(Iwencai(arr))
        for item in self.save:
            print item.code
            print item.name
            print item.get_increase()
            print item.get_price()
            print item.get_pe()
            print item.get_forcast()
            print item.get_pbv()
            print item.get_total()
            print '\n'
        print len(save)
        