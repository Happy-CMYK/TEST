import requests

url = "https://www.baidu.com"

response = requests.get ( url )

print ( response.url )  #  请求的地址
print ( response.content.decode ( "utf8" ) )
print ( response.request.body )  #请求体
print ( response.request.body )   #请求体


print ( response.headers ) #响应头
print ( response.request.headers )  #请求头


# print ( response.text )
