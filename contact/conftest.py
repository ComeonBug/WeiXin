# 把fixture加进来
import pytest

from contact.token import WeiXin


@pytest.fixture(scope='session')
def token():
    return WeiXin.get_token_new()