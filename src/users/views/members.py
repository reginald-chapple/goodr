from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from users.decorators import members_required
from users.forms import UserPhotoForm

@login_required
@members_required
def upload_photo(request):

    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            print(form.cleaned_data['photo'])
            user.photo = form.cleaned_data['photo']
            user.save()
            return redirect('home')
    else:
        form = UserPhotoForm()
    context = { 'form': form }
    return render(request, 'members/upload_photo.html', context)
