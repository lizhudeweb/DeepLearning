# -*- coding:utf-8 -*-
import os
import paramiko

# 做自动化打包需要配置maven环境变量

# 需要上传服务器的IP地址
serverIp = '139.199.73.14'
# 服务器的登录用户名
serverUser = 'root'
# 服务器的登录密码
serverPwd = 'muguang89n&'

# 需要生成的war名称(最终改成项目名上传的包)
targetFileName = 'muguangsys.war'
# 一般使用maven打包生成后的名称（后续需要操作）
createFileName = 'com.mg.web-0.0.1-SNAPSHOT.war'

# 本地项目根目录 F:\muguangCode\com.mg.web\target
projectPath = r'F:/muguangCode/com.mg.web/'
# 本地项目的target目录(war 或 jar 包生成的目录)
localMkDirPath = projectPath + r'target/'

# 远程服务器路径
remoteFileMkDir = '/opt/abc/'
# 远程服务器下旧war包
remoteFilePath = remoteFileMkDir + targetFileName
# 上传位置
uploadPath = remoteFileMkDir + 'abc.war'

def remove_local_old_file():
    flag = os.path.exists(localMkDirPath + targetFileName)
    if flag:
        os.remove(localMkDirPath + targetFileName)

    flag = os.path.exists(localMkDirPath + createFileName)
    if flag:
        os.remove(localMkDirPath + createFileName)
    print('删除本地旧包----------')

def mvn_package():
    os.chdir(projectPath)
    os.system('mvn package -Dmaven.test.skip=true')
    os.rename(localMkDirPath + createFileName, localMkDirPath + targetFileName)
    print('mvn打包并改名----------')

def remove_remote_file():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(serverIp, username=serverUser, password=serverPwd, allow_agent=True)
    ssh.exec_command("rm -rf " + remoteFileMkDir)
    #ssh.exec_command("rm -rf " + remoteFilePath)
    ssh.close()
    print('删除服务器旧包')

def ftp_upload_file():
    t = paramiko.Transport((serverIp, 22))
    t.connect(username=serverUser, password=serverPwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(localMkDirPath + targetFileName, remoteFilePath, put_call_back)
    t.close()
    print("上传文件----------上传成功")

# 上传文件进度反馈
def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)

if __name__ == '__main__':
    #remove_local_old_file()
    #remove_remote_file()
    #mvn_package()
    ftp_upload_file()



    
