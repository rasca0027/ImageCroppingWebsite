from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Job

def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            worker = form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/dashboard/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard_view(request):
    user = request.user
    jobs = Job.objects.filter(user=user)
    counts = len(jobs)
    return render(request, 'dashboard.html', {'user': user, 'jobs_done': counts})
