from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
sleep(5)
driver.add_cookie({"name":'BDUSS',"value":'klrZ2dFOTRtNVRCU3kzOG9rRlRNanYxMGxEaFcwb1pOQjVMTkFEdTM0MWhyRmhrSVFBQUFBJCQAAAAAAAAAAAEAAAD-y1rq0arIvrrazcMwNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEfMWRhHzFka'})
driver.add_cookie({"name":'BAIDUID',"value":'BD27231253777F78CA7DE324AA7FA70A:FG=1'})
sleep(10)
driver.refresh()
sleep(5)