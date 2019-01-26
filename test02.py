#coding=UTF-8
import urllib.request

response=urllib.request.urlopen("https://www.python.org")
#print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


import urllib.parse
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response1=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response1.read())