# encoding:utf-8
import wmi, os, sys, datetime, time, re

def Remote_computer():
    Daoran_user = "daoran"
    Daoran_password = "daoran"
    for x, y in list_machine:
        ipaddress = "192.168.1.%s" % y
        Remote_Boot(ipaddress, Daoran_user, Daoran_password)
        time.sleep(35)

def Get_Start_time():

    a = datetime.datetime.now()
    year, month, day, hour, minute, second, other = re.split('[-\.: ]', str(a))
    start_day, start_time = "%s/%s/%s" % (year, month, day), "%s:%02d:%s" % (hour, int(minute) +2, second)
    if int(minute) + 2 >= 60:
        start_time = "%02d:01:%s" % (int(hour) + 1, second)
        if int(minute) + 2 ==60:
            start_time = "%02d:00:%s" % (int(hour) + 1, second)
        if int(hour) + 1 >= 24:
            start_day, start_time = "%s/%s/%0sd" % (year, month, int(day) + 1), "00:01:%s" % second

    return start_day, start_time

def Remote_Boot(ipaddress, Daoran_user, Daoran_password):
    start_date, start_time = Get_Start_time()
    conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
    try:
        auto_start = r"cmd /c schtasks /create /F /sc once /tn yang%s /tr  E:\convert_2\VideoConvert\convert_run.bat  /sd %s /st %s" % (
        start_time.replace(':','-'),start_date, start_time)
        conn.Win32_Process.Create(CommandLine=auto_start)
        print("转码机器（192.168.1.%s）预启动成功  开始时间：%s %s" % (ipaddress, start_date, start_time))
    except Exception as e:
        print(e)


def try_to_connect():
    print(" \t正在测试链接。。。。")
    for x, y in list_machine:
        ipaddress = "192.168.1.%s" % y
        Daoran_user = "daoran"
        Daoran_password = "daoran"
        try:
            conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
            print(ipaddress, "成功")
        except Exception as e:
            print(ipaddress, "链接失败")
            print("请检查网落")
            sys.exit()

    Remote_computer()


if __name__ == '__main__':
    master_ip = "192.168.1.171"  # 转码主机
    master_local_path = "G:\\AutoConvert2\\"  # 主机共享文件夹绝对路径
    Big_conn = "2"  # 最大连接数
    Upload_filename = "甘肃电信500"  # 主机的存放的目录
    Convert_type = ".ts"  # 转码格式
    #list_machine = [[1, 54], [2, 78], [3, 105],[4, 170], [5, 177], [6, 193], [7, 203], [8, 222], [9, 228], [10, 243]]
    list_machine =[[1,54], [ 2,78],[3,105],[4, 228],[5,148],[6,243],
                  [7,170], [8,62],[9,201],[10,203],[11,215],[12,222]]
    try_to_connect()
