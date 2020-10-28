import json
import logging
import random
import time

import pystache
import requests

from contact.token import WeiXin


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    depart_id = 2
    no = str(int(time.time()))

    @classmethod
    def setup_class(cls):
        # todo 创建测试用的部门
        print('set up class')

    def test_add_user(self):
        data = {
            "userid": "id_" + self.no,
            "name": "n_" + self.no,
            "mobile": "15822259938",
            "department": [self.depart_id]
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": WeiXin.get_token()},
                          json=data
                          ).json()
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_depart_menber(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": WeiXin.get_token(),
                                 "department_id": self.depart_id}).json()
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_create_user_by_template(self):
        param = {
            "userid": "no_" + self.no,
            "name": "t_" + self.no,
            "mobile": "86+ 1" + self.no,
            "email" : self.no +"@qq.com"
        }
        data = str(self.get_user_from_tmpl(param))
        data = data.encode("UTF-8")
        logging.debug(data)
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": WeiXin.get_token()},
                          data=data,
                          headers={'content_type': 'application/json; charset=UTF-8'},
                          ).json()
        assert r["errcode"] == 0

    def get_user_from_tmpl(self, dict):
        with open("user_create.json") as f:
            tmp = f.read()
        return pystache.render(tmp, dict)