import unittest
from Verfication_db import *
from QueryByContion_interface import QueryByContion

class QueryInformationTestCase(unittest.TestCase):

    # 分页查询有效状态的图文信息，验证返回结果正确性
    def test_queryInfo_case1(self):
        query = QueryByContion()
        response = query.request_queryinfo('G:/python/test/QueryByCondition_interface.yaml')
        self.assertEqual(response.status_code,200)   #验证请求响应码

        sql = "select * from information where delete_flag=0 and content_type=0"
        response_result = response.json()    #将返回结果转化成json，类型时dict
        db_rowcount = DB()

        self.assertEqual(response_result['total'],db_rowcount.check_rowcount(sql))   #返回结果总条数与数据库查询结果总条数进行对比





if __name__ == '__main__':
    unittest.main()
