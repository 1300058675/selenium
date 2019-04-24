import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    #导入鼠标事件
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.log import Log
from readconfig import ReadConfig

logger = Log()
read_config = ReadConfig()

url = read_config.getValue('testServer', 'URL')
browserName = read_config.getValue('browserType', 'browserName')

class Base(object):

    def __init__(self, browser = browserName, base_url = url):
        try:
            if browser == "Firefox" or browser =="firefox":
                driver = webdriver.Firefox()
                self.driver = driver
                logger.info("正在打开"+browser+"浏览器")
            elif browser == "Chrome" or browser == "chrome":
                driver = webdriver.Chrome()
                self.driver = driver
                logger.info("正在打开"+browser+"浏览器")
            elif browser == "ie" or browser =="IE":
                driver = webdriver.Ie()
                self.driver = driver
                logger.info("正在打开"+browser+"浏览器")
            elif browser == "phantomjs":
                driver = webdriver.PhantomJS()
                self.driver = driver
                logger.info("正在打开"+browser+"浏览器")
            else:
                logger.error("没有发现你所使用的浏览器,你可以使用'firefox','chrome', 'ie' 或者 'phantomjs'")
        except Exception as e: # 捕获所有异常的方方法
            logger.error("%s" % e)

        self.base_url = base_url
        self.timeout =15
        self.t = 0.5


    def open(self):
        '''
        open bbs index . "https://www.baidu.com"
        Usage:
            driver.open()
        '''
        self.driver.get(self.base_url)
        logger.info('open the url  '+self.base_url)


    def find_element(self, locator):
        try:
            logger.info('正在通过==》“'+locator[0]+'”定位元素==》“'+locator[1]+'”')
            element = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            logger.info('“'+locator[0]+'”----“'+locator[1]+'”,定位成功')
            return element
        except Exception as msg:  # 捕获所有异常的方方法
            logger.error('“'+locator[0]+'”----“'+locator[1]+'”,定位失败')


    def find_elements(self, locator):
        try:
            logger.info('正在通过==》“'+locator[0]+'”定位元素==》“'+locator[1]+'”')
            element = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            logger.info('“'+locator[0]+'”----“'+locator[1]+'”,定位成功')
            return element
        except Exception as msg:  # 捕获所有异常的方方法
            logger.error('“'+locator[1]+'”这组元素定位失败')


    def sendKeys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)


    def click(self, locator):
        element = self.find_element(locator)
        element.click()


    def clear(self, locator):
        element = self.find_element(locator)
        element.clear()

    def max_window(self):
        self.driver.maximize_window()
        logger.info('max the window')


    def is_title(self, title):
        '''判断标题(完全)，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            logger.error('URL的标题不一致')


    def is_title_contains(self, title):
        '''判断标题（包含），返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            logger.error('URL的标题不包含'+str(title))


    def is_ElementExist(self, locator):
        '''判定元素是否存在'''
        try:
            self.find_element(locator)
            return True
        except:
            logger.error('元素“'+locator[1]+'”不存在')


    def is_text_element(self, locator, text):
        '''判定某个元素中的text的字符是否和预期一致'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            logger.error('元素“'+locator[1]+'”中的text和预期结果不一致')


    def is_Selected(self, locator):
        '''判断下拉框或者按钮元素是否被选中，返回bool值   例如：判断全选按钮是哦夫选中'''
        try:
            element = self.find_element(locator)
            result = element.is_selected()
            return result
        except:
            logger.error('元素“' + locator[1] + '”未被选中')


    def get_text(self, locator):
        '''获取元素文本'''
        try:
            t = self.find_element(locator).text
            return t
        except:
            logger.error('获取元素“'+locator[1]+'”文本值失败，将输出一个空字符')
            return ''


    def get_value(self,locator):
        '''获取文本框内容'''
        try:
            t = self.find_element(locator).get_attribute('value')
            return t
        except:
            logger.info('获取元素“'+locator[1]+'”文本值失败，将输出一个空字符')
            return ''


    def scroll_bar_bottom(self):
        # 滑动滚动条到底部
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)


    def scroll_bar_top(self):
        js = "window.scrollTo(0,0)"  # 外滑动到顶部
        self.driver.execute_script(js)


    def scroll_bar_left(self):
        js = "window.scrollTo(0,0)"  # 外滑动到最左端
        self.driver.execute_script(js)


    def scroll_bar_right(self):
        js = 'window.scrollTo(document.body.scrollWidth,0)' # 外滑动滚动条到最右端
        self.driver.execute_script(js)


    def scroll_bar_Specified_element(self, locator):
        js = "arguments[0].scrollIntoView();"  # 外滑动滚动条到某个指定的元素"
        Specified_element = self.find_element(locator)
        self.driver.execute_script(js, Specified_element)

    def iframe_frame(self, locator):  # 切换iframe
        iframe = self.find_element(locator)  # 获取iframe
        self.driver.switch_to.frame(iframe)  # 切换至body

    # def window_handles(self):
    #     all = self.driver.window_handles  # 获取全部页面
    #     print(all)
    #     current = self.driver.current_window_handle  # 获取当前页面
    #     print(current)

    def switch_to_window(self, n):
        all = self.driver.window_handles
        self.driver.switch_to_window(all[n])  # 切换页面

    def get_tag(self, locator):
        tag = self.find_element(locator).tag_name  # 获取元素的标签
        return tag

    def alert(self):  # 弹窗
        a = self.driver.switch_to_alert()
        return a

    def is_alert(self):
        '''
        判断是否有alert弹窗，如果有则返回
        switch_to_alert() 定位弹窗
        text()            获取文本值
        accept()          确认
        dismiss()         取消
        send_keys()       输入值
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            # alert = self.driver.switch_to_alert()
            return result
        except:
            return False

    def alert_text(self, text):  # 弹窗  text  确定  取消
        self.driver.switch_to_alert().send_keys(text)


    def mouse_flight(self, locator):  # 鼠标悬停
        mouse = self.find_element(locator)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def double_click(self, locator):  # 鼠标双击
        mouse = self.find_element(locator)
        ActionChains(self.driver).double_click(mouse).perform()


    def check_box(self, locator, m, n):  # 复选框
        '''
        all=driver.find_elements_by_xpath(".//*[@type='checkbox']")
        for i in all:
           i.click()
        '''
        all = self.find_elements(locator)
        for i in all[m:n]:
            i.click()

    def File_upload(self,text):  # 文件上传,test传文件路径（.au3转换的.exe）
        relesefile = text
        os.system(relesefile)

    def readonly(self, locator):  # 针对Id
        js = "document.getElementBy"+locator[0].title()+"('"+locator[1]+"').removeAttribute('readonly');"
        self.driver.execute_script(js)

    def drag_and_drop(self, el_locator, ta_locator):
        '''
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("locator=>#el","locator=>#ta")
        '''
        element = self.find_element(el_locator)
        target = self.find_element(ta_locator)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

if __name__ == '__main__':
    base = Base()
    base.open()
    base.max_window()
    base.find_element(('id', 'su'))
    base.sendKeys(('id', 'kw'), 'haha')
























