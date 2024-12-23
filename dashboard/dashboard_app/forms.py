from django import forms
from .models import State, City, Property

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state name'}),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state']  # Include 'state' for dropdown selection
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city name'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_id', 'property_name', 'description', 'city', 'address', 'contact_number', 'email', 'owner_name']
        '''widgets = {
            'property_id': forms.TextInput(),
            'property_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter property name','required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter owner name'}),
        }
'''