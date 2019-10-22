# 添加护理类别
# 正常场景测试数据
AddNursing_normal_data = {'name': '正常测试-添加护理类别', 'labelColor': '#31CD24','typeName':'五级护理'}

# 异常场景测试 - labelColor
AddNursing_success_data = [
	{'name': '异常测试-输入错误的参数添加护理类别', 'labelColor': '#31C24','typeName':'六级护理'},
	{'name': '异常测试-不输入标签颜色添加护理类别', 'labelColor': '','typeName':'六级护理'},
]
# 异常场景测试
AddNursing_param_error_data = [
	{'name': '异常测试-输入不存在的参数添加护理类别', 'labelColor': '#311531C24','typeName':'/*/*'},
	{'name': '异常测试-输入不存在的参数添加护理类别', 'labelColor': '/*/*','typeName':'/*/*'},
]
# 异常场景测试 - typeName
Nursing_abnormal_data = [
	{'name': '异常测试-不输入参数添加护理类别', 'labelColor': '','typeName':''},
	{'name': '异常测试-只输入标签颜色添加护理类别', 'labelColor': '#31CD24','typeName':''},
]


# 修改护理类别
# 正常场景测试数据
UpdateNursing_normal_data = {'name':'正常测试-修改护理类别','labelColor':'#2157A3','typeName':'六级护理'}

# 异常场景测试 - labelColor
UpdateNursing_success_data = [
	{'name': '异常测试-输入错误的参数添加护理类别', 'labelColor': '#31C24','typeName':'六级护理'},
	{'name': '异常测试-不输入标签颜色添加护理类别', 'labelColor': '','typeName':'六级护理'},
]
# 异常场景测试
UpdateNursing_param_error_data = [
	{'name': '异常测试-输入不存在的参数添加护理类别', 'labelColor': '#311531C24','typeName':'/*/*'},
	{'name': '异常测试-输入不存在的参数添加护理类别', 'labelColor': '/*/*','typeName':'/*/*'},
]
# 异常场景测试 - typeName
UpdateNursing_abnormal_data = [
	{'name': '异常测试-不输入参数添加护理类别', 'labelColor': '','typeName':''},
	{'name': '异常测试-只输入标签颜色添加护理类别', 'labelColor': '#31CD24','typeName':''},
]


# 根据Id查询护理类别
# 正常场景测试数据
GetNursing_normal_data = {'name':'正常测试-根据Id查询护理类别'}

# 异常场景测试
GetNursing_param_error_data = [
	{'name': '异常测试-输入不存在的参数', 'Id': '#/*/*'},
	{'name': '异常测试-输入不存在的参数', 'Id': '123456786'},
	{'name': '异常测试-输入不存在的参数', 'Id': '123qwe'},
	{'name': '异常测试-输入不存在的参数', 'Id': ''},
]

#分页查询护理类别
# 正常场景测试数据
GetAllNursing_normal_data = [
	{'name':'正常测试-分页查询护理类别','MaxResultCount':'1'},
	{'name':'正常测试-分页查询护理类别','MaxResultCount':'10'},
	{'name':'正常测试-分页查询护理类别','MaxResultCount':'20'},
]

# 异常场景测试
GetAllNursing_param_error_data = [
	{'name': '异常测试-输入不存在的参数', 'MaxResultCount': '#/*/*'},
	{'name': '异常测试-输入不存在的参数', 'MaxResultCount': '123456*/*'},
	{'name': '异常测试-输入不存在的参数', 'MaxResultCount': '123qwe'},
	{'name': '异常测试-输入不存在的参数', 'MaxResultCount': ''},
]