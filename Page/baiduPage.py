from common.base import Base

clickButton = ('id', 'su')
searchInput = ('id', 'kw')


class baiduPage(Base):

    def clickButton(self):
        self.click(clickButton)

    def searchInput(self, text):
        self.sendKeys(searchInput, text)


if __name__ == '__main__':
    base = baiduPage()
    base.open()
