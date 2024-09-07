import requests

url = "https://www.google.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}

r = requests.get ( url, timeout=3,headers=headers)

print ( r.status_code )
