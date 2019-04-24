from common import myunit
from common.readExcel import readExcel

readExcel = readExcel('login_data.xlsx', 'Sheet2')
a = readExcel.get_value()
print(a)

class Login_one(myunit.Myunit):

    def test01(self):
        name=('d','account')
        password=('name','password')
        submit=('id','submit')
        self.zendao.sendKeys(name,'test1')
        self.zendao.sendKeys(password, '123456')
        self.zendao.click(submit)


    def test02(self):
        name = ('id', 'account')
        password = ('name', 'password')
        submit = ('id', 'submit')
        self.zendao.sendKeys(name, 'test2')
        self.zendao.sendKeys(password, '123456')
        self.zendao.click(submit)

    def test03(self):
        name = ('id', 'account')
        password = ('name', 'password')
        submit = ('id', 'submit')
        self.zendao.sendKeys(name, 'test3')
        self.zendao.sendKeys(password, '123456')
        self.zendao.click(submit)
