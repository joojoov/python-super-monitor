# -*- coding: utf-8 -*-
import os
def Get_list_of_file(dir,filelist):
    for s in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,s)):
            filelist.append(os.path.join(dir,s))
        elif os.path.isdir(os.path.join(dir,s)):
            Get_list_of_file(os.path.join(dir,s),filelist)
    return filelist
if __name__=='__main__':
    li=Get_list_of_file('F:\Python27',[] )
    for i in range(len(li)):
        if li[i].split('.')[-1]=='mp4':
            print(li[i])

