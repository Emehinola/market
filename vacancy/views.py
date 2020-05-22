from django.shortcuts import render

# Create your views here.

# vacancy index views
def vacancy(request):
    context={
        "title" : "Vacancy"
    }
    return render(request, 'vacancy/vacancy.html', context)

def jobs(request):
    context={
        "title" : "Jobs list"
    }
    return render(request, 'vacancy/jobs.html', context)

def job(request):
    context={
        "title" : "Job application"
    }
    return render(request, 'vacancy/job.html', context)

def job_post(request):
    context={
        "title" : "Post a job offer"
    }
    return render(request, 'vacancy/job-post.html', context)