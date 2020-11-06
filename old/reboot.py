# encoding:utf-8
import wmi, os, sys, datetime, time, re

def all_to_stop(ipaddress, Daoran_user, Daoran_password):
    conn = wmi.WMI(computer=ipaddress, user=Daoran_user, password=Daoran_password)
    try:
        auto_start = r"cmd /c taskkill /F /IM cmd.exe"
        conn.Win32_Process.Create(CommandLine=auto_start)
        print("转码机器（%s）预启动成功 " % (ipaddress))
    except Exception as e:
        print(e)