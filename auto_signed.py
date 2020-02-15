# -*-coding:utf-8 -*-
from selenium import webdriver
import schedule
import time
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.DEBUG)


def sign_in():
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

    # 表单填充代码，修改所在城市
    driver.execute_script("localStorage.setItem(\"lastSubmit-2\",\"{\\\"tbrq\\\":\\\"2020-02-14\\\",\\\"mqszd\\\":\\\"浙江省 衢州市 龙游县\\\",\\\"sfjcs1\\\":\\\"否\\\",\\\"sfjcs2\\\":\\\"否\\\",\\\"sfdgyq\\\":\\\"否\\\",\\\"sfcyyxgc\\\":\\\"否\\\",\\\"yxgcxx\\\":\\\"\\\",\\\"sfcyjjgl\\\":\\\"否\\\",\\\"jjglxx\\\":\\\"\\\",\\\"xstzk\\\":\\\"否\\\",\\\"jssfjcs1\\\":\\\"否\\\",\\\"jssfjcs2\\\":\\\"否\\\",\\\"jssfdgyq\\\":\\\"否\\\",\\\"jssfcyyxgc\\\":\\\"否\\\"}\")")
    driver.refresh()
    time.sleep(10)
    # 提交（第一次运行无误后取消下方代码注释）
    driver.find_element_by_class_name("btn-commit").click()
    driver.quit()


if __name__ == '__main__':
    logging.info("Application Start")
    schedule.every().day.at("00:10").do(sign_in)
    while True:
        schedule.run_pending()
        time.sleep(1)
