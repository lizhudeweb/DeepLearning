from urllib import request

resp = request.urlopen('http://www.baidu.com')

#str = resp.read().decode('utf-8')

#f = open('2.html','w',encoding='utf-8')

#f.write(str)

#f.close()
print(resp.read().decode("utf-8"))
