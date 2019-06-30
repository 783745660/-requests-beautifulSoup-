#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/6/30 19:15'

import os,csv,threading

# path = os.getcwd()
os.makedirs('RemoveHeaderCSV',exist_ok=True)
# print(path)
'''
将csv文件名写入到列表中保存
'''
csvfile_list = []
for csvfilename in os.listdir('.'):
    if not csvfilename.endswith('.csv'):
        continue
    csvfile_list.append(csvfilename)

def remove_header(startnum,endnum):
    '''
    每次读取列表中endnum - startnum 个文件，去掉第一行后，将其写入到相同文件名中
    '''
    print('当前线程为:', threading.current_thread().name)
    for filenum in range(startnum,endnum):
        csvfile = open(csvfile_list[filenum],'r')  # 打开文件
        renderObj = csv.reader(csvfile)            # 生成reader对象
        csvlist = []
        for row in renderObj:
            if renderObj.line_num == 1:
                continue
            csvlist.append(row)                    # 得到文件副本， 第一行除外，其余全部保存在csvlist中
        csvfile.close()

        outcsvfilepath = os.path.join('RemoveHeaderCSV',csvfile_list[filenum])
        outcsvobject = open(outcsvfilepath,'w',newline='')
        csvwriter = csv.writer(outcsvobject)                # 生成写对象
        for row in csvlist:                                 # 从列表副本里面写入
            csvwriter.writerow(row)
        outcsvobject.close()

threadings_list = []
for i in  range(1,20,4):
    thread = threading.Thread(target=remove_header,args=(i,i+4))
    thread.start()
    threadings_list.append(thread)

for thread in threadings_list:
    thread.join()
print('Done！')









