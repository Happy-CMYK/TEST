import requests

r = requests.get ( 'https://github.com/Ranxf' )  # 最基本的不带参数的get请求
r1 = requests.get ( url='http://dict.baidu.com/s', params={'wd': 'python'} )  # 带参数的get请求

requests.get ( 'https://github.com/timeline.json' )  # GET请求
requests.post ( 'http://httpbin.org/post' )  # POST请求
requests.put ( 'http://httpbin.org/put' )  # PUT请求
requests.delete ( 'http://httpbin.org/delete' )  # DELETE请求
requests.head ( 'http://httpbin.org/get' )  # HEAD请求
requests.options ( 'http://httpbin.org/get' )  # OPTIONS请求

print ( r.request.headers )  #
# 打印请求头信息

print ( r.encoding )  # 获取当前的编码
r.encoding = 'utf-8'  # 设置编码
# print ( r.encoding )
print ( r.text )  # 以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
print ( r.content )  # 以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。

print ( r.headers )  # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None

print ( r.status_code )  # 响应状态码
print ( r.raw )  # 返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
print ( r.ok )  # 查看r.ok的布尔值便可以知道是否登陆成功

# *特殊方法*#
# print ( r.json () )              # Requests中内置的JSON解码器，以json形式返回, 前提返回的内容确保是json格式的，不然解析出错会抛异常
print ( r.raise_for_status () )  # 失败请求( 非200响应 )抛出异常
