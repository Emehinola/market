from django.shortcuts import render

# Create your views here.

# home views
def home(request):
    return render(request, 'index/index.html')

# market views
def market(request):
    return render(request, 'index/blog.html')