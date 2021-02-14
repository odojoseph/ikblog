from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from myapp.views import evanres
# from .forms import ContactForm, PhotoForm,GodwinForm, TrainForm,EvangelismForm
from . models import Train, Student1, Evangelism, Post
# TrainForm
import reportlab
from reportlab.pdfgen import canvas
# from django.views import generic


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for{username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def savteam(request):
    if request.method=="POST":
        form=serviceteam2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-home')
    else:
        form=serviceteam2()
    return render(request, 'users/savteam.html', {'form': form})



def sirwin(request):
    if request.method=="POST":
        form=GodwinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-home')
    else:
        form=GodwinForm()
    return render(request, 'users/sirwin.html', {'form': form})

def vistech(request):
    if request.method=="POST":
        form=JoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-home')
    else:
        form=JoeForm()
    return render(request, 'users/vistech.html', {'form': form})

def train(request):
    if request.method=="POST":
        form=TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-home')
    else:
        form=TrainForm()
        return render(request, 'users/train.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form()
            messages.success(request, f'your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm (instance = request.user)
        p_form = ProfileUpdateForm (instance = request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)

def email(request):
    # subject = 'Thank you for registering to our site'
    # message = 'You are welcome to our fellowship site, we expected you to come and join us in our journey to the Kingdom of God.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['visionsynergy.ict@gmail.com','sirwin2win@gmail.com']
    # send_mail(subject, message, email_from, recipient_list)
    # return redirect('myapp-home')
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form .is_valid():
            subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['form_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, form_email,['visionsynergy.ict@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return redirect('successView')
    return render(request, "users/email.html", {'form':form})

def successView(request):
    return HttpResponse('success! Thank you for your message')

def pics(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['content.Disposition']= 'attachment',
    filename = 'somefilename.pdf'
    p = canvas.Canvas(response)
    p.drawString(100,100,'Hellow World')
    p.showPage()
    p.save
    return response

def img(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo')
    else:
        form = HotelForm()
    return render(request, 'users/img.html', {'form':form})

def photo(request):
    if request.method == 'GET':
        # response = get_response(request)
        Hotels = Hotel.objects.all()
        return render(request,'users/photo.html',{'hotel_images':Hotels})

def pay(request):
    return render(request,'users/pay.html')

def see(request):
    yes = Train.objects.all()
    context = {'res':yes}
    return render(request, 'users/see.html', context)

def student1(request):
    if request.method == "POST":
        form = Student1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-home')
    else:
        form = Student1Form()
        return render(request, 'users/student1.html', {'form':form})
# displaying of the Student1 db result
def stdent(request):
    sch = Student1.objects.all()
    context = {'result': sch}
    return render(request, 'users/stdent.html', context)

def prdt(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print ('Saving datas..')
            form.save()   
            messages.success(request, 'Form submission successful')   
            return redirect('myapp-prdt')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('myapp-prdt')
    else:
        form = ProductForm()        
        return render(request, 'users/prdt.html', {'form':form})

evange = Evangelism.objects.all()
Context = { 'evi':evange }

def evanmin(request):
    evange = Evangelism.objects.all()
    Context = { 'evi':evange }
    evanp = Post.objects.all()
    Context = { 'evp':evanp }
    # return render(request,'myapp/evanmin.html', Context)    
    if request.method=="POST":
        form = EvangelismForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('myapp-home')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('myapp-home')
    else:
        form = EvangelismForm()
        return render(request,'myapp/evanmin.html',{'form':form, 'evi':evange, 'evp':evanp } )
# Evangelical Ministry Members List
                       
# def evanmin(request):
#     evange = Evangelism.objects.all()
#     Context = { 'evi':evange }
#     return render(request,'myapp/evanmin.html', Context)
def evanpost(request): 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post submission successful')   
            return redirect('myapp-home')
    else:
        form = PostForm()
        return render(request,'myapp/evanpost.html', {'form':form} )

# Steward Ministry Form, Record, Events
def stwdmin(request):
    stwdevent = Eventstwd.objects.all()
    return render( request,'myapp/stwdmin.html', {'stwd':stwdevent, 'evi':evange,} )
    
# Teaching ministry view form
def min_teach(request):
    if request.method == "POST":
        form = Min_TeachingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_teach')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_teach')
    else:
        form = Min_TeachingForm()
        teach = Min_Teaching.objects.all()
        Context = {'tm':teach }
        tevent = Event_teaching.objects.all()
        pro = {'evt':tevent }
        return render(request,'myapp/min_teach.html', { 'form':form, 'evt':tevent, 'tm':teach })
# Teaching Ministry view Event
def eventeach(request):
    if request.method == 'POST':
        form = Event_teachingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventeach')
    else:
        form = Event_teachingForm()
    return render(request, 'users/eventeach.html', { 'form':form })
    # End of teaching view
# Evangelical ministry view form
def min_evang(request):
    if request.method == "POST":
        form = Min_EvangelicalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_evang')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_evang')
    else:
        form = Min_EvangelicalForm()
        evang = Min_Evangelical.objects.all()
        Context = {'eva':evang }
        vent = Event_evangelical.objects.all()
        lica = {'ng':vent }
        return render(request,'myapp/min_evang.html', { 'form':form, 'ng':vent, 'eva':evang })
# Evangelical Ministry view Event
def eventgelic(request):
    if request.method == 'POST':
        form = Event_evangelicalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful') 
            return redirect('eventgelic')
    else:
        form = Event_evangelicalForm()            
    return render(request, 'users/eventgelic.html', { 'form':form })
    # end of Evangelical Ministry view form
# Intercessory ministry view form
def min_pray(request):
    if request.method == "POST":
        form = Min_IntercessoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_pray')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_pray')
    else:
        form = Min_IntercessoryForm()
        pray = Min_Intercessory.objects.all()
        Context = {'pr':pray }
        prevent = Event_intercessory.objects.all()
        yain = {'ay':prevent }
        return render(request,'myapp/min_pray.html', { 'form':form, 'ay':prevent, 'pr':pray })
# Intercessory Ministry view Event
def eventpray(request):
    if request.method == 'POST':
        form = Event_intercessoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventpray')
    else:
        form = Event_intercessoryForm()
    return render(request, 'users/eventpray.html', { 'form':form })
    # end of Intercessory Ministry view form
# Stewards ministry view form
def min_stewards(request):
    if request.method == "POST":
        form = Min_StewardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_stewards')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_stewards')
    else:
        form = Min_StewardsForm()
        stewards = Min_Stewards.objects.all()
        Context = {'war':stewards }
        stevent = Event_stewards.objects.all()
        wards = {'ds':stevent }
        return render(request,'myapp/min_stewards.html', { 'form':form, 'ds':stevent, 'war':stewards })
# Stewards Ministry view Event
def eventsteward(request):
    if request.method == 'POST':
        form = Event_stewardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventsteward')
    else:
        form = Event_stewardsForm()
    return render(request, 'users/eventsteward.html', { 'form':form })
    # end of Stewards Ministry view form
# Visitation ministry view form
def min_visit(request):
    if request.method == "POST":
        form = Min_VisitationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_visit')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_visit')
    else:
        form = Min_VisitationForm()
        visit = Min_Visitation.objects.all()
        Context = {'vis':visit }
        visevent = Event_visitation.objects.all()
        sit = {'it':visevent }
        return render(request,'myapp/min_visit.html', { 'form':form, 'it':visevent, 'vis':visit })
# Visitation Ministry view Event
def eventvisit(request):
    if request.method == 'POST':
        form = Event_visitationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventvisit')
    else:
        form = Event_visitationForm()
    return render(request, 'users/eventvisit.html', { 'form':form })
    # end of Visitation Ministry view form
# Praiseworship ministry view form
def min_praiz(request):
    if request.method == "POST":
        form = Min_PraiseworshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_praiz')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_praiz')
    else:
        form = Min_PraiseworshipForm()
        praiz = Min_Praiseworship.objects.all()
        Context = {'prai':praiz }
        przevent = Event_praiseworship.objects.all()
        aiz = {'iz':przevent }
        return render(request,'myapp/min_praiz.html', { 'form':form, 'iz':przevent, 'prai':praiz })
# Praiseworship Ministry view Event
def eventpraiz(request):
    if request.method == 'POST':
        form = Event_praiseworshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventpraiz')
    else:
        form = Event_praiseworshipForm()
    return render(request, 'users/eventpraiz.html', { 'form':form })
    # end of Praiseworship Ministry view form
# Leadership  view form
def min_lead(request):
    if request.method == "POST":
        form = Min_LeadershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')   
            return redirect('min_lead')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('min_lead')
    else:
        form = Min_LeadershipForm()
        lead = Min_Leadership.objects.all()
        Context = {'le':lead }
        leadevent = Event_leadership.objects.all()
        led = {'ad':leadevent }
        return render(request,'myapp/min_lead.html', { 'form':form, 'ad':leadevent, 'le':lead })
def eventlead(request):
    if request.method == 'POST':
        form = Event_leadershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventlead')
    else:
        form = Event_leadershipForm()
    return render(request, 'users/eventlead.html', { 'form':form })
    # end of Visitation Ministry view form

#View the displays on the leaders Page foer general leadership
def service(request):
    lead = Min_Leadership.objects.all()
    Context = {'let':lead }
    # leadevent = Event_leadership.objects.all()
    # led = {'ad':leadevent }
    return render(request,'myapp/service.html', Context)
   
# Praiseworship Ministry view Event



def account(request):
    if request.method == "POST":
        form = Pgrp_Account1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted')   
            return redirect('account')
        else:
            messages.success(request, 'Form submission not successful')
            return redirect('account')
    else:
        form = Pgrp_Account1Form()
        acct = Pgrp_Account1.objects.all()
        acct.order_by = 'date'
        Context = {'act':acct }
        cred = Pgrp_Account1.objects.aggregate(Sum('credit'))       
        # cred=Pgrp_Account.objects.filter(credit__isnull=True).aggregate(Sum('credit'))
        credt = {'cred':cred }
        # cred = float(credt['cred'])
        deb = Pgrp_Account1.objects.aggregate(Sum('debit'))
        debt = {'deb':deb }
        # bala = cred - deb
        # bal = {'blc':balance }       
        return render(request,'myapp/account.html', {'form':form, 'act':acct,'cred':cred,'deb':deb } )
        # , 'crdt':cred,'dbt':deb, 'blc':balance

# News view form
def news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()
        nwz = News.objects.all()
        Context = {'nez':nwz }
    return render(request, 'myapp/news.html', { 'form':form,'nez':nwz })
    # end of News view form

# General Event view form
def secretary(request):
    if request.method == 'POST':
        form = EventsgeneralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = EventsgeneralForm()
        evg = Eventsgeneral.objects.all()
        Context = {'gevt':evg }
    return render(request, 'myapp/secretary.html', { 'form':form, 'gevt':evg })
    # end of General Event view form