from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from causes.forms import AssignmentForm
from causes.models import Assignment

@login_required
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if assignment.project.created_by != request.user:
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments:update', assignment.pk)
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignments/update.html', {'form': form, 'assignment': assignment})

@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if assignment.project.created_by != request.user:
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        assignment.delete()
        return redirect('project-management:assignments', assignment.project.pk)

    return redirect('assignments:update', assignment.pk)

