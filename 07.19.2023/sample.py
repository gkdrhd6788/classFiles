# import my_math
# print(my_math.pi)
# print(my_math. add(1,2))

# from my_math import pi, add
# print(pi)
# print(add(1,5))

from my_package import my_math
print(my_math.pi)
print(my_math.add(1,5))


# from my_package.my_math import pi, add
# print(pi)
# print(add(1,5))

print(__name__)   #처음시작하는 module을 알려줌 