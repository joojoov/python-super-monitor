# encoding:utf-8
import wmi, os, sys, datetime, time, re
def free_ip():    #获取转码主机清单
    localpath=os.getcwd()
    monitor=os.path.join(localpath,"monitor")
    os.chdir(monitor)
    lists = os.listdir(monitor)
    run_ip=[]
    run = []
    info=[]
    for i in lists:
        if "ok" in i:
            os.remove(i)
            lists.remove(i)
        elif "runing.txt" in i:
            run_ip.append(i.split("_")[0])
            if  i.split("_")[2] not in run:
                run.append(i.split("_")[2])
        elif "information" in i and i !="information.txt":
            info.append(i.split(".")[1])
    for i in info:
        if i not in run:
            os.remove("information.%s.txt"%i)
    print("正在启动项目有：",run)
    file=os.path.join(localpath,"all_ip")
    with open(file,'r+') as file_ip:
        ff=file_ip.readlines()
        print("所有转机数量是：%s    \t\t 在用的数量：%s"%(len(ff),len(run_ip)))
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
    if list == []:
        print("\t抱歉，你已经没有空闲的转码机器")
        sys.exit()
    print("剩余的转码机数量是：", len(list))
    print("剩余转码机IP是",list)
    print("\n\t输入（all）代表所有；（q）代表退出；或者输入具体数量（x）")
    a=input("请选择启动主机数量：")
    if a=="all":
        print("拼命加载。。。。")
    elif a=="q":
        print("\t欢迎下次光临")
        sys.exit()
    elif a.isdigit() == True:
        if int(a)>len(list):
            print("兄弟，资本不够呀，只剩%s台"% len(list))
            sys.exit()
        for i in range(len(list)-int(a)):
            list.pop()
    else :
        print("你是猴子请来的救兵吗？？？")
        sys.exit()
    print("本次转码主机是：",list)
    return list
def Show_soucre():   #获取主机转码目录
    path = "\\\\%s\\FtpServer\\download\\" % (master_ip)
    file_list_convert = os.listdir(path)
    print(file_list_convert)
    convert=input("请输入转码原目录：")
    file_all=os.listdir(os.path.join(path,convert))
    file=os.listdir(os.path.join(path,convert))
    path2="\\\\%s\\FtpServer\\upload\\%s" % (master_ip,convert)
    if os.path.exists(path2):
        ok_list = []
        ok_list2=[]
        file_all2 = os.listdir(path2)
        for i in file_all2:
            ok_list.append(i.split(".")[0])
        for i in range(len(file_all)):
            if file_all[i].split(".")[0] in ok_list:
                ok_list2.append(file_all[i])
        for i in ok_list2:
            file_all.remove(i)
    print("\t当前文夹( %s )总数量是：(%s) , 需要转码数量是：%s"%(convert,len(file),len(file_all)))
    return convert,file_all
def BeginSet(list_machine):  # 初步配置转码所需的各种参数和转码清单
    Upload_filename=file_list(list_machine)
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
    return  Upload_filename
def BeginSet_reboot(list_machine):  # 初步配置转码所需的各种参数和转码清单
    Upload_filename=file_list(list_machine)
    master_share_file = master_local_path.split("\\")[-2]
    with open("information.txt", 'w+') as file:
        for i in [Convert_type, Big_conn, master_ip, master_share_file, Upload_filename,source_ip]:
            file.write(i + "&")
        file.write(open("E:\超级监控服务器\转码参数", 'r+').read())
    file.close()
    return  Upload_filename
def file_list(list_machine):    #生成转码清单
    Upload_filename,line=Show_soucre()
    name = 0
    while line:
        file_path_name = open(str(name) + 'yang.txt', 'a+')
        file_path_name.write(line.pop()+"\n")
        file_path_name.close()
        name += 1
        if name >= len(list_machine):
                name = 0
    for i in range(len(list_machine)):
        try:
            os.rename(str(i) + "yang.txt", str(list_machine[i]) + ".txt")
        except Exception as e:
            print(e)
            print("文件生成失败 %s.txt " % list_machine[i])
    return Upload_filename
def Set_Uploal_file_for_master(Upload_filename):  # 主机生成上传目录文件夹
    conn = wmi.WMI(computer=master_ip, user="daoran", password="daoran")
    try:
        cmd_Control = "cmd /c md  %s" % master_local_path + Upload_filename
        conn.Win32_Process.Create(CommandLine=cmd_Control)
        print("主机(%s)上传目录（%s）创建成功" % (master_ip, Upload_filename))
    except Exception as a:
        print(a)
