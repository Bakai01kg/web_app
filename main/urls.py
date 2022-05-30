from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('about_us',views.about_us),
    path('layout',views.layout)
]
