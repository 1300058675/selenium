#coding=utf-8
import configparser
import codecs

# class ReadConfig():
#     """
#     专门读取配置文件的，.ini文件格式
#     """
#     def __init__(self):
#         # configpath = os.path.join(prjDir,filename)
#         configpath = '..\\config\\config.ini'
#         # print(configpath)
#         fd = open(configpath)
#         data = fd.read()
#         # remove BOM
#         if data[:3] == codecs.BOM_UTF8:
#             data = data[3:]
#             files = codecs.open(configpath, "w")
#             files.write(data)
#             files.close()
#         fd.close()
#
#         self.cf = configparser.ConfigParser()
#         self.cf.read(configpath)
#
#     def getValue(self, env, name):
#         """
#         [projectConfig]
#         project_path=E:/Python-Project/UItestframework
#         :param env:[projectConfig]
#         :param name:project_path
#         :return:E:/Python-Project/UItestframework
#         """
#         return self.cf.get(env,name)
class ReadConfig():

    def __init__(self):
        self.sFile = '..\\config\\config.ini'
        try:
            self.conf = configparser.ConfigParser()
            self.conf.read(self.sFile)
        except Exception as err:
            raise

    '''
    判断sections是否存在
    '''
    def isExistsSection(self, sections):
        if self.conf.has_section(section = sections):
            return True
        else:
            return False


    '''
    判断option是否存在
    '''
    def isExistsOption(self, section, option):
        if self.conf.has_option(section = section, option = option):
            return True
        else:
            return False


    '''
    获取配置信息的数据，返回string类型
    '''
    def getValue(self, section, option):
        try:
            value=self.conf.get(section, option)
            return value
        except Exception:
            return 0
    '''
    获取配置信息的数据，返回int类型
    '''
    def getIntValue(self, section, option):
        try:
            value = self.conf.getint(section, option)
            return value
        except Exception:
            return 0

    '''
    获取配置信息的数据，返回float类型
    '''
    def getFloatValue(self, section, option):
        try:
            value=self.conf.getfloat(section, option)
            return value
        except Exception:
            return 0

    '''
    获取配置信息的数据，返回bool类型
    '''
    def getBoolValue(self, section, option):
        try:
            value=self.conf.getboolean(section, option)
            return value
        except Exception:
            return 0


    '''
    修改更新数据
    '''
    def UpdateValue(self, section, option, value):
        try:
            self.conf.set(section, option, value)
            with open(self.sFile,'r+') as f:
                self.conf.write(f)
        except Exception:
            return False

    '''
    添加数据
    '''
    def AddValue(self, section, option, value):
        try:
            self.conf.add_section(section)
            self.conf.set(section, option, value)
            with open(self.sFile,'r+') as f:
                self.conf.write(f)
        except Exception:
            return False