def Remote_computer(list_machine):   #远程设置定时任务
    Daoran_user = "daoran"
    Daoran_password = "daoran"
    for y in list_machine:
        ipaddress = "192.168.1.%s" % y
        Remote_Boot(ipaddress, Daoran_user, Daoran_password)
        time.sleep(35)
def Get_Start_time():    #生成各转码机开始时间启动

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
def Remote_Boot(ipaddress, Daoran_user, Daoran_password):  #远程定时任务具体命令
    start_date, start_time = Get_Start_time()
    conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
    try:
        auto_start = r"cmd /c schtasks /create /F /sc once /tn yangsheng%s /tr  E:\AutoConvert2\Begin.bat /sd %s /st %s" % (
        start_date.replace('/',''),start_date, start_time)
        conn.Win32_Process.Create(CommandLine=auto_start)
        print("转码机器（192.168.1.%s）预启动成功  开始时间：%s %s" % (ipaddress, start_date, start_time))
        print("拼命加载。。。。")
    except Exception as e:
        print(e)
def test_connect(list_machine):      #测试链接
    print(" \t正在测试链接。。。。")
    for y in list_machine:
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
def connect_control():  # 链接控制
    path="E:\超级监控服务器\connect"
    file=source_ip
    dirs=os.listdir(path)
    if file not in dirs:
        os.mkdir(os.path.join(path,file))
def clear_all():
    path=os.getcwd()
    os.chdir(os.path.join(path,"monitor"))
    for i in os.listdir():
        os.remove(i)
    os.chdir(path)
def for_reboot():
    master_share_file = master_local_path.split("\\")[-2]
    all=os.listdir()
    for i in all:
        if "information" in i and str(i).split(".")[1]!="txt" :
            print("可以从起的项目：%s" %str(i).split(".")[1])
    xiangmu = input("请选择设置重启参数: ")
    with open("information.txt" , 'w+') as file:
        for i in [Convert_type, Big_conn, master_ip, master_share_file, xiangmu, source_ip]:
            file.write(i + "&")
        file.write(open("information.%s.txt" % xiangmu, 'r+').read())
    file.close()
def choose_start():
    way = input("要是重启请输入（1），不是重启就直接回车：")
    if way=="1":
        connect_control()  # 链接控制
        list_machine = free_ip()  # 获取主机列表
        for_reboot()
        Upload_filename = BeginSet_reboot(list_machine)  # 初始化，生成配置文件
        test_connect(list_machine)  # 测试链接
        Set_Uploal_file_for_master(Upload_filename)  # 生成上传目录
        Remote_computer(list_machine)  # 启动转码机
    elif way=="killall":
        clear_all()
        list_machine = free_ip()
        Remote_computer_kill(list_machine)
    else:
        connect_control()  # 链接控制
        list_machine = free_ip()  # 获取主机列表
        Upload_filename = BeginSet(list_machine)  # 初始化，生成配置文件
        test_connect(list_machine)  # 测试链接
        Set_Uploal_file_for_master(Upload_filename)  # 生成上传目录
        Remote_computer(list_machine)  # 启动转码机
def Remote_computer_kill(list_machine):   #远程设置定时任务
    Daoran_user = "daoran"
    Daoran_password = "daoran"
    for y in list_machine:
        ipaddress = "192.168.1.%s" % y
        Remote_kill(ipaddress, Daoran_user, Daoran_password)
def Remote_kill(ipaddress, Daoran_user, Daoran_password):  #远程定时任务具体命令
    conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
    try:
        auto_start = r"cmd /c taskkill /f /im cmd.txt"
        conn.Win32_Process.Create(CommandLine=auto_start)
        print("%s拼命kill。。。。"%ipaddress)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    master_ip = "192.168.1.78"  # 转码主机
    source_ip = master_ip
    master_local_path = "D:\\FtpServer\\upload\\"  # 主机共享文件夹绝对路径
    #master_local_path = "G:\\FtpServer\\upload\\"  # 主机共享文件夹绝对路径
    Big_conn = "2"  # 最大连接数
    Convert_type = ".mp4"  # 转码格式
    choose_start()