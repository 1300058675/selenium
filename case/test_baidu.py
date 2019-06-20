from common import myunit
from common.readExcel import readExcel
import ddt
import unittest

readExcel = readExcel('login_data.xlsx')
success_list = readExcel.get_value()


@ddt.ddt
class Search_Baidu(myunit.Myunit):

    '''百度搜索测试'''
    @ddt.data(*success_list)
    def test01(self, data):
        '''通过断言 java_百度搜索判断'''
        self.basepage.searchInput(data['search'])
        self.basepage.clickButton()
        assert_value = self.basepage.is_title(data['search'] + '1_百度搜索')
        self.assertTrue(assert_value)

    @ddt.data(*success_list)
    def test02(self, data):
        '''通过断言 java_百度搜索判断'''
        self.basepage.searchInput(data['search'])
        self.basepage.clickButton()
        assert_value = self.basepage.is_title(data['search'] + '_百度搜索')
        self.assertTrue(assert_value)

    @ddt.data(*success_list)
    def test03(self, data):
        '''通过断言 java_百度搜索判断'''
        self.basepage.searchInput(data['search'])
        self.basepage.clickButton()
        assert_value = self.basepage.is_title(data['search'] + '_百度搜索')
        self.assertTrue(assert_value)


if __name__ == '__main__':
    unittest.main()
