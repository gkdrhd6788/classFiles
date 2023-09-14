from django.shortcuts import render

# Create your views here.
def cal(request,first_num,second_num):
    if second_num ==0:
        divided = "none"
    else:
        divided = first_num/second_num
    context = {
            "fir_num" : first_num,
            "sec_num" : second_num,
            "multiple": first_num*second_num,
            "minus":    first_num-second_num,
            "divided":  divided
    }
    return render(request,"calculators/calculator.html",context)