# @Time : 2022/4/15 16:57
# @Author : Liang er qian
# @File : all.py
import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')


