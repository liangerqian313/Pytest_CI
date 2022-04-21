# @Time : 2022/4/16 18:28
# @Author : Liang er qian
# @File : yaml_util.py
import yaml


class YamlUtil:

    def __init__(self, yaml_file):
        """
        通过init方法把yaml文件传入到当前类中
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        读取yaml,对yaml进行反序列化(把yaml格式转换成字典格式)
        :return:
        """
        with open(r'D:\Casedemo\pytest\yaml_case\test_login.yaml', encoding='utf-8') as file:
            value = yaml.load(file, Loader=yaml.FullLoader)
            return value


if __name__ == '__main__':
    print(YamlUtil('test_login.yaml').read_yaml())