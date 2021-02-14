from django.contrib import admin
from django.urls import path
from .import views
from users import views as user_views


urlpatterns = [
    path('', views.home, name='myapp-home'),
    path('contact/', views.contact, name='myapp-contact'),
    path('about/', views.about, name='myapp-about'),
    path('history/', views.history, name='myapp-history'),
    path('service/', views.service, name='myapp-service'),
    path('ministry/', views.ministry, name='myapp-ministry'),
    path('evanres/', views.evanres, name='myapp-evanres'),
    path('eventgelic/', user_views.eventgelic, name='eventgelic'),
    path('eventsteward/', user_views.eventsteward, name='eventsteward'),
    path('eventpraiz/', user_views.eventpraiz, name='eventpraiz'),
    path('eventlead/', user_views.eventlead, name='eventlead'),
    path('evanpresult/', views.evanpresult, name='myapp-evanpresult'),
    path('evanmin/', views.evanmin, name='myapp-evanmin'),
    path('eventpray/', user_views.eventpray, name='eventpray'),
    path('testimony/', views.testimony, name='myapp-testimony'),
    path('activities/', views.activities, name='myapp-activities'),
    path('gallery/', views.gallery, name='myapp-gallery'),
    path('news/', views.news, name='myapp-news'),
    path('secretary/', user_views.secretary, name='myapp-secretary'),
    path('donation/', views.donation, name='myapp-donation'),
    path('member/', views.member, name='myapp-member'),
    path('register/', user_views.register, name='myapp-register'),
    path('sirwin/', user_views.sirwin, name='myapp-sirwin'),
    path('prdt/', user_views.prdt, name='myapp-prdt'),   
    path('vistech/', user_views.vistech, name='myapp-vistech'),
    path('train/', user_views.train, name='myapp-train'),
    path('student1/', user_views.student1, name='myapp-student1'),
    path('login/', views.login, name='myapp-login'),
    path('logout/', views.logout, name='myapp-logout'),
    path('leaders/', views.leaders, name='myapp-leaders'),
    path('serviceteam/', views.serviceteam, name ='myapp-serviceteam'),   
]
