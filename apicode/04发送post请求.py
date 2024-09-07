import requests

url = "http://127.0.0.1:8000/api/departments/"


# json_str是字典,data是关键字,所以data后面用中括号括起来表示值
json_str = {
"data": [
    {
            "dep_id": "测试_26",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
    }
    ]
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}
r = requests.post ( url, json=json_str,headers =headers  )

print ( r.status_code )

print(r.headers)

# print ( r.json()["already_exist"] )

print ( r.json())
print ( r.json()['create_success'])



