from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Job, Image
from django.utils import timezone
import random
from datetime import timedelta


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


@login_required
def job_view(request):
    # renew object list
    d = timedelta(minutes=30)
    timedout_objects = Image.objects.filter(block=True).filter(block_time__lt=timezone.now() - d)
    timedout_objects.update(block=False)
    # retrieve random obj from img that has not been done yet
    available_list = Image.objects.filter(count=0).filter(block=False)
    random_idx = random.randint(1, available_list.count())
    img = available_list[random_idx]
    # render the job page
    title = 'image-cropping-' + str(img.photo_id) 
    # block the process, record order time
    img.count += 1
    img.block = True
    img.block_time = timezone.now()
    img.save()
    # if not done, undo it, if done, create job object, add money 
    return render(request, 'job.html', {'title': title, 'img': img})


def thankyou_view(request):
    # save job object
    user = request.user
    done = True
    # TODO! 
    # unblock
    img.block = False
    # thank you
    return render(request, 'thankyou.html', {'obj': obj})
