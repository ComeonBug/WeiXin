import requests

from contact.token import WeiXin


class User:
    def create(self, dict=None, data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                             params={"access_token": WeiXin.get_token()},
                             json=dict,
                             data=data
                             ).json()

    def get_user_list(self, depart_id=1, **kwargs):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                            params={"access_token": WeiXin.get_token(),
                                    "department_id": depart_id}).json()
