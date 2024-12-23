from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *



@login_required
def indexpage(request):
    users = User.objects.all()
    return render(request, 'index.html', {'user': request.user, 'users': users})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def registerpage(request):
    return render(request, 'register.html')  # Render the registration form


def passwordpage(request):
    return render(request, 'password.html')  # Render the password reset form



def fo1page(request):
    return render(request, '401.html')  # Render a custom 401 page


def fofpage(request):
    return render(request, '404.html')  # Render a custom 404 page


def foopage(request):
    return render(request, '500.html')  # Render a custom 500 page

def propertypage(request):
    return render(request,'property.html')




def propertypage(request):
    if request.method == "POST":
        property_form = PropertyForm(request.POST)
        if property_form.is_valid():
            property_form.save()
            messages.success(request, "Property added successfully!")  # Optional success message
            return redirect('property_form')  # Redirect to the allproperty view after successful submission
    else:
        property_form = PropertyForm()

    context = {
        'property_form': property_form  # Make sure to pass the form back in case of validation errors
    }

    return render(request, 'property.html', context)

# View to display all properties
def allproperty(request):
    context = {
        'all_property': Property.objects.all()  # Retrieve all properties from the database
    }
    return render(request, 'property_form.html', context)