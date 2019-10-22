# coding:utf-8
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
from data import NursingType_datas as LD
from config.config import *
sys.path.append('..')
from config.config import *
sys.path.append('../')
#from basecase import  BaseCase



@allure.epic('托养中心')
class TestNursingType(): 

	def test_AddNursing_normal(self):
		token = getToken()
		path = "***"
		params = {"labelColor":"{}".format(LD.AddNursing_normal_data['labelColor']),"typeName":"{}".format(LD.AddNursing_normal_data['typeName'])}
		headers = {"Authorization":"Bearer {}".format(token),"Content-Type":"application/json"}
		res = requests.post(url=url+path,json=params,headers=headers)
		result =json.dumps(res.json(),indent=False,ensure_ascii=False)
		log_case_info(LD.AddNursing_normal_data['name'],path,params,res.status_code,result)
		assert(res.status_code,200)
		result = res.json()
		assert(result['result']['typeName'],'五级护理')
		Id = result['result']['id']
		Ntype=TestNursingType()
		Ntype.Delete(Id)



if __name__ == "__main__":
 	pytest.main()
