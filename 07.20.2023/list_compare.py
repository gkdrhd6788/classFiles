numbers=['1','2','3']

#1. for loop
new_numbers=[]

for num in numbers:
    new_numbers.append(int(num))

print(new_numbers)



#2. map
new_numbers_2 = list(map(int,numbers))
print(new_numbers_2)




#3. List Comprehension

new_numbers_3 = [int(number) for number in numbers]  
print(new_numbers_3)                    