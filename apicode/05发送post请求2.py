import requests

code_url = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"   #  这里的verify很重要,可以携带cookie
url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"  # 时间戳 &t=0.76673587127681

data = {
    "username": "13654548658",  # 注意逗号的位置
    "password": "123123",       # 注意逗号的位置
    "verify_code": "8888"

}
headers = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}


session = requests.session ()

res = session.get ( code_url )
print ( res.headers )
r = session.post ( url, data=data,headers=headers )
print ( r.request.headers )

print(r.status_code)
print ( r.json()['msg'])  #r.json()是将返回的json数据转为字典。
