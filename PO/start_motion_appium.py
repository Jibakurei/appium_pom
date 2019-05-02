import win32api
import os
import time

class start_motion_appium:
    def start_motion(self):
        d = ('start D:\Genymotion\player.exe --vm-name "Custom Phone - 8.0 - API 26 - 768x1280"')
        # motion = r'.\Data\motion_start.bat'
        os.popen(d)
        time.sleep(20)
    def start_appium(self):
        a = ('start appium&')
        os.popen(a)
    
    def kill_motion(self):
        process = os.popen("netstat -aon|findstr 6379").read()
        pid = process.replace('  ','').split(" ")[2]
        print(pid)
        m = os.popen("taskkill -f -pid %s" % pid)
        print(m.read())

    def kill_appium(self):
        process = os.popen("netstat -aon|findstr 4723").read()
        pid = process.replace('  ','').split(" ")[2]
        print(pid)
        m = os.popen("taskkill -f -pid %s" % pid)
        print(m.read())

    