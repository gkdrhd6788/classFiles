from django.shortcuts import render

# Create your views here.
def cal(request,food,num):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if food in product_price.keys():
        total_price = product_price.get(food)*num
    else:
        total_price = 0
    
    context = {
        'food': food,
        'num': num,
        'total_price' : total_price,
    }
    return render(request,'prices/price.html',context)

