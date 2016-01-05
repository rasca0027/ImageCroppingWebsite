from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Job, Image, Crop
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
            worker = form.save(commit=False)
            worker.set_password(form.cleaned_data["password"])
            worker.save()
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
    resp = render(request, 'job.html', {'title': title, 'img': img})
    resp.set_cookie('start_time', timezone.now())
    return resp

def thankyou_view(request):
    if request.method == "POST":
        x1 = request.POST['x1']
        y1 = request.POST['y1']
        height = request.POST['height']
        width = request.POST['width']
        # save job object
        user = request.user
        photo_id = request.POST['photo_id']
        start_time = request.COOKIES.get('start_time')
        end_time = timezone.now()
        image = Image.objects.get(photo_id=photo_id)
        title = "Crop Job-" + str(photo_id)
        pay = 3 # TODO!
        job = Job(title=title, done=True, user=user, pay=pay,
                start_time=start_time, end_time=end_time)
        job.save()
        job.image.add(image)
        photo_url = Image.objects.get(photo_id=photo_id).url
        print photo_url
        rx1, ry1, rw, rh = recover_size(x1, y1, width, height, photo_url)
        crops = Crop(img=image, worker=user, need_crop=True,
                x1=rx1, y1=ry1, width=rw, height=rh)
        crops.save()
        # add money
        user.money += pay
        user.save()
        # unblock
        image.block = False
        image.save()
        return HttpResponse('success')
    else:
        return render(request, 'thankyou.html', {})

def no_crop(request, photo_id):
    # save job object
    user = request.user
    image = Image.objects.get(photo_id=photo_id)
    start_time = request.COOKIES.get('start_time')
    print start_time
    end_time = timezone.now()
    title = "Crop Job-" + str(photo_id)
    pay = 1 # TODO!
    job = Job(title=title, done=True, user=user, pay=pay,
            start_time=start_time, end_time=end_time)
    job.save()
    job.image.add(image)
    crops = Crop(img=image, worker=user, need_crop=False) 
    crops.save()
    # add money
    user.money += pay
    user.save()
    # unblock
    image.block = False
    image.save()
    return render(request, 'thankyou.html', {'pay': pay})


def recover_size(x1, y1, w, h, url):
    from .get_size import get_image_size
    rwidth, rheight = get_image_size(url)
    print 'types:',type(rwidth), type(rheight)
    if rwidth <= 800 and rheight <= 800:
        return int(x1), int(y1), int(w), int(h)
    elif rwidth > 800:
        scale = rwidth / (800 + 0.0)
        rx1 = int(x1) * scale
        ry1 = int(y1) * scale
        rh = int(h) * scale
        rw = int(w) * scale
        return rx1, ry1, rw, rh 
    elif rheight > 800:
        scale = rheight / (800 + 0.0)
        print 'x1', x1, type(x1)
        rx1 = int(x1) * scale
        ry1 = int(y1) * scale
        rh = int(h) * scale
        rw = int(w) * scale
        return rx1, ry1, rw, rh 

