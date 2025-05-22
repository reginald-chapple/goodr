from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from causes.models import Project

def home(request):
    template_name='pages/home.html'
    projects = Project.objects.all()[:4]
    context = {
        'projects': projects
    }
    return render(request, template_name, context)

@login_required
def browse(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pages/browse.html', context)

