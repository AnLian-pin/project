import json

data=[{"name":"王大雷","age":19},{"name":"赵一笛","age":17},{"name":"荆红雪","age":21}]
json_str=json.dumps(data,ensure_ascii=False)
print(json_str)
print(type(json_str))
print(json_str)

data2={"name":"汪曾棋","age":19}
json_str2=json.dumps(data2,ensure_ascii=False)
print(type(json_str2))
print(json_str2)

mystr=json.loads(json_str)
print(type(mystr))
print(mystr)

mystr2=json.loads(json_str2)
print(type(mystr2))
print(mystr2)