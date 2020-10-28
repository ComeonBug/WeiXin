import json
import logging
import random
import time

import pystache
import requests

from contact.token import WeiXin
from contact.user import User
from contact.utils import Utils


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    depart_id = 2
    no = str(int(time.time()))

    @classmethod
    def setup_class(cls):
        # todo 创建测试用的部门
        cls.user = User()
        print('set up class')

    def test_add_user(self):
        data = {
            "userid": "id_" + self.no,
            "name": "n_" + self.no,
            "mobile": "15822259939",
            "department": [self.depart_id]
        }
        r = self.user.create(data)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_depart_menber(self):
        depart_id = 2
        r = self.user.get_user_list(depart_id)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    def test_create_user_by_template(self):
        param = {
            "userid": "no_" + self.no,
            "name": "t_" + self.no,
            "mobile": "86+ 1" + self.no,
            "email" : self.no +"@qq.com"
        }
        data = str(Utils.get_info_from_tmpl("user_create.json",param))
        data = data.encode("UTF-8")
        logging.debug(data)
        r = self.user.create(data=data)
        assert r["errcode"] == 0