# @Time : 2022/4/15 15:36
# @Author : Liang er qian
# @File : test_demo.py


import pytest

class TestDemo:


    def test_demo01(self):
        print('这是第一个试用')

    # @pytest.mark.parametrize('case',['第一个','第二个','第三个'])
    # def test_many_case01(self,case):
    #     print(case) # 第一个  第二个  第二个
    #
    @pytest.mark.parametrize('case',[{'name':18},{'name':25},{'name':12}])
    def test_many_case02(self,case):
        print(case,type(case)) # ['妹妹', 18] ['哥哥', 25]
        age=case['name']
        print(age)


    # @pytest.mark.parametrize('nickname,age',[['妹妹',18],['哥哥',25]])
    # def test_many_case03(self,nickname,age):
    #     print(nickname,age) # 妹妹 18  哥哥 25

    @pytest.mark.smoke
    def test_step01(self):
        print('冒烟第一步')

if __name__ == '__main__':
    pytest.main()

# ll=[{'name':18},{'name':25},{'name':12}]
# print(type(ll))  list