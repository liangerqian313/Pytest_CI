
import json
import jsonpath
from logzero import logger


class Json:

    def json_format(self, _json):
        """
        格式化json
        :param _json: 要格式化json串
        :return:
        """
        return json.dumps(_json, sort_keys=True, indent=2, ensure_ascii=False)

    def get_json_value(self, _json, key):
        """
        根据key从json获取相关value
        :param _json:
        :param key:
        :return:
        """
        return jsonpath.jsonpath(_json, key)

    def get_json_value_by_key(self, _json, key):
        """
        获取单个key的值
        :param _json:数据源
        :param key:键
        :return:
        """
        res = jsonpath.jsonpath(_json, f'$..{key}')
        if res:
            if len(res) < 2:
                return res[0]
            if len(res) >= 2:
                return res

    def get_json_value_by_keys(self, _json, tag, key):
        """
        如果不同父键下面有同样名称的子键
        :param _json:数据源
        :param tag:父键
        :param key:子键对应值
        :return:
        """
        res = jsonpath.jsonpath(_json, f'$..{tag}..{key}')
        if res:
            if len(res) < 2:
                return res[0]
            if len(res) >= 2:
                return res


if __name__ == '__main__':
    js = Json()
    # data = {"error_code": 0, "stu_info": [
    #     {"id": 314, "name": "矿泉水", "sex": "男", "age": 18, "addr": "北京市昌平区", "grade": "摩羯座", "phone": "18317155663",
    #      "gold": 100, "cars": [{"car1": "bmw"}, {"car1": "ben-z"}], "cars1": [{"car1": "bmw"}, {"car1": "ben-z"}]}]}
    data = {"status":"1","count":"1","info":"OK","infocode":"10000","lives":[{"province":"北京","city":"东城区","adcode":"110101","weather":"晴","temperature":"26","winddirection":"西南","windpower":"4","humidity":"24","reporttime":"2021-04-19 14:34:13"}]}
    # logger.info('\n {}'.format(js.json_format(data)))
    # logger.info(js.get_json_value(data, '$..id'))
    # logger.info(js.get_json_value(data, '$.stu_info[0].cars'))
    # logger.info(js.get_json_value(data, '$.stu_info'))
    logger.info(js.get_json_value_by_key(data, 'info'))
    logger.info(js.get_json_value_by_key(data, 'info'))
    # logger.info(js.get_json_value_by_keys(data, 'cars', 'car1'))
