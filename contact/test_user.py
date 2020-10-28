import json
import logging
from contact.user import User
from contact.utils import Utils


class TestUser:
    logging.basicConfig(level=logging.DEBUG)
    depart_id = 2


    @classmethod
    def setup_class(cls):
        # todo 创建测试用的部门
        cls.user = User()
        print('set up class')

    def test_add_user(self):
        data = {
            "userid": "id_" + Utils.udid(),
            "name": "n_" + Utils.udid(),
            "mobile": "86+ 1" + Utils.udid(),
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
            "userid": "no_" + Utils.udid(),
            "name": "t_" + Utils.udid(),
            "mobile": "86+ 1" + Utils.udid(),
            "email" : Utils.udid() +"@qq.com"
        }
        data = str(Utils.get_info_from_tmpl("user_create.json",param))
        data = data.encode("UTF-8")
        logging.debug(data)
        r = self.user.create(data=data)
        assert r["errcode"] == 0