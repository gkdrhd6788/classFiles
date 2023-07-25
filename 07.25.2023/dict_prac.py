blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']


# #[]
# new_dict ={}
# for blood_type in blood_types:
#     #기존에 키가 존재한다면,
#     if blood_type in new_dict:
#         new_dict[blood_type] +=1
#     # 키가 존재하지 않는다면
#     else:
#         new_dict[blood_type] =1

# print(new_dict)


# #get
# new_dict ={}
# for blood_type in blood_types:
#     new_dict[blood_type] = new_dict.get(blood_type, 0 ) + 1   #1이 아닌 이유
# #강의 다시

# print(new_dict)


#.setdefault()
new_dict ={}
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.setdefault(blood_type, 0) + 1
    # new_dict.setdefault(blood_type,0)
    # new_dict[blood_type] += 1   #1이 아닌 이유 

print(new_dict)

