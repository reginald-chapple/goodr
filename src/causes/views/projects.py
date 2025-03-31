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

@login_required
def my_projects(request):
    projects = Project.objects.filter(created_by=request.user)
    form = ProjectForm()
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'projects/my_projects.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, 'Project created successfully.')
            return redirect('projects:my_projects')
    messages.error(request, 'Project was not created successfully.')
    return redirect('projects:my_projects')

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save
            messages.success(request, 'Project updated successfully.')
            return redirect('projects:my_projects')
        else:
            form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('projects:my_projects')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})