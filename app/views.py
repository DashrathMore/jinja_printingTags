from django.shortcuts import render

# Create your views here.
def data(request):
    d={'name':'Dashrath', 'address':'MAHARASHTRA'}
    return render(request,'data.html',context=d)