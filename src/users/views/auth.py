from django.contrib.auth import logout
from django.shortcuts import redirect, render

from users.forms import CreateUserForm

def user_registration(request):
    template_name = 'registration/signup.html'
    context = {}
    
    form = CreateUserForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect("home")
    
    context["form"] = form
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')
