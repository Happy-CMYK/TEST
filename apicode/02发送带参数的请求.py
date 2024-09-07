import requests

url = "http://127.0.0.1:8000/api/departments/"

params = {
    "page": "3"
}

headers = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}
r = requests.get ( url, params=params,headers=headers )

print ( r.status_code )   # 状态码

print(r.request.url)
print(r.request.headers)

print ( r.text )
print ( r.content.decode("utf8") )




