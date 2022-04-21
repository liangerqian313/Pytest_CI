#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/20 8:57
# @Author : 
# @Version：V 0.1
# @File : HandlerCheck.py
# @desc :
import json

from comon.HandlerJson import Json
from comon.log_util import logger


class JsonCompare:
    def __init__(self):
        self.data_compare_result = []  # 数据对比结果
        self.frame_cmpare_result = []  # 结构对比结果
    def cmp(self, expect_data, real_data, path='/'):
        """
        比较json
        :param expect_data: 预期
        :param real_data: 实际
        :return:
        """
        try:
            if not isinstance(expect_data, (list, tuple, dict)):
                if not expect_data == real_data:
                    msg = '%s:预期值:%s%s,实际值:%s%s' % (
                        path, str(expect_data), type(expect_data), str(real_data), type(real_data))
                    self.data_compare_result.append(msg)
            # list tuple
            elif isinstance(expect_data, (list, tuple)):
                if not isinstance(real_data, (list, tuple)):
                    raise IndexError('实际数据不是list:%s' % path)  # 实际数据为非list/tuple类型
                for index, value in enumerate(expect_data):
                    try:
                        if index < len(real_data):
                            self.cmp(value, real_data[index], '%s[%d]' % (path, index))
                        else:
                            raise IndexError('不存在的下标：%s[%d]' % (path, index))
                    except Exception as e:
                        if IndexError:
                            self.frame_cmpare_result.append('结构异常or数据缺失:%s' % e.args)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s' % e.args)
            # dict
            else:
                if not isinstance(real_data, dict):
                    raise IndexError('实际数据不是dict:%s' % path)  # 实际数据为非dict类型
                for key, value in expect_data.items():
                    try:
                        if key in real_data.keys():
                            self.cmp(value, real_data[key], '%s[\'%s\']' % (path, str(key)))
                        else:
                            raise IndexError('不存在的键：%s[\'%s\']' % (path, str(key)))
                    except Exception as e:
                        if IndexError:
                            e = '接口返回-》结构异常or数据缺失:%s' % e.args
                            self.frame_cmpare_result.append(e)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s' % e.args)
        except Exception as e:
            self.frame_cmpare_result.append('未知异常:%s' % e.args)
        # for i in self.data_compare_result:
        #     logger.info('data_compare_result:{}'.format(i))
        # for i in self.frame_cmpare_result:
        #     logger.info('frame_cmpare_result:{}'.format(i))
        return self.data_compare_result, self.frame_cmpare_result

    def check(self, res, Expect):
        _expect = dict([i.split("=") for i in Expect.split(';')])
        _res = res.content.decode(encoding="utf-8")
        for k, v in _expect.items():
            logger.info('{0},{1}'.format(k, v))
            # 接口状态码
            # if k == 'status_code':
            #     assert int(res.status_code) == int(v)
            logger.info('预期：【{0}】,【{1}】'.format(k, v))
            real_expect = Json().get_json_value_by_key(json.loads(res.content), k)
            logger.info('实际：【{0}】,【{1}】'.format(k, real_expect))
            assert real_expect == v

    def check_assert_code(self, code, exp_code):
        """
        检查返回码
        :param code: 实际返回code
        :param exp_code: 预期code
        :return:
        """
        try:
            assert int(code) == int(exp_code)
            return True
        except:
            raise Exception('Code 异常,【实际Code：{0}】,【预期Code：{1}】', format(code, exp_code))

    def check_assert_in_body(self, body, exp_body):
        """
        检查返回数据是否包含预期数据
        :param body:
        :param exp_body:
        :return:
        """
        try:
            body_json = json.dumps(body)
            assert exp_body in body_json
            return True
        except:
            raise Exception('body 异常,【实际body：{0}】,【预期exp_body：{1}】', format(body, exp_body))
if __name__ == '__main__':
    a={"code":1,"results":{"ip":"58.40.90.206","country":"中国","continent":"Asia","subContinent":"Eastern Asia","province":"Shanghai","city":"Shanghai","latlng":[31.222219,121.458061],"zipcode":"200020","tld":[".cn",".中国",".中國",".公司",".网络"],"cca2":"CN","cca3":"CHN","currency":["CNY"],"callingCode":["86"],"capital":"Beijing","languages":{"zho":"Chinese"},"borders":["阿富汗","不丹","缅甸","香港","印度","哈萨克斯坦","尼泊尔","朝鲜","吉尔吉斯斯坦","老挝","澳门","蒙古","巴基斯坦","俄罗斯","塔吉克斯坦","越南"],"flag":"🇨🇳","flagUrl":"https://static.webmasterapi.com/images/country-flags/svg/cn.svg","wiki":"https://en.wikipedia.org/wiki/China","user_agent":{"ua":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36","browser":{"name":"Chrome","version":"83.0.4103.116","major":"83"},"engine":{"name":"Blink","version":"83.0.4103.116"},"os":{"name":"Windows","version":"10"},"device":{},"language":"zh","locale":"zh-CN"}}}
    b={"code":1,"results":{"ip":"58.40.90.206","country":"中国","continent":"Asia","subContinent":"Eastern Asia","province":"Shanghai","city":"Shanghai","latlng":[31.222219,121.458061],"zipcode":"200020","tld":[".cn",".中国",".中國",".公司",".网络"],"cca2":"CN","cca3":"CHN","currency":["CNY"],"callingCode":["86"],"capital":"Beijing","languages":{"zho":"Chinese"},"borders":["阿富汗","不丹","缅甸","香港","印度","哈萨克斯坦","尼泊尔","朝鲜","吉尔吉斯斯坦","老挝","澳门","蒙古","巴基斯坦","俄罗斯","塔吉克斯坦","越南"],"timezone":{"id":"Asia/Shanghai","time":"2021-04-19T13:53:56+08:00"},"flag":"🇨🇳","flagUrl":"https://static.webmasterapi.com/images/country-flags/svg/cn.svg","wiki":"https://en.wikipedia.org/wiki/China","user_agent":{"ua":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36","browser":{"name":"Chrome","version":"83.0.4103.116","major":"83"},"engine":{"name":"Blink","version":"83.0.4103.116"},"os":{"name":"Windows","version":"10"},"device":{},"language":"zh","locale":"zh-CN"}}}
    data,frame = JsonCompare().cmp(a, b)
    logger.info('data={0},frame={1}'.format(data,frame))
