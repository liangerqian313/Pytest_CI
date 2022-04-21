# @Time : 2022/4/16 22:14
# @Author : Liang er qian
# @File : test_login.py

import pytest
import requests
from comon.yaml_util import YamlUtil
from comon.excel_util import ExcelUtil
import os
import allure
from comon.log_util import logger
from comon.HandlerCheck import JsonCompare
from comon.HandlerJson import Json
import json
from allure_commons.types import LabelType

# branch = "master"


class TestLogin:

    @pytest.mark.parametrize('case',ExcelUtil().read_excel('login'))
    def test_login01(self, case):
        allure.dynamic.label(LabelType.EPIC,case.get("app_name"))
        # allure.dynamic.feature(branch)
        allure.dynamic.title(case.get("case_title"))
        # allure.dynamic.story(case.get("case_title"))
        logger.info("详细参数为: {}".format(case['case_title']))
        allure.attach(body=case['url'], name='接口路径')
        allure.attach(body=case['case_data'], name='请求参数')
        allure.attach(body=case['res'], name='预期结果')
        logger.info("*************** 开始执行用例 ***************")
        logger.info('----------->开始执行测试案例:{}'.format(case['case_title']))
        response = requests.get(url=case['url'], data=eval(case['case_data']))
        # print(response,type(response))
        print(response.text,type(response))
        # act_res=response.json()
        allure.attach(body=str(response), name='响应状态')
        # #校验
        flag = False
        # 返回结果
        if not response:
            flag = True
            with allure.step("错误原因"):
                allure.attach("接口异常，没有获取到响应结果", "结果", allure.attachment_type.TEXT)
        else:
            _res = response.content.decode(encoding="utf-8")
            logger.info('返回结果:{}'.format(_res))
            logger.info('预期:{}'.format(case['res']))
            logger.info('实际:{}'.format(_res))
            with allure.step("预期与结果"):
                allure.attach(case['res'], "预期", allure.attachment_type.JSON)
                allure.attach(_res, "结果", allure.attachment_type.JSON)
                data, frame = JsonCompare().cmp(json.loads(case['res']), json.loads(_res))

            # 如果结果value不一致 or key 不一致时,打印出相关信息
            if data or frame:
                flag = True
                logger.error('测试案例【{}】实际结果与预期结果不一致'.format(case['case_id']))
                with allure.step("响应失败原因"):
                    for j in data:
                        logger.info('data={}'.format(j))
                        allure.attach(j, "数据", allure.attachment_type.TEXT)
                    for j in frame:
                        logger.info('frame={}'.format(j))
                        allure.attach(j, "结构", allure.attachment_type.TEXT)
        # #     # else:
        # #     #     #响应结果校验通过，检查是否有相关数据库校验
        # #     #     if case.get("Check"):
        # #     #         result = Verification().verify(case.get("Check"))
        # #     #         if result:
        # #     #             flag = True
        # #     #             logger.error('测试案例【{}】实际结果与预期结果不一致'.format(case['case_id']))
        # #     #             with allure.step("校验失败原因"):
        # #     #                 for j in result:
        # #     #                     logger.info('校验结果详情：{}'.format(j))
        # #     #                     allure.attach(j, "校验详情", allure.attachment_type.TEXT)
        #
        with allure.step("断言结果"):
            #assert flag == False  #该断言方式, 如果断言失败会导致后续代码不执行
            pytest.assume(flag == False)
        logger.info('----------->结束执行测试案例：【{}】'.format(case['case_title']))
        logger.info("*************** 结束执行用例 ***************")
