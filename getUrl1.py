# import random
# import time
# import requests
# from bs4 import BeautifulSoup
# #指定搜索关键字
# kwd = 'vape '
# #自定义请求头信息:UA伪装,将包含了User-Agent的字典作用到请求方法的headers参数中即可
#
#
# def getAllRrl(kwd):
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     #指定url，原始url可能是https://www.sogou.com/web?query=撩妹，发现该url携带了参数
#     url = f'https://www.google.com//search?q={kwd}'
#     #封装get请求参数：如果请求携带了参数，则可以将参数封装到字典中结合这requests请求方法中的data/params参数进行url参数的处理
#
#     #发起请求
#     response = requests.get(url,headers=headers)
#     if response.status_code != 200:
#         print('请求失败')
#         return
#
#     rlt01 = BeautifulSoup(response.text,'html.parser')
#     rlt02 = rlt01.find_all('div',class_='tF2Cxc')
#
#     for rank,result in enumerate(rlt02,start=1):
#         title = result.find('h3').text
#         url = result.find('a')['href']
#         print('rank:',rank)
#         print('title:',title)
#         print('url:', url)
#
#     time.sleep(random.uniform(1,2))
#
#
#
#
#
#
#
# getAllRrl(kwd)
#
#
import random
import time
import requests
from bs4 import BeautifulSoup


# this is a test



# 指定搜索关键字
kwd = 'vape'

def getAllRrl(kwd, pages):  # 增加 pages 参数，控制爬取页数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for page in range(pages):  # 循环爬取多页
        start = page * 10  # 计算 start 参数，每页 10 条
        url = f'https://www.google.com/search?q={kwd}&start={start}'  # 添加 start 参数控制页码

        # 发起请求
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print('请求失败')
            return

        rlt01 = BeautifulSoup(response.text, 'html.parser')
        rlt02 = rlt01.find_all('div', class_='tF2Cxc')

        for rank, result in enumerate(rlt02, start=1 + page * 10):  # 修改 rank，保持全局排名
            title = result.find('h3').text
            url = result.find('a')['href']
            print('rank:', rank)
            print('title:', title)
            print('url:', url)

        time.sleep(random.uniform(1, 2))  # 随机延迟，防止被封禁

# 调用函数，指定爬取 5 页结果
getAllRrl(kwd, pages=5)

# #获取响应数据
# # page_text = response.text
# #
# # print('test',page_text)
# #持久化存储
# # fileName = word+'.html'
# # with open(fileName,'w',encoding='utf-8') as fp:
# #     fp.write(page_text)