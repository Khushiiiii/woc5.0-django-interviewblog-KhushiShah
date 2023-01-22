from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("Home Page")

def home(request):
    return render(request, 'InterviewBlog/dashboard.html')

def login(request):
    return render(request, 'InterviewBlog/login.html')

def signup(request):
    return render(request,'InterviewBlog/signup.html')

def about(request):
    return render(request,'InterviewBlog/about.html')



# """
# hierarchy of storing information/html files/ webpages in django
# --interviewblog
# ---templates
# ----interviewblog
# -----dashboard.html
# -----index.html
# -----student.html
# """