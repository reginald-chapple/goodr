from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from causes.forms import ProjectForm, ObjectiveForm, AssignmentForm
from causes.models import Project, Objective, Assignment

@login_required
def my_projects(request):
    projects = Project.objects.filter(created_by=request.user)
    form = ProjectForm()
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'project_management/my_projects.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    return render(request, 'project_management/detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, 'Project created successfully.')
            return redirect('project-management:my_projects')
    messages.error(request, 'Project was not created successfully.')
    return redirect('project-management:my_projects')

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save
            messages.success(request, 'Project updated successfully.')
            return redirect('project-management:my_projects')
        else:
            form = ProjectForm(instance=project)

    return render(request, 'project_management/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('project-management:my_projects')
    return render(request, 'project_management/project_confirm_delete.html', {'project': project})

@login_required
def project_objectives(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    form = ObjectiveForm()
    context = {
        'project': project,
        'form': form
    }
    
    return render(request, 'project_management/objectives.html', context)

@login_required
def objective_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    if request.method == 'POST':
        form = ObjectiveForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.project = project
            obj.save()
        return redirect('project-management:objectives', project.id)
    else:
        return redirect('project-management:my_projects')
    
@login_required
def project_assignments(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    form = AssignmentForm()
    context = {
        'project': project,
        'form': form
    }
    
    return render(request, 'project_management/assignments.html', context)

@login_required
def assignment_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.created_by != request.user:
        return redirect('project-management:my_projects')
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.project = project
            assignment.save()
            return redirect('project-management:assignments', project.id)
    else:
        return redirect('project-management:my_projects')
