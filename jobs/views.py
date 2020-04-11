from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .models import Job

def home(request):
    jobs = Job.objects #gets all jobs objects
    return render(request, 'jobs/home.html', {'jobs':jobs})#grabs everything from JOBS db!!!

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
