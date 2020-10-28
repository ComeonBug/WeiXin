import requests
import logging
import json


class TestDepartment:
    logging.basicConfig(level=logging.DEBUG)

    def test_create(self, token):
        data = {
            "name": "上海研发中心9",
            "name_en": "SHDD",
            "parentid": 1,
            "order": 1,
            "id": 11
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data).json()
        logging.debug(json.dumps(r, indent=2))

    def test_create_nlevel(self,token):
        parentid = 1
        for i in range(1, 6):
            data = {
                "name": "上海研发中心8" + str(i),
                "parentid": parentid
            }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": token},
                              json=data).json()
            logging.debug(json.dumps(r, indent=2))
            parentid = r['id']

    def test_getDepartment(self,token):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": token}).json()
        logging.debug(json.dumps(r, indent=2))
