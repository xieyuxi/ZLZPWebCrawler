import ZhiLianSpider
import sys
def main():
    jl=input('请输入工作地点：')
    kw=input('请输入工作关键字：')
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))

    spider=ZhiLianSpider(jl,kw,start_page,end_page)
    spider.run()

#启动爬取程序
if __name__ == '__main__':
    main()