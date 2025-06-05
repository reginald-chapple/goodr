from django.contrib.auth import logout
from django.shortcuts import redirect, render

from users.forms import CreateUserForm

def user_registration(request):
    template_name = 'registration/signup.html'
    context = {}

    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    context['form'] = form
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')
