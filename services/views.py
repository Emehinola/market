from django.shortcuts import render

# Create your views here.

# accommodation views 
def accommodation(request):
    return render(request, 'services/index.html')

def professionals(request):
    context={
        'title':'professionals'
    }
    return render(request, 'services/professionals.html', context)

def hire(request):
    context={
        'title':'hire'
    }
    return render(request, 'services/hire.html', context)

def resume(request):
    context={
        'title':'update your resume'
    }
    return render(request, 'services/resume.html', context)