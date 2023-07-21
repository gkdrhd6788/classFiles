'''
import requests

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data)
'''

import json

# 왜 세번을 쳐야 하지?
json_data = '''   
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "공부하기",
        "복습하기"
    ]

}
'''

data = json.loads(json_data)
print(data)
print(type(data)) #dict

#JSON 데이터에서 원하는 데이터만 가져오기
name = data.get('name')  #이게 맞나??dict에서 value가져오는 거
print(name)

