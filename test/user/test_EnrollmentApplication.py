# coding:utf-8
import unittest
import requests
import pytest
import allure
import time
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
from lib.get_token import getToken
from data import EnrollmentApplication_datas as LD
from config.config import *
sys.path.append('..')
from config.config import *
sys.path.append('../')



@allure.epic('托养中心')
class TestEnrollmentApplication(): 


	def test_GetDisabledInfoByIdNumber(self):
		token = getToken()
		path = "***"
		params = {"idNumber":"{}".format(LD.Enrollment_success_data['idNumber'])}
		headers = {"Authorization":"Bearer {}".format(token),"Content-Type":"application/json"}
		res = requests.get(url=url+path,params=params,headers=headers)
		result =json.dumps(res.json(),indent=False,ensure_ascii=False)
		log_case_info(LD.Enrollment_success_data['name'],path,params,res.status_code,result)
		assert res.status_code == 200
		result = res.json()
		assert result['result']['name'] == '王金莲'


if __name__ == "__main__":
 	pytest.main()
