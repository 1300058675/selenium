# selenium
unittest + selenium  framework


# 框架结构
Framework
---Page
---case
---common
---config                //配置文件
---data       
---report
------log                //日子文件
------testreport         //html报告
---run


# 截图问题
应为htmlrunner 断言失败截图需要webdriver.Chrome()
driver = getattr(test, "driver")
test.imgs.append(driver.get_screenshot_as_base64())



在unittest调用open方法时，对self.driver赋值
self.basepage = Base()
self.driver = self.basepage.open()
open() 打开url链接，并返回driver对象

