from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']

class ContactForm(forms.Form):
    form_email = forms.EmailField(required = True)
    subject = forms.CharField(required = True)
    message = forms.CharField(widget = forms.Textarea, required = True)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'photo_main_img']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_main_Img']
class GodwinForm(forms.ModelForm):
    class Meta:
        model = Godwin
        fields = ['name', 'tel', 'position', 'date', 'address']

class JoeForm(forms.ModelForm):
    class Meta:
        model = Joe
        fields = ['name', 'tel', 'position', 'date', 'address']

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['name', 'phone', 'ministry', 'date', 'address']
    
class Student1Form(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ['name', 'class1', 'date', 'address', 'tel']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item','qty','brand','prize','tel','date']

class EvangelismForm(forms.ModelForm):
    class Meta:
        model = Evangelism
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','nok_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','author','content','status']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
    
# Teaching Ministry Form for registration
class Min_TeachingForm(forms.ModelForm):
    class Meta:
        model = Min_Teaching
        fields = '__all__'
# Teaching Ministry Event Form
class Event_teachingForm(forms.ModelForm):
    class Meta:
        model = Event_teaching
        fields = ['title','anouncer','content','event_img']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Teaching Ministry Form
# Evangelical Ministry Form for registration
class Min_EvangelicalForm(forms.ModelForm):
    class Meta:
        model = Min_Evangelical
        fields = '__all__'
# Evangelical Ministry Event Form
class Event_evangelicalForm(forms.ModelForm):
    class Meta:
        model = Event_evangelical
        fields = '__all__'
        # queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Evangelical Ministry Form

# Intercessory Ministry Form for registration
class Min_IntercessoryForm(forms.ModelForm):
    class Meta:
        model = Min_Intercessory
        fields = '__all__'
# Intercessory Ministry Event Form
class Event_intercessoryForm(forms.ModelForm):
    class Meta:
        model = Event_intercessory
        fields = '__all__'
        # queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Intercessory Ministry Form
# Stewards Ministry Form for registration
class Min_StewardsForm(forms.ModelForm):
    class Meta:
        model = Min_Stewards
        fields = '__all__'
# Stewards Ministry Event Form
class Event_stewardsForm(forms.ModelForm):
    class Meta:
        model = Event_stewards
        fields = ['title','anouncer','content','event_img']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Stewards Ministry Form
# Visitation Ministry Form for registration
class Min_VisitationForm(forms.ModelForm):
    class Meta:
        model = Min_Visitation
        fields = '__all__'
# Visitation Ministry Event Form
class Event_visitationForm(forms.ModelForm):
    class Meta:
        model = Event_visitation
        fields = ['title','anouncer','content','event_img']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Visitation Ministry Form
# Praiseworship Ministry Form for registration
class Min_PraiseworshipForm(forms.ModelForm):
    class Meta:
        model = Min_Praiseworship
        fields = '__all__'
# Praiseworship Ministry Event Form
class Event_praiseworshipForm(forms.ModelForm):
    class Meta:
        model = Event_praiseworship
        fields = ['title','anouncer','content','event_img']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Praiseworship Ministry Form
# Leadership Form for registration
class Min_LeadershipForm(forms.ModelForm):
    class Meta:
        model = Min_Leadership
        fields = '__all__'
# Leadership Ministry Event Form
class Event_leadershipForm(forms.ModelForm):
    class Meta:
        model = Event_leadership
        fields = ['title','anouncer','content','event_img']
        queryset = Post.objects.filter(status=1).order_by('-created_on')
# End of Leadership Form
class Pgrp_Account1Form(forms.ModelForm):
    class Meta:
        model = Pgrp_Account1
        fields = '__all__'
        
# Leadership Ministry Event Form
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        queryset = News.objects.filter().order_by('-created_on')
# End of Leadership Form
class EventsgeneralForm(forms.ModelForm):
    class Meta:
        model = Eventsgeneral
        fields = '__all__'
        