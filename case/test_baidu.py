from common import myunit
from common.readExcel import readExcel
import ddt
import unittest

readExcel = readExcel('login_data.xlsx')
success_list = readExcel.get_value()
print(success_list)

@ddt.ddt
class Search_Baidu(myunit.Myunit):

    @ddt.data(*success_list)
    def test01(self, data):
        self.basePage.searchInput(data['search'])
        self.basePage.clickButton()
        assert_value = self.basePage.is_title(data['search']+'_百度搜索')
        self.assertTrue(assert_value)


if __name__ == '__main__':
    unittest.main()