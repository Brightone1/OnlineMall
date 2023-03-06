from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


def register(request):
    """Register a new user"""

    if request.method != 'POST':
        # No data submitted: Blank form
        form = RegistrationForm()
    else:
        # Data submitted: process data
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            login(request, new_user)
            return redirect('products:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
