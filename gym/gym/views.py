from django.shortcuts import render
from .forms import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
def Homepage(request):
    data={
        "name":"Vijay",
        "age":"23",
        "numbers":[1,2,3,4,5],
    }
    return render(request,'home.html',data)


def aboutpage(request):
    return render(request,'about.html')


def classespage(request):
    return render(request,'classes.html')


from django.shortcuts import render, redirect
from .forms import MembershipForm

def memebershippage(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = MembershipForm()

    context = {'member': form}
    return render(request, 'membership.html', context)



def tryuspage(request):

    return render(request,'tryus.html')

def productpage(request):

    context={
        'product_form':product_form()
        }
    if request.method =='POST':
        
        product=product_form(request.POST)
        if product.is_valid():
            product.save()
    return render (request,'products.html',context)


def successpage(request):
    # Fetch the most recent membership entry based on ID or creation date (if you have a created_at field)
    latest_membership = membership.objects.latest('id')  # Or 'created_at' if you have a timestamp field

    # Pass the data to the template
    context = {
        'latest_membership': latest_membership
    }

    return render(request, 'success.html', context)




def hello(request):
    return render(request,'hello.html')


#class productsView(APIView):
