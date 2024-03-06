from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from track.models import *
from track.forms import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

data=[{"name":"John","age":24},{"name":"Smith","age":45},{"name":"zerro","age":66}]
def index(request):
    return HttpResponse("hello world")
def mahmoud(request,id):
    return render(request,'main.html')
def parent(request):
    return render(request,'parent.html')
def strin(request):
    context={'data':data}
    return render(request,'list.html',context)

def producrshow(request,id):
    prod=productd.objects.get(id=id)
    context={'prod':prod}
    return render(request,'show.html',context)

@login_required()
@require_http_methods(['GET','POST'])
def productall(request):

    # context={'data':productd.objects.all()}
    context={'data':productd.get_products()}

    return render(request,'product.html',context)

def productAddusingForm(request):
    form=AddproductusingForm()
    context={'form':form}
    if(request.method=='POST'):
        form=AddproductusingForm(request.POST)
        if form.is_valid():
            productd.objects.create(name=request.POST['name'],price=request.POST['price'])
            return render(request, 'insertUsingForm.html', context)

    return render(request,'insertUsingForm.html',context)

class ProductList(ListView):
    model = productd

class ProductDetails(DetailView):
    model = productd

class ProductCreate(CreateView):
    model = productd
    fields = ['name', 'price']
    template_name = 'insert.htmll'
    success_url = '/'


class ProductUpdate(UpdateView):
    model = productd
    fields = ['name', 'price']
    template_name = 'update.html'
    success_url = '/'


class ProductDelete(DeleteView):
    model = productd
    success_url = '/'
def productAdd(request):
    if request.method=='POST':
        if (request.POST['tname']!=''):

            pname=request.POST['tname']
            pprice=request.POST['tnumber']

            productd.objects.create(name=pname,price=pprice)

            return HttpResponseRedirect(reverse('product'))
        else:
            context={'message':'The name you entered is invalid.'}
            return render(request, 'insert.html', context)

    return render(request,'insert.html')

def productupdate(request,id):
    context={}
    if request.method=='POST':
        productd.objects.filter(id=id).update(
            name=request.POST['tname'],
            price=request.POST['tnumber']
        )
        return HttpResponseRedirect(reverse('product'))


    product=productd.objects.get(id=id)
    context['product']=product
    return render(request,'update.html',context)
def productdel(request,id):
    productd.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('product'))