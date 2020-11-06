#!/bin/usr/env python
# -*- coding:utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import shutil,json,time,os,datetime,configparser,subprocess
def getparmaiter():
    print("当前所有项目")
    print("\033[0;33;30m1: 广东广电（ts）\t\t\t\t2: 陕西广电（ts）\t\t\t3: 甘肃移动梨园行（ts）"
          " \n4: 甘肃电信梨园行（ts）\t\t\t5: 陕西丝路（ts）\t\t\t6: 河北移动/河北联通(ts)"
          "\n7: 广东移动(ts)\t\t\t\t\t8: 悦道粤广电（ts）\t\t\t9: 河南联通本地教育(ts)\n"
          "10: 悦道学堂APP\t\t\t\t\t11: 广西广电（ts）\t\t\t12: 深圳天威\n"
          "13: 江苏移动\t\t\t\t\t\t14: OTT梨园行\t\t\t\t15: 天津联通TV中心高清/内蒙烽火台\n"
          "16: 江苏电信标清\t\t\t\t\t17: 江苏电信高清\t\t\t\t18: 山东广电高清\n"
          "19:天津广电\t\t\t\t\t\t20: 深圳天威\t\t\t\t\t21: 河南电信\n"
          "22: 四川电信\t\t\t\t\t\t23: 沃视频\t\t\t\t\t24: \033[0m")
    config = configparser.ConfigParser()
    config.read('config.ini')
    project = input("\n\033[0;31;40m请输入项目编号:\033[0m")
    info = config.get(project, "info")
    return info

if __name__=='__main__':

    info=getparmaiter()
    print(info)