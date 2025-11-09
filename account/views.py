from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def create_account(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(
        request,
        'registration/register.html',
        {'user_form': user_form}
    )
