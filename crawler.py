#导入自动化模块
import json
import time
from pprint import pprint
from DrissionPage import ChromiumOptions
from DrissionPage._pages.chromium_page import ChromiumPage
import csv
#创建文件对象
f = open('data.csv',mode='w',encoding='utf-8',newline='')
#字典写入方法
csv_writer=csv.DictWriter(f,fieldnames=[
    '职位',
'城市',
'区域',
'街道',
'公司',
'薪资',
'经验',
'学历',
'领域',
'融资',
'规模',
'技能要求',
'基本福利',
])
#写入表头
csv_writer.writeheader()
path = r'D:\BaiduNetdiskDownload\101.0.4951.54_chrome64_stable_windows_installer\chrome\Chrome-bin\chrome.exe'
ChromiumOptions().set_browser_path(path).save()
#实例化浏览器对象
dp = ChromiumPage()
#监听数据包
dp.listen.start('wapi/zpgeek/search/joblist.json')
#访问网站
dp.get('https://www.zhipin.com/web/geek/job')
#等待数据包的加载
resp=dp.listen.wait()
#循环翻页
for page in range(1,11):
    print(f'正在采集{page}页的数据内容')
    #下滑页面到底部
    dp.scroll.to_bottom()
    #获取响应数据
    json_data=resp.response.body
    """解析数据"""
    #提取职位信息所在列表
    jobList=json_data['zpData']['jobList']
    #for循环遍历，提取列表里面元素（30个岗位信息）
    for index in jobList:
        #pprint(index)
        dit={
            '职位':index['jobName'],
            '城市': index['cityName'],
            '区域': index['areaDistrict'],
            '街道': index['businessDistrict'],
            '公司': index['brandName'],
            '薪资': index['salaryDesc'],
            '经验': index['jobExperience'],
            '学历': index['jobDegree'],
            '领域': index['brandIndustry'],
            '融资': index['brandStageName'],
            '规模': index['brandScaleName'],
            '技能要求': index['skills'],
            '基本福利': index['welfareList'],
        }
        #写入数据
        csv_writer.writerow(dit)
        pprint(dit)
    #元素定位
    time.sleep(2)
    dp.ele('css:.ui-icon-arrow-right').click()