from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('email/', user_views.email, name='email'),
    path('pics/', user_views.pics, name='pics'),
    path('pay/', user_views.pay, name='pay'),
    path('savteam/', user_views.savteam, name='savteam'),
    path('see/', user_views.see, name='see'),   
    path('stdent/', user_views.stdent, name='stdent'),
    path('evanmin/', user_views.evanmin, name='evanmin'),
    path('stwdmin/', user_views.stwdmin, name='stwdmin'),
    path('min_teach/', user_views.min_teach, name='min_teach'),
    path('min_evang/', user_views.min_evang, name='min_evang'),
    path('min_pray/', user_views.min_pray, name='min_pray'),
    path('min_stewards/', user_views.min_stewards, name='min_stewards'),
    path('min_visit/', user_views.min_visit, name='min_visit'),
    path('min_praiz/', user_views.min_praiz, name='min_praiz'),
    path('min_lead/', user_views.min_lead, name='min_lead'),
    path('account/', user_views.account, name='account'),
    path('evanpost/', user_views.evanpost, name='evanpost'),
    path('img/', user_views.img, name='img'),
    path('eventeach/', user_views.eventeach, name='eventeach'),
    path('eventgelic/', user_views.eventgelic, name='myapp-eventgelic'),
    path('eventpray/', user_views.eventpray, name='eventpray'),
    path('eventsteward/', user_views.eventsteward, name='eventsteward'),
    path('eventvisit/', user_views.eventvisit, name='eventvisit'),
    path('eventpraiz/', user_views.eventpraiz, name='eventpraiz'),
    path('eventlead/', user_views.eventlead, name='eventlead'),
    path('photo/', user_views.photo, name='photo'),
    path('successView/', user_views.successView, name='successView'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view (template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view (template_name='users/logout.html'), name='logout'),
    path('', include('myapp.urls')),
    # path('paystack',include(('paystack.urls','paystack'),namespace='paystack')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
