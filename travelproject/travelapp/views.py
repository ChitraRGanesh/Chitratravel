from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
    # name = "India"
    obj=Place.objects.all()
    return render(request,"index.html",{'result': obj})
    # return  render(request, "index.html")
    # return render(request, "home.html", {'obj': name})

# def calculation(request):
#     num1 = int(request.GET['num1'])
#     num2 = int(request.GET['num2'])
#     addresult = num1 + num2
#     subresult = num1 - num2
#     mulresult = num1 * num2
#     divresult = num1 / num2
#     return render(request, "results.html", {'add':addresult,
#                                             'sub':subresult,
#                                             'mul':mulresult,
#                                             'div':divresult})
