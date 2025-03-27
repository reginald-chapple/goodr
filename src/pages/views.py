from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from causes.models import Project

@login_required
def home(request):
    template_name='pages/home.html'
    return render(request, template_name)

@login_required
def browse(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pages/browse.html', context)

