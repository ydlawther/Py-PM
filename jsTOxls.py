import requests
import json
import xlwt

# 获取城市PM2.5的api数据

def readjsonfile(city):
    url = "http://www.pm25.in/api/querys/co.json?city={}&token=5j1znBVAsnSf5xQyNQyq".format(city)
    r = requests.get(url)
    hjson = json.loads(r.text)
    return hjson

# 将api数据存储为同文件夹下的.xls文件

def jsonToexcel(city):
    jsonfile = readjsonfile(city)
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('student')
    ll = list(jsonfile[0].keys())
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])
    for j in range(0,len(jsonfile)):
        m = 0
        ls = list(jsonfile[j].values())
        for k in ls:
            sheet1.write(j+1, m, k)
            m += 1
    wb.save('pm2.5.xls')