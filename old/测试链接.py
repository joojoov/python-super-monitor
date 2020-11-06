# encoding:utf-8
import wmi, os, sys, datetime, time, re
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
def free_ip():
    start_date, start_time =  Get_Start_time()
    with open("测试ip","r+") as ip:
        all_ip=ip.readlines()
        print(all_ip)
    for i in all_ip:
        ipaddress = i.strip()
        Daoran_user = "daoran"
        Daoran_password = "daoran"
        conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
        try:
           # auto_start = r"cmd /c  cd / E:\AutoConvert"
            auto_start = r"cmd /c schtasks /create /F /sc once /tn yangsheng%s /tr  E:\AutoConvert\Begin.bat /sd %s /st %s" % (
                start_date.replace('/', ''), start_date, start_time)
            #  auto_start = r"cmd /c shutdown -s "
            conn.Win32_Process.Create(CommandLine=auto_start)
            print("转码机器（%s）预启动成功  开始时间：%s %s" % (ipaddress, start_date, start_time))
        except Exception as e:
            print(ipaddress, "链接失败")
            print(e)
            sys.exit()



if __name__ == '__main__':
    free_ip()