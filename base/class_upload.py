# -*- coding:utf-8 -*-
import os
import paramiko
import time
 
class SSHConnection(object):
    
    #项目目录
    projectRootPath = r'D:/muguangCode/'
    #项目war目录(war 或 jar 包生成的目录)
    warPath = projectRootPath + r'com.mg.web/target/com.mg.web-0.0.1-SNAPSHOT.war'
    bgPath = projectRootPath + r'com.mg.backgroud/target/com.mg.backgroud-0.0.1-SNAPSHOT.war'

    toWarPath = '/home/muguang/soft/tomcat8/com.mg.web-0.0.1-SNAPSHOT.war'
    toBgPath = '/home/muguang/soft/tomcat8/com.mg.backgroud-0.0.1-SNAPSHOT.war'
    
    def __init__(self, host='139.199.73.14', port=22, username='root',pwd='muguang89n&'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None
 
    def run(self):
        self.getArgument()  # 连接远程服务器
        self.connect()  # 连接远程服务器
        #self.package()
        self.upload()

        self.cmd('df')  # 执行df 命令
        self.cmd('sh ./../home/muguang/cc.sh')  # 执行df 命令
        self.close()    # 关闭连接
 
    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()
        
    def getArgument (self):
        str = input("“” or “b” or “all”\n");
        if str == "":
            self.flag = 0
            print ("前台...")
        elif str == "b":
            self.flag = 1
            print ("后台...")
        elif str == "all":
            self.flag = 2
            print ("all in...")
            
    def package(self):
        flag = os.path.exists(self.warPath)
        if flag:
            os.remove(self.warPath)
            print('删除本地旧包----------')        
        os.chdir('D:/muguangCode/com.mg.web/')
        os.system('mvn package -Dmaven.test.skip=true -Dspring.active.profile=dev')
        #os.rename(localMkDirPath + createFileName, localMkDirPath + targetFileName)
        print('mvn打包----------')
 
    def upload(self):
        time_start=time.time()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        if self.flag == 0:
            sftp.put(self.warPath, self.toWarPath, put_call_back)
        elif self.flag == 1:
            sftp.put(self.bgPath, self.toBgPath, put_call_back)
        elif self.flag == 2:
            sftp.put(self.warPath, self.toWarPath, put_call_back)
            sftp.put(self.bgPath, self.toBgPath, put_call_back)
        time_end=time.time()
        print('totally cost',time_end-time_start)
        
    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        print(result)
        return result


def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)
        
obj = SSHConnection()
obj.run()



    
