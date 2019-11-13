from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projects
from .forms import OrderForm,BakeryForm

def home(request):
    
    images=Projects.objects.all()
    return render(request,'index.html',{"images":images})
