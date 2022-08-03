
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def wayanad(request):
    return render(request,'wayanad.html')

def thrissur(request):
    return render(request,'thrissur.html')

def alappuzha(request):
    return render(request,'alappuzha.html')

def idukki(request):
    return render(request,'idukki.html')

def add(request):
    return render(request,'add.html')

def result(request):
    return render(request,'result.html')

def add_num(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    sum=n1+n2
    return render(request,'result.html',{'result':sum})

def calc_page(request):
    return render(request,'calc_page.html') 

def kozhikode(request):
    return render(request,'kozhikode.html')
    
def calc(request):
    c=''

    if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opr=request.POST.get('opr')
 
        if opr=="+":
            c=n1+n2
        elif opr=="-":
            c=n1-n2
        elif opr=="*":
            c=n1*n2
        elif opr=="/":
            c=n1/n2
    
    print(c)
    return render(request,"calc_page.html",{'result':c})