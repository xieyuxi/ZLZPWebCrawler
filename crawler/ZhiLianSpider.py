import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import json
import time

url_prefix = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%2589%25A9%25E8%2581%2594%25E7%25BD%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,'
url_postfix = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

for page in range(11,16):
    print('开始爬取第%s页'%page)
    #组装URL

    url= url_prefix+str(page)+url_postfix
    #构建请求对象#
    headers={
        "User-Agnet":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    #发送请求，获取内容#
    request =  urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('gbk')

    soup=BeautifulSoup(content,'lxml')
    results = soup.find_all("script", {"type": "text/javascript"})[2]
    text = str(results)
    list = text.split('{')

    for info in list:
        if(info.find('job_name')!=-1):
            infolist = info.replace('"','').split(',')
            print(info)
            # print(infolist[10],infolist[12],infolist[13],infolist[15])
        else:
            continue
        # print(re.findall(r"company_name\":\"(.+?)\",", info))
        # print(re.findall(r"providesalary_text\":\"(.+?)\",", info))
        # print(re.findall(r"workarea_text\":\"(.+?)\",", info))
    time.sleep(10)
    # res = re.sub(r'.*engine_jds":',"",str(results))
    # data_json = json.dumps(res)
    # print(data_json.encode(''))
    # #解析内容#
    # parse_content(content)
    # print('结束爬取第%s页'%page)
    # time.sleep(10)


# class ZhiLianSpider(object):
#
#     #url中不变的内容，要和参数进行拼接组成完整的url#
#     url='http://sou.zhaopin.com/jobs/searchresult.ashx?'
#     def __init__(self,jl,kw,start_page,end_page):
#         #将上面的参数都保存为自己的成员属性#
#         self.jl=jl
#         self.kw=kw
#         self.start_page=start_page
#         self.end_page=end_page
#         #定义一个空列表，用来存放所有的工作信息#
#         self.items=[]
#
#     #根据page拼接指定的url，然后生成请求对象#
#     def handle_request(self,page):
#         data={
#             'jl':self.jl,
#             'kw':self.kw,
#             'p':page
#         }
#         url_now=self.url+urllib.parse.urlencode(data)#拼接get参数
#         print(url_now)
#         #构建请求对象#
#         headers={
#             "User-Agnet":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
#         }
#         request=urllib.request.Request(url=url_now,headers=headers)
#         return request
#
#     #解析内容函数#
#     def parse_content(self,content):
#         #生成对象#
#         soup=BeautifulSoup(content,'lxml')
#         #思路：先找到所有的table，因为一个工作岗位就是一个table，遍历这个table的列表，然后通过table对象的select、find方法去找每一条记录的具体信息#
#         table_list=soup.select('#newlist_list_content_table>table')[1:]
#         #遍历这个table_list,依次获取每一个数据#
#         print(table_list)
#         print(len(table_list))
#         for table in table_list:
#             #获取职位名称#
#             zwmc=table.select('.zwmc > div > a')[0].text
#             print(zwmc)#选择器返回是一个列表，需要通过下标访问 #
#             #获取公司名称#
#             gsmc=table.select('.gsmc > a')[0].text
#             #获取职位月薪#
#             zwyx=table.select('.zwyx')[0].text
#             #获取工作地点#
#             gzdd=table.select('.gzdd')[0].text
#             #获取发布时间#
#             gxsj=table.select('.gxsj > span')[0].text
#             #存放到字典中#
#             item={
#                 '职位名称':zwmc,
#                 '公司名称':gsmc,
#                 '职位月薪':zwyx,
#                 '工作地点':gzdd,
#                 '更新时间':gxsj,
#             }
#             #再存放到列表中#
#             self.items.append(item)
#
#
#     #爬取程序#
#     def run(self):
#         #循环爬取每一页#
#         for page in range(self.start_page,self.end_page+1):
#             print('开始爬取第%s页'%page)
#             request=self.handle_request(page)
#             #发送请求，获取内容#
#             content=urllib.request.urlopen(request).read().decode()
#             print(content)
#             #解析内容#
#             self.parse_content(content)
#             print('结束爬取第%s页'%page)
#             time.sleep(10)
#
#         #将列表数据保存在文件中#
#         string=json.dumps(self.items,ensure_ascii=False) #将字典形式的数据转化成字符串,想要输出中文需要指定ensure_ascii=False#
#         with open(r'D:/zhilian.txt','w',encoding='utf8')as fp:
#             fp.write(string)

