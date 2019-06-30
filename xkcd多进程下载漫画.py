#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/6/30 16:30'
import os,requests,bs4,threading,time
url = 'http://www.xkcd.com'
ImagePath = os.path.join(os.getcwd(),'XkcdImage')
# os.makedirs(ImagePath)              #已经存在所有注释掉


def download(startComicnumber,endComicnumber):
    print('当前线程的名字是： ', threading.current_thread().name)
    for num in range(startComicnumber,endComicnumber):
        url_comic = url+'/'+str(num)
        print('downing page'+ url_comic)
        res = requests.get(url_comic)                    #请求到当前页目标地址，返回一个目标响应对象
        res.raise_for_status()                          #检测异常，是否请求成功
        soup = bs4.BeautifulSoup(res.text)                  #解析当前页响应html字符串
        comic_ls = soup.select('#comic img')                 #获得id=comic,class=img的元素列表
        link = comic_ls[0].get('src')               #得到当前页漫画的连接
        image_url ='http:'+ link                          #得到当前页漫画的url
        image_res = requests.get(image_url)                  #获得图片
        image_res.raise_for_status()                           #检测是否响应成功
        print('Downing image from %s...'% image_url)                          #如果响应成功就打印出正在从图片的url获取图片
        imageFile = open(os.path.join(ImagePath,os.path.basename(link)),'wb')         #以二进制创建一个图片文件
        for chunk in image_res.iter_content(100000):          #图片的每100000字节为一段，分段写入图片文件中，以节省内存
            imageFile.write(chunk)
        imageFile.close()                                    #关闭写入后的图片文件
        print('Done!')

thread_list = []

start_time = time.time()
for i in  range(1,1000,50):
    downloadthread = threading.Thread(target=download,args=(i,i+50))
    thread_list.append(downloadthread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end_time = time.time()

print('用时:', end_time-start_time)

path = os.path.abspath('XkcdImage')
print(path)
ls = os.listdir('XkcdImage')
print(len(ls))