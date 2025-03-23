from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def home(request):
    template_name='pages/home.html'
    return render(request, template_name)

