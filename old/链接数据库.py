#-*-  coding:utf-8 -*-
import pymysql as py

def connect():
    dataall=[]
    list=[11013070003773,1101307000377,11013070003772,11013070003774]
    db=py.connect('47.94.90.42',"autoconvert","autoconvert123","CMS")
    list.sort()
    cursor=db.cursor()
    while list:
        conde = list.pop(0)
        try:
            cursor.execute("SELECT S_VIDEO_CODE,S_FILE_URL from CMS.TC_VIDEO_FILE WHERE S_VIDEO_CODE='%d';"% conde)
            data=cursor.fetchall()
            print(data[0][1])
            dataall.append(data[0])
        except Exception as e:
            print("没有数据库信息 %d" % conde)
    print(dataall)

if __name__=="__main__":
    connect()
