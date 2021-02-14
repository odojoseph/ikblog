from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from phone_field.models import PhoneField
from djmoney.models.fields import MoneyField
from django.db.models import Sum
from decimal import Decimal


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    def __str__(self):
        return f'{self.user.username} profile'


class Photo(models.Model):
    name = models.CharField(max_length = 50)
    photo_main_img = models.ImageField(upload_to = 'images/')


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_main_Img = models.ImageField(upload_to='images/')


class serviceteam2(models.Model):
    name = models.CharField(max_length=255)
    tel =models.IntegerField()
    position = models.CharField(max_length=255)
    date = models.DateTimeField()
    address = models.CharField(max_length=255)


class Godwin(models.Model):
    name = models.CharField(max_length=255)
    tel =models.IntegerField()
    position = models.CharField(max_length=255)
    date = models.DateTimeField()
    address = models.CharField(max_length=255)

class Joe(models.Model):
    name = models.CharField(max_length=255)
    tel =models.IntegerField()
    position = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(max_length=255)

class Train(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    ministry = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(max_length=255)    
    class Meta:
        db_table='train'
class TrainAdmin(admin.ModelAdmin):
        list_display = ('name', 'phone', 'ministry', 'date', 'address')
        def __str__(self):
            return self.name

class Student1(models.Model):
    name = models.CharField(max_length=255)
    class1 = models.CharField(max_length=55)
    date = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=25)
    class Meta:
        db_table = 'student1'
class Student1Admin(admin.ModelAdmin):
    list_display = ('name', 'class1', 'date', 'address', 'tel')
    def __str__(self):
        return self.name

class Product(models.Model):
    item = models.CharField(max_length=200)
    qty = models.IntegerField()
    brand = models.CharField(max_length=255, unique=True)
    prize = MoneyField(max_digits=11, decimal_places=2, default_currency='USD')
    tel = PhoneField()
    date = models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        db_table='product'
        def __str__(self):
            return str(self.item)+":$"+str(self.price)

class ProductAdmin(admin.ModelAdmin):
    list_display=('item','qty','brand','prize','tel','date')
    def __str__(self):
        return str(self.item)+":$"+str(self.price)
# Evangelical ministry Table

class Evangelism(models.Model):     
    OPTIONS = (
        ('male' , 'Male'),
    ('female','Female'),            
           )
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField()
    phone_number = PhoneField()
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField()
    next_of_kin = models.CharField(max_length=255)
    nok_phone = PhoneField()
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=CHOICES, default='teach')
    date_joined = models.DateField()
    class Meta:
        db_table='evangelism'
class EvangelismAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','nok_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined')
    def __str__(self):
        return self.fname

# Evangelical blog
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')    
    def __str__(self):
        return self.title
# Steward Ministry
class Eventstwd(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_main_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_steward'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
class EventstwdAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'anouncer','content','event_main_img','created_on')    
    def __str__(self):
        return self.title

# Teaching Ministry Database
class Min_Teaching(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_teaching'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_TeachingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_teaching(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_teaching'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_teachingAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of teaching ministry page
# Evangelical Ministry Database
class Min_Evangelical(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_evangelical'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_EvangelicalAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_evangelical(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_evangelical'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_evangelicalAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Evangelical ministry page
# Intercessory Ministry Database
class Min_Intercessory(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_intercessory'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_IntercessoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_intercessory(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_intercessory'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_intercessoryAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Intercessory ministry page
# Steward Ministry Database
class Min_Stewards(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_stewards'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_StewardsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_stewards(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_stewards'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_stewardsAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Steward ministry page
# Visitation Ministry Database
class Min_Visitation(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_visitation'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_VisitationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_visitation(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_visitation'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_visitationAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Visitation ministry page
# Praiseworship Ministry Database
class Min_Praiseworship(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    first_name = models.CharField(max_length=200,  null=True)
    middle_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    birthdate = models.DateField(default="1900-01-31")
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = PhoneField(blank=True)
    family_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    home_town = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_joined = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_praiseworship'
        ordering = ['-first_name']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_PraiseworshipAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender', 'birthdate','phone_number',
    'marital_status','email','next_of_kin','next_of_kin_phone','family_name','village','home_town','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_joined','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_praiseworship(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_praiseworship'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_praiseworshipAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Praiseworship ministry page
# Leadership Ministry Database
class Min_Leadership(models.Model):     
    OPTIONS = [
        ('male' , 'Male'),
        ('female','Female'),            
        ]
    CHOICES= [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),  
        ]
    MINI= [     
        ('teach', 'Teaching'), 
        ('pray', 'Intercessor'),    
        ('evan', 'Evangelical'),   
        ('visit', 'Visitation'), 
        ('steward', 'Steward'),
        ('praise', 'Praise and Worship'),   
        ]
    full_name = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=100, choices=OPTIONS, default='male')
    position = models.CharField(max_length=200,  null=True)
    phone_number = PhoneField(blank=True)
    marital_status = models.CharField(max_length=100, choices=CHOICES, default='single')
    email = models.EmailField(blank=True)
    home_address = models.CharField(max_length=255)
    lga_of_origin = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255,  choices=MINI, default='teach')
    date_elected = models.DateField(default="1900-01-31")
    passport = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        db_table='min_leadership'
        ordering = ['-date_elected']
    def __str__(self):
        return self.first_name
# creating in admin page
class Min_LeadershipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'position','phone_number',
    'marital_status','email','home_address','lga_of_origin','state_of_origin',
    'nationality','residential_address','ministry','date_elected','passport')
    def __str__(self):
        return self.fname
# creating event database
class Event_leadership(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_leadership'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
# creating event db in admin page
class Event_leadershipAdmin(admin.ModelAdmin):
    list_display = ('title','anouncer','content','event_img')    
    def __str__(self):
        return self.title
# end of Praiseworship ministry page
# Account database
class Pgrp_Account1(models.Model):     
    CHOICES= [
        ('debit', 'Debit'),
        ('credit', 'Credit'), 
        ]
    MODE= [     
        ('cash', 'Cash'), 
        ('cheque', 'Cheque'),
         ]
    full_name = models.CharField(max_length=200)
    phone_number = PhoneField(blank=True)    
    credit = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    debit = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)       
    mode = models.CharField(max_length=100, choices=MODE, default='cash') 
    date = models.DateField(("Date"), default=datetime.date.today)
    description = models.CharField(max_length=300,default='Default')
    class Meta:
        db_table='pgrp_account1'
        ordering = ['-date']
        def __str__(self):
            return self.full_name
# creating in admin page
class Pgrp_Account1Admin(admin.ModelAdmin):
    list_display = ('full_name','phone_number','description','credit','debit','mode','date')
    def __str__(self):
        return self.full_name

# News database
class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    news_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'news'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','content','news_img','created_on')    
    def __str__(self):
        return self.title

# General Events
class Eventsgeneral(models.Model):
    title = models.CharField(max_length=200, unique=True)
    anouncer = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    event_main_img = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        db_table = 'event_general'
        ordering = ['-created_on']
    def __str__(self):
        return self.title
class EventsgeneralAdmin(admin.ModelAdmin):
    list_display = ('title', 'anouncer','content','event_main_img','created_on')    
    def __str__(self):
        return self.title
