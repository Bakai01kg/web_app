from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def about_us(request):
    return render(request,'main/about_us.html')

def layout(request):
    return render(request,'main/layout.html')

