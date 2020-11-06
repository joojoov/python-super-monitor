# encoding:utf-8
import wmi, os, sys, datetime, time, re

def Show_soucre():
    path = "\\\\%s\\FtpServer\\download\\" % (master_ip)
    file_list_convert = os.listdir(path)
    print(file_list_convert)
    convert=input("请输入转码原目录：")
    file_all=os.listdir(os.path.join(path,convert))
    file=os.listdir(os.path.join(path,convert))
    path2="\\\\%s\\FtpServer\\upload\\" % (master_ip)
    if os.path.exists(path2):
        ok_list = []
        ok_list2=[]
        file_all2 = os.listdir(os.path.join(path2, convert))
        for i in file_all2:
            ok_list.append(i.split(".")[0])
        for i in range(len(file_all)):
            if file_all[i].split(".")[0] in ok_list:
                ok_list2.append(file_all[i])
        for i in ok_list2:
            file_all.remove(i)
    print("当前文夹(%s)总数量是：(%s) ,需要转码数量是：%s"%(convert,len(file),len(file_all)))
    return file_all

def for_reboot():
    localpath=os.getcwd()
    monitor=os.path.join(localpath,"monitor")
    os.chdir(monitor)
    master_share_file = master_local_path.split("\\")[-2]
    all=os.listdir()
    for i in all:
        if "information" in i and str(i).split(".")[1]!="txt" :
            print("可以从起的项目：%s",str(i).split(".")[1])
    xiangmu = input("请选择设置重启参数: ")
    with open("information.txt" , 'w+') as file:
        for i in [Convert_type, Big_conn, master_ip, master_share_file, xiangmu, source_ip]:
            file.write(i + "&")
        file.write(open("information.%s.txt" % xiangmu, 'r+').read())
    file.close()


if __name__ =="__main__":
    master_ip = "192.168.1.171"  # 转码主机
    source_ip = master_ip
    master_local_path = "D:\\FtpServer\\upload\\"  # 主机共享文件夹绝对路径
    master_ip = "192.168.1.78"  # 转码主机
    source_ip = master_ip
    master_local_path = "D:\\FtpServer\\upload\\"  # 主机共享文件夹绝对路径
    Big_conn = "2"  # 最大连接数
    Upload_filename = "55555555555"  # 主机的存放的目录，不得已阿拉伯数字命名
    Convert_type = ".ts"  # 转码格式
    for_reboot()

    #Show_soucre()