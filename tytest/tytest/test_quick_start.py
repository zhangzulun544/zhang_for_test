# def reverse(string):
#     return string[::-1]
#
# def test_reverse():
#     string = "good"
#     assert reverse(string) == "doog"
#
#     another_string = "itest"
#     assert reverse(another_string) == "tseti"
import pytest
from tytest.ty_setting import db


class Test_reverse(object):
    @pytest.fixture
    def dba(self):
        x = db.DB()
        return x
    def test_db(self,dba):
        results = dba.find(["*","test_case where id = 2"])
        li = []
        for i in results:
            for y in i:
                li.append(y)
        assert li[0] == 2