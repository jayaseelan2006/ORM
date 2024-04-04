from django.shortcuts import render,redirect 
from .models import subject
 
def home(request):
    subjects = subject.objects.all()
    return render(request,'home.html',{'subject':subjects})
