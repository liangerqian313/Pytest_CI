# @Time : 2022/4/18 14:29
# @Author : Liang er qian
# @File : excel_util.py
import os

import openpyxl


class CaseData(object):
    def __init__(self, dict_case):
        for i in dict_case.items():
            setattr(self, i[0], i[1])


class ExcelUtil:

    def get_objrct_path(self):
        return os.path.abspath(os.path.dirname(__file__)).split('comon')[0]

    def read_excel(self, sheet_name):
        wb = openpyxl.load_workbook(self.get_objrct_path() + '/data/case.xlsx')
        sh = wb[sheet_name]
        all_case = []
        rows = list(sh.rows)
        titles = []
        for cell in rows[0]:
            titles.append(cell.value)
        # print(titles)  ['case_id', 'case_title', 'username', 'password']
        for row in rows[1:]:
            data = []
            for v in row:
                data.append(v.value)
            # print(data) #[1, '输入正确的用户名和密码', 'admin', 'admin']
            case_zip = dict(zip(titles, data))
            # print(type(case_zip),case_zip)  #{'case_id': 1, 'case_title': '输入正确的用户名和密码', 'username': 'admin', 'password': 'admin'}
            # pack = CaseData(case_zip)
            all_case.append(case_zip)
        # print(all_case,type(all_case))
        return all_case


if __name__ == '__main__':
    ExcelUtil().read_excel('login')
