#-*-coding:utf-8 -*-
from selenium import webdriver
import datetime
import threading

# windows
driver = webdriver.Chrome("./win/chromedriver.exe")

# linux 
# driver = webdriver.Chrome("./linux/chromedriver")

# mac
# driver = webdriver.Chrome("./mac/chromedriver")

# ZUCC统一身份认证平台，目标网址为http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html
driver.get("http://ca.zucc.edu.cn/cas/login?service=http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html")
driver.find_element_by_id("username").send_keys("学号")
driver.find_element_by_id("password").send_keys("密码")
driver.find_element_by_class_name("btn-submit").click()

# 表单填充代码，修改所在城市（浏览器中执行js）
driver.execute_script("localStorage.setItem(\"lastSubmit-2\",\"{\\\"tbrq\\\":\\\"2020-02-17\\\",\\\"mqszd\\\":\\\"浙江省 衢州市 龙游县\\\",\\\"sfjcs1\\\":\\\"否\\\",\\\"sfjcs2\\\":\\\"否\\\",\\\"sfdgyq\\\":\\\"否\\\",\\\"sfcyyxgc\\\":\\\"否\\\",\\\"yxgcxx\\\":\\\"\\\",\\\"sfcyjjgl\\\":\\\"否\\\",\\\"jjglxx\\\":\\\"\\\",\\\"xstzk\\\":\\\"否\\\",\\\"jssfjcs1\\\":\\\"否\\\",\\\"jssfjcs2\\\":\\\"否\\\",\\\"jssfdgyq\\\":\\\"否\\\",\\\"jssfcyyxgc\\\":\\\"否\\\",\\\"hzjkm\\\":\\\"绿码\\\"}\")")
driver.refresh()

# 提交（第一次运行无误后取消下方代码注释）
# driver.find_element_by_class_name("btn-commit").click()
# 退出
# driver.quit()