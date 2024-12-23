from django.urls import path


from .views import *

urlpatterns=[
    path('', Homepage),
    path('about/',aboutpage),
    path('classes/', classespage),
    path('membership/', memebershippage),
    path('tryus/', tryuspage),
    path('products/',productpage),
    path('success/', successpage, name='success'),
    path('hello/',hello)
]
