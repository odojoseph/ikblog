from django.shortcuts import render
from .models import serviceteam
from users.models import Evangelism, Post
# from django.http import HttpResponse

# Create your views here.
def home(request):
    # text = '<h1> Welcome to my WebPage!</h1>'
    # return HttpResponse(text)
    return render(request, 'myapp/home.html')

def contact(request):    
    return render(request, 'myapp/contact.html')

def about(request):    
    return render(request, 'myapp/about.html')
def history(request):    
    return render(request, 'myapp/history.html')
def service(request):    
    return render(request, 'myapp/service.html')
def ministry(request):    
    return render(request, 'myapp/ministry.html')
def evanmin(request):    
    return render(request, 'myapp/evanmin.html')
def testimony(request):    
    return render(request, 'myapp/testimony.html')

def activities(request):    
    return render(request, 'myapp/activities.html')

def gallery(request):    
    return render(request, 'myapp/gallery.html')

def news(request):    
    return render(request, 'myapp/news.html')

def donation(request):    
    return render(request, 'myapp/donation.html')

def member(request):    
    return render(request, 'myapp/member.html')

# def register(request):    
#     return render(request, 'myapp/register.html')

def login(request):    
    return render(request, 'myapp/login.html')

def logout(request):    
    return render(request, 'myapp/logout.html')

def leaders(request):
    serviceteam1 = serviceteam.objects.all()
    context = {'res':serviceteam1}
    return render(request, 'myapp/leaders.html', context)
def evanres(request):
    # if request.method=="GET":
        evange = Evangelism.objects.all()
        Context = { 'evi':evange }
        return render(request, 'users/evanres.html', Context)

def evanpresult(request):
    # if request.method=="GET":
        evanp = Post.objects.all()
        Context = { 'evp':evanp }
        return render(request, 'users/evanpresult.html', Context)



