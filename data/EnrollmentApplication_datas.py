# 正常场景测试数据
Enrollment_success_data = {'name': '正常测试-获取用户基本信息', 'idNumber': '33252719480305242341'}
GetEnrollment_success_data = {'name': '正常测试-获取入托申请列表','SkipCount': '1','MaxResultCount':10}
InfoList_success_data = {'name': '正常测试-获取所有残联中心待审核用户信息'}
GetAll_success_data = {'name': '正常测试-获取所有入托申请'}

# 异常场景测试 
Enrollment_param_error = [
	{'name': '异常测试-输入错误的参数获取用户基本信息', 'idNumber': '332527194803052','message':'没有查找到对应人员信息'},
	{'name': '异常测试-输入不存在的参数获取用户基本信息', 'idNumber': '3325271/*/565656','message':'没有查找到对应人员信息'},
	{'name': '异常测试-不输入参数获取用户基本信息', 'idNumber': '','message':'没有填写身份证号码'},
]

GetEnrollment_param_error = [
	{'name': '异常测试-输入错误的参数获取入托申请列表','SkipCount': '3','MaxResultCount':10},
	{'name': '异常测试-输入错误的参数获取入托申请列表','SkipCount': '1','MaxResultCount':50},
]

GetEnrollment_no_param = [
	{'name': '异常测试-输入错误的参数获取入托申请列表','SkipCount': '@','MaxResultCount':20},
	{'name': '异常测试-不输入参数获取入托申请列表','SkipCount': '','MaxResultCount':''},
]

