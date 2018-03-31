# -*- coding:utf-8 -*-
import os
import paramiko

# 利用Python将java的maven项目自动生成war包或者jar包 并自动上传至服务器（一般放在tomcat的 webapp 目录下会自动解压）
# 做自动化打包需要配置maven环境变量

# 需要上传服务器的IP地址
serverIp = 'xxx.xx.xxx.xx'
# 服务器的登录用户名
serverUser = 'root'
# 服务器的登录密码
serverPwd = '123456'
# 需要生成的war名称(最终改成项目名上传的包)
targetFileName = 'xxx.war'
# 一般使用maven打包生成后的名称（后续需要操作）
createFileName = 'xxx-0.0.1-SNAPSHOT.war'
# 本地项目根目录
projectPath = r'/D/work/xx(项目)/'
# 本地项目的target目录(war 或 jar 包生成的目录)
localMkDirPath = projectPath + r'target/'
# 远程服务器的tomcat路径  xxx是你war解压的文件夹  一般war上传至tomcat下 会直接解压
remoteFileMkDir = '/usr/local/tomcat/webapps/xxx'
# 远程服务器下旧war包
remoteFilePath = remoteFileMkDir + targetFileName

# 删除本地旧包
def remove_local_old_file():
    flag = os.path.exists(localMkDirPath + targetFileName)
    if flag:
        os.remove(localMkDirPath + targetFileName)

    flag = os.path.exists(localMkDirPath + createFileName)
    if flag:
        os.remove(localMkDirPath + createFileName)
    print

# mvn 命令打包  先进入目录下  再执行打包命令并改名
def mvn_package():
    os.chdir(projectPath)
    os.system('mvn package -Dmaven.test.skip=true')
    os.rename(localMkDirPath + createFileName, localMkDirPath + targetFileName)
    print

# 远程删除服务器的tomcat下的旧包 和文件夹
def remove_remote_file():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(serverIp, username=serverUser, password=serverPwd, allow_agent=True)
    ssh.exec_command("rm -rf " + remoteFileMkDir)
    ssh.exec_command("rm -rf " + remoteFilePath)
    print

# 上传文件
def ftp_upload_file():
    t = paramiko.Transport((serverIp, 22))
    t.connect(username=serverUser, password=serverPwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(projectPath + targetFileName, remoteFilePath, put_call_back)
    t.close()
    print("上传成功")

# 上传文件进度反馈
def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)

# 具体更新文件的步骤
# 1.先查询本地之前是否存在老的项目包 如存在则先删除
# 2.使用maven 命令将项目打包 并改名（也可以不改名 看个人需求）
# 3.先将服务器tomcat目录下的旧war包删除（也可以自己下载备份 服务器log也可做相同操作）
# 4.将本地最新项目更新到服务器

if __name__ == '__main__':
    remove_local_old_file()
    remove_remote_file()
    mvn_package()
    ftp_upload_file()