from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from causes.forms import ObjectiveForm
from causes.models import Objective

@login_required
def objective_update(request, pk):
    objective = get_object_or_404(Objective, pk=pk)

    if objective.project.created_by != request.user:
        logout(request)
        return redirect('login')

    if request.method == "POST":
        form = ObjectiveForm(request.POST, instance=objective)

        if form.is_valid():
            form.save()
            return redirect("objectives:update", objective.pk)
    else:
        form = ObjectiveForm(instance=objective)

    context = {
        "form": form,
        "objective": objective
    }
    return render(request, "objectives/update.html", context)

@login_required
def objective_delete(request, pk):
    objective = get_object_or_404(Objective, pk=pk)

    if objective.project.created_by != request.user:
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        objective.delete()
        return redirect('project-management:objectives', objective.project.pk)

    return redirect('objectives:update', objective.pk)
