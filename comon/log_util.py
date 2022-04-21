# @Time : 2022/4/18 17:09
# @Author : Liang er qian
# @File : log_util.py
import logging
import os
import time

curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(curpath, 'logs')


class Logger(logging.Logger):

    def __init__(self, name='root', level='DEBUG', file=None, format=None):
        super().__init__(name)
        self.setLevel(level)
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置文件处理器，日志输出到文件
        file = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = Logger(name='',
                level='DEBUG',
                format='%(filename)s-[LineNo:%(lineno)d]-%(asctime)s-%(levelname)s-%(message)s')