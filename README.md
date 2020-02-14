# ncp-sign-in
ZUCC NCP疫情钉钉自动健康打卡脚本

请按实填写表单！为自己和他人的健康负责。

## Getting Started
- 安装Python3.x环境
- 安装`selenium`依赖：
  ```
  pip install --user selenium
  ```
- 修改`signed.py`脚本中的账号密码（统一身份认证），按需要取消填充表单代码注释（修改注释代码中的所在地）
- 按自己的操作系统，修改`signed.py`脚本中调用的chromedriver
- 第一次运行时，注释提交表单的代码，查看登录和表单填写是否正常

## 定时执行
在定时执行前，一定要先手动执行一次`signed.py`，保证填表数据正常

**系统定时**
- 取消`signed.py`中提交和退出的代码注释
- 创建系统定时任务

**python定时**
- 安装`schedule`模块
  ```
  pip install --user schedule
  ```
- 修改`auto_signed.py`中的账号密码（统一身份认证），按需要取消填充表单代码注释（修改注释代码中的所在地）
- 按自己的操作系统，修改`auto_signed.py`脚本中调用的chromedriver
- 修改打卡时间
- 运行`auto_signed.py`，自动签到

## License
CatMock is available under the terms of the [MIT License](https://opensource.org/licenses/MIT).

