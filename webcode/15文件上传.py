from selenium import webdriver
import time

driver = webdriver.Chrome ()

# 初始化浏览器
url = "http://www.sahitest.com/demo/php/fileUpload.htm"
driver.get ( url )
driver.maximize_window ()

# 文件上传操作
driver.implicitly_wait ( 5 )
element = driver.find_element_by_name
upload = element ( "file" )
time.sleep ( 2 )
upload.send_keys ( r"C:\Users\ROY\Desktop\test_baiduupload.py" )
element ( "submit" ).click ()
time.sleep ( 2 )

# 关闭浏览器节约资源
driver.close ()
driver.quit ()
