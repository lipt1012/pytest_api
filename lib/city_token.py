import requests
import json
import sys
sys.path.append('..')
from config.config import *
def get_cityToken():
	res = requests.post(
		url = url +"***",
		json = {"username": "***","password": "***"},
		headers = {"Content-Type":"application/json"},timeout = 5)
	return res.json()['result']['token']





