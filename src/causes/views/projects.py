from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from causes.forms import ProjectForm
from causes.models import Cause, Project

def project_list(request):
    projects = Project.objects.filter(status="In Progress")

    search_query = request.GET.get('search', '')
    selected_cause = request.GET.get('cause', '')

    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(intended_impact__icontains=search_query) |
            Q(beneficaries__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    if selected_cause:
        projects = projects.filter(cause__name=selected_cause)

    paginator = Paginator(projects, 10)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    causes = Cause.objects.all()

    context = {
        'page_obj': page_obj,
        'causes': causes
    }
    return render(request, 'projects/project_list.html', context)
