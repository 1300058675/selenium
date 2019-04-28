import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime


class readExcel():

    def __init__(self, sheetdata, sheetName="Sheet1"):
        # 打开Excel表格
        # self.data = xlrd.open_workbook(excelPath)
        # self.table = self.data.sheet_by_name(sheetName)
        self.excelPath = '..\\data\\' + sheetdata
        self.sheetName = sheetName

    def get_value(self):  # 传入文件路径字符串即可，例如：get_excel_data('account.xlsx')
        workbook = xlrd.open_workbook(self.excelPath)
        sheet = workbook.sheet_by_name(self.sheetName)
        # sheet = workbook.sheets()[0]  # 读取第一个sheet
        nrows = sheet.nrows  # 行数
        first_row_values = sheet.row_values(0)  # 第一行数据
        list = []
        num = 1
        for row_num in range(1, nrows):
            row_values = sheet.row_values(row_num)
            if row_values:
                str_obj = {}
            for i in range(len(first_row_values)):
                ctype = sheet.cell(num, i).ctype
                cell = sheet.cell_value(num, i)
                if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                    cell = int(cell)  # 浮点转成整型
                    cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
                # 这个代表表格中是日期类型
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(cell, 0))
                    # cell = date.strftime('%Y/%m/%d %H:%M:%S')
                    cell = date.strftime('%Y/%m/%d')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                str_obj[first_row_values[i]] = cell
            list.append(str_obj)
            num = num + 1
        return list


if __name__ == '__main__':
    '''
    获取当前文件位置：os.path.realpath(__file__)
    获取当前位置的上一路径： os.path.dirname()        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    获取路径：filepath = os.path.join(propath,"ddt","data.xlsx")  相当于propath\\ddt\\data.xlsx
    '''
    # propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # filepath = os.path.join(propath, "data", "testdata", "username.xlsx")
    # print(filepath)

    # data = ExcelUtil(filepath, "Sheet1")
    # a = data.dict_data()
    # # print(a['time'])
    # print(data.dict_data())

    b = readExcel()
    c = b.get_value()
    print(c)
