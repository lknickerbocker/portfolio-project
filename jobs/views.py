from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects #gets all jobs objects
    return render(request, 'jobs/home.html', {'jobs':jobs})#grabs everything from JOBS db!!!