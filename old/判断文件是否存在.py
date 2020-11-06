# -*- coding: utf-8 -*-
import os

def Get_file_list():
    exst = int(0)
    notexst=int(0)
    with open('临时','r+') as f:
        list=f.readlines()
    with open('临时','w+')  as ff:
        for i in list :
            path=i.replace('/','\\')
            if os.path.exists("\\\\192.168.1.218%s"% path.strip()):
                exst+=1
                ff.write(i)
                #print(i.split('/')[-1][0:14])
            else:
                notexst+=1
                #print(i.strip())
                print(i.split('/')[-1][0:14])
    print("文件总数：  %s , 存在数： %s  ,不存在数： %s " % (len(list),exst,notexst))
    f.close()
    ff.close()

if __name__=='__main__':
    Get_file_list()
