# requests_BeautifulSoup
基于requests和beautifulSoup下载漫画
## 使用的模块requests,bs4
    1) requests.get()请求目标文件或html，返回一个响应对象
    2) 利用bs4.BeautifulSoup()解析响应对象字符串或html字符串,并生成一BeautifulSoup对象
    3) 利用BeautifulSoup()对象select(参数)方法生成图片元素列表
    4) 请求图片链接地址并保存至本地
## 基于多线程下载文件或处理csv文件
    使用threading多线程库,在for循环中开启多个线程
  ```
    thread_list = []
    for i in  range(1,1000,50):
        downloadthread = threading.Thread(target=download,args=(i,i+50))
        downloadthread.start()
        thread_list.append(downloadthread)
  ```
    定义下载漫画函数
  ```
    def download(startComicnumber,endComicnumber):
        ···
        ···
  ```
