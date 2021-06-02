from django.shortcuts import render
from testApp.models import hydjobs

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hydjobsinfo(request):
    job_list=hydjobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testApp/hyd.html',context=my_dict)

def punejobsinfo(request):
    return render(request,'testApp/pune.html')

def bangjobsinfo(request):
    return render(request,'testApp/bang.html')

def indorejobsinfo(request):
    return render(request,'testApp/indore.html')
