# -*-coding:utf-8 -*-
from selenium import webdriver
import schedule
import time

def sign_in():
    # 打开chrome页面
    driver = webdriver.Chrome()

    # ZUCC统一身份认证平台，目标网址为http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html
    driver.get("http://ca.zucc.edu.cn/cas/login?service=http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html")
    driver.find_element_by_id("username").send_keys("学号")
    driver.find_element_by_id("password").send_keys("密码")
    driver.find_element_by_class_name("btn-submit").click()

    # 表单填充代码（浏览器中执行js无异常）
    # driver.execute_script("document.getElementsByName('mqszd')[0].value=\"浙江省 衢州市 龙游县\";\n" +
    #                     "document.getElementsByName('sfjcs1')[1].checked=true;\n" +
    #                     "document.getElementsByName('sfjcs2')[1].checked=true;\n" +
    #                     "document.getElementsByName('sfdgyq')[1].checked=true;\n" +
    #                     "document.getElementsByName('sfcyyxgc')[1].checked=true;\n" +
    #                     "document.getElementsByName('sfcyjjgl')[1].checked=true;\n" +
    #                     "document.getElementsByName('xstzk')[1].checked=true;\n" +
    #                     "document.getElementsByName('jssfjcs1')[1].checked=true;\n" +
    #                     "document.getElementsByName('jssfjcs2')[1].checked=true;\n" +
    #                     "document.getElementsByName('jssfdgyq')[1].checked=true;\n" +
    #                     "document.getElementsByName('jssfcyyxgc')[1].checked=true;")

    # 提交（第一次运行无误后取消下方代码注释）
    driver.find_element_by_class_name("btn-commit").click()
    driver.quit()


if __name__ == '__main__':
    schedule.every().day.at("00:10").do(sign_in)
    while True:
        schedule.run_pending()
        time.sleep(1)
