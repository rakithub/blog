from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Create a blank form.
        form = UserCreationForm()
    else:
        # Process POST data.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:home')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
