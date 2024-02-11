from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

# returing string as responce of function based view

def fbv_string(request):
    return HttpResponse('<h1>this is function based view </h1>')


# returing string as class based view


class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1> this is class based view ')
    


# rendaring html form by function based view
    

def fbvhtml(request):
    return render(request,'fbvhtml.html')


# rendaring html form by class based view


class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    




#insert data by fbv models
    
def fbv_template(request):
    SFO=schoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=schoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('inserted data')
    return render(request,'fbv_template.html',d)



#insert data by cbv models
class cfvtemplates(View):
    def get(self,request):
        ESFO=schoolForm()
        d={'ESFO':ESFO}
        return render(request,'cfvtemplates.html',d)
    
    def post(self,request):
        SFDO=schoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('<h1> insertion is done')