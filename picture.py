''''' 
第一个示例：简单的网页爬虫 
 
爬取豆瓣首页 
'''  
  
import urllib.request  
import re
def getHtml():  
#网址  
    url = "http://www.douban.com/"  
#    url = "https://img1.doubanio.com/view/photo/albumcover/public/p2501793247.jpg"
#请求  
#    request = urllib.request.Request(url)  
  
#爬取结果  
    response = urllib.request.urlopen(url)  
  
    data = response.read()  
  
#设置解码方式  
    data = data.decode('utf-8')  
    return data
#打印结果  
#print(data)  
def getImage(html):
    reg = r'data-origin="(https://.+?\.jpg)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    imgName = 0
    for imgPath in imglist:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
        f = open("D:/img/"+str(imgName)+".jpg", 'wb')
        f.write((urllib.request.urlopen(imgPath)).read())
        f.close()
        imgName += 1

#        print("All Done!")
#    x = 0
#    for imgurl in imglist:
#        urllib.request.urlretrieve(imgurl, '%s.jpg' % x, '', '')
#        x+=1
    return imglist 
print( getImage(getHtml()))
print("All Done!")
#urllib.response.read()
#https://img1.doubanio.com/view/photo/albumcover/public/p2501793247.jpg
#打印爬取网页的各类信息  
  
#print(type(response))  
#print(response.geturl())  
#print(response.info())  
#print(response.getcode())
