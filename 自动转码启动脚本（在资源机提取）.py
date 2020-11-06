# encoding:utf-8
import wmi, os, sys, datetime, time, re
def free_ip():
    localpath=os.getcwd()
    monitor=os.path.join(localpath,"monitor")
    os.chdir(monitor)
    lists = os.listdir(monitor)
    run = []
    info=[]
    for i in lists:
        if "ok" in i:
            os.remove(i)
            lists.remove(i)
        elif "runing.txt" in i:
            if  i.split("_")[2] not in run:
                run.append(i.split("_")[2])
        elif "information" in i and i !="information.txt":
            info.append(i.split(".")[1])
    for i in info:
        if i not in run:
            os.remove("information.%s.txt"%i)
    for i in info:
        if i not in run:
            os.remove("information.%s.txt"%i)
    print("正在启动项目有：",run)
    file=os.path.join(localpath,"all_ip")
    with open(file,'r+') as file_ip:
        ff=file_ip.readlines()
        print("所有主机数量是：",len(ff))
        list=[]
        for i in ff:
            list.append(int(i.strip().split(".")[-1]))
        list.sort()
    file_ip.close()
    with open(file,"w+") as file:
        for i in list:
            file.write("192.168.1."+str(i)+"\n")
    file.close()
    new=[]
    for i in range(len(lists)):
        for b in range(len(list)):
            if str(list[b]) in lists[i]:
                new.append(list[b])
    for i in new:
        list.remove(i)
    print("剩余的主机数量是：" ,len(list))
    if list == []:
        print("\t抱歉，没有空闲的转码机器")
        sys.exit()
    print("剩余主机IP是",list)
    print("\n\t输入（all）代表所有；（q）代表退出；或者输入具体数量\t")
    a=input("请选择启动主机数量：")
    if a=="all":
        print("拼命加载。。。。")
    elif a.isdigit() == True:
        if int(a)>len(list):
            print("兄弟，资源不够呀，只剩%s台"% len(list))
            sys.exit()
        for i in range(len(list)-int(a)):
            list.pop()
    else :
        print("逗逼,乱来是吗？？？")
        sys.exit()
    print("本次转码主机是：",list)
    return list
def BeginSet():  # 初步配置转码所需的各种参数和转码清单
    master_share_file = master_local_path.split("\\")[-2]
    with open("information.txt", 'w+') as file:
        for i in [Convert_type, Big_conn, master_ip, master_share_file, Upload_filename,source_ip]:
            file.write(i + "&")
        file.write(open("E:\超级监控服务器\转码参数", 'r+').read())
    file.close()
    with open("information.%s.txt" % Upload_filename, 'w+') as file:
        for i in [Convert_type, Big_conn, master_ip, master_share_file, Upload_filename, source_ip]:
            file.write(i + "&")
        file.write(open("E:\超级监控服务器\转码参数", 'r+').read())
    file.close()
    file_list()
def file_list():
    with open("E:\超级监控服务器\path.txt", 'r+') as convert_file:
        line = convert_file.readline()
        name = 0
        while line:
            file_path_name = open(str(name) + 'yang.txt', 'a+')
            file_path_name.write(line)
            file_path_name.close()
            name += 1
            if name >= len(list_machine):
                name = 0
            line = convert_file.readline()
        convert_file.close()
    for x in range(len(list_machine)):
        try:
            os.rename(str(x) + "yang.txt", str(list_machine[x]) + ".txt")
        except Exception as e:
            print(e)
            print("文件生成失败 %s.txt " % list_machine[x])
def Set_Uploal_file_for_master():  # 主机生成上传目录文件夹
    conn = wmi.WMI(computer=master_ip, user="daoran", password="daoran")
    try:
        cmd_Control = "cmd /c md  %s" % master_local_path + Upload_filename
        conn.Win32_Process.Create(CommandLine=cmd_Control)
        print("主机(%s)上传目录（%s）创建成功" % (master_ip, Upload_filename))
    except Exception as a:
        print(a)
def Remote_computer():
    Daoran_user = "daoran"
    Daoran_password = "daoran"
    for  y in list_machine:
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
        auto_start = r"cmd /c schtasks /create /F /sc once /tn yangsheng%s /tr  E:\AutoConvert\Begin.bat /sd %s /st %s" % (
        start_date.replace('/',''),start_date, start_time)
      #  auto_start = r"cmd /c shutdown -s "
        conn.Win32_Process.Create(CommandLine=auto_start)
        print("转码机器（%s）预启动成功  开始时间：%s %s" % (ipaddress, start_date, start_time))

    except Exception as e:
        print(e)
def try_to_connect():
    print(" \t正在测试链接。。。。")
    for i in list_machine:
        ipaddress = "192.168.1.%s" % i
        Daoran_user = "daoran"
        Daoran_password = "daoran"
        try:
            conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
            print(ipaddress, "成功")
        except Exception as e:
            print(ipaddress, "链接失败")
            print("请检查网落")
            sys.exit()
def connect_file():
    path="E:\超级监控服务器\connect"
    file=source_ip
    dirs=os.listdir(path)
    if file not in dirs:
        os.mkdir(os.path.join(path,file))
if __name__ == '__main__':
    source_ip="192.168.1.218"  #提取资源主机的ip,
    master_ip = "192.168.1.216"  #（78；234；170；171；5） 转码主机ip 78江苏移动&新歌，243陕西广电，170广东广电&广西广电，171ott
    master_local_path = "D:\\AutoConvert\\"  # 主机共享文件夹绝对路径
    Big_conn = "2"  # 最大连接数
    Upload_filename = ""  # 主机的存放的目录
    Convert_type = ".ts"  # 转码格式
    connect_file()
    list_machine=free_ip()
    try_to_connect()
    BeginSet()
    Set_Uploal_file_for_master()
    Remote_computer()