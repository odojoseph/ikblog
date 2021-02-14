from django.contrib import admin
from . models import profile, Train, TrainAdmin, Student1, Student1Admin, Product, ProductAdmin, Evangelism, EvangelismAdmin, Post, PostAdmin, Eventstwd, EventstwdAdmin, Min_Teaching, Min_TeachingAdmin, Event_teaching, Event_teachingAdmin
from . models import Min_Evangelical,Min_EvangelicalAdmin,Event_evangelical,Event_evangelicalAdmin,Min_Intercessory,Min_IntercessoryAdmin,Event_intercessory,Event_intercessoryAdmin,Min_Stewards,Min_StewardsAdmin,Event_stewards,Event_stewardsAdmin
from . models import Min_Visitation,Min_VisitationAdmin,Event_visitation,Event_visitationAdmin,Min_Praiseworship,Min_PraiseworshipAdmin,Event_praiseworship,Event_praiseworshipAdmin,Min_Leadership,Min_LeadershipAdmin,Event_leadership,Event_leadershipAdmin
from . models import Pgrp_Account1, Pgrp_Account1Admin, News, NewsAdmin, Eventsgeneral, EventsgeneralAdmin

# Register your models here.
admin.site.register(profile)
admin.site.register(Train, TrainAdmin)
admin.site.register(Student1, Student1Admin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Evangelism, EvangelismAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Eventstwd, EventstwdAdmin)
admin.site.register(Min_Teaching, Min_TeachingAdmin)
admin.site.register(Event_teaching, Event_teachingAdmin)
admin.site.register(Min_Evangelical,Min_EvangelicalAdmin)
admin.site.register(Event_evangelical,Event_evangelicalAdmin)
admin.site.register(Min_Intercessory,Min_IntercessoryAdmin)
admin.site.register(Event_intercessory,Event_intercessoryAdmin)
admin.site.register(Min_Stewards,Min_StewardsAdmin)
admin.site.register(Event_stewards,Event_stewardsAdmin)
admin.site.register(Min_Visitation,Min_VisitationAdmin)
admin.site.register(Event_visitation,Event_visitationAdmin)
admin.site.register(Min_Praiseworship,Min_PraiseworshipAdmin)
admin.site.register(Event_praiseworship,Event_praiseworshipAdmin)
admin.site.register(Min_Leadership,Min_LeadershipAdmin)
admin.site.register(Event_leadership,Event_leadershipAdmin)
admin.site.register(Pgrp_Account1,Pgrp_Account1Admin)
admin.site.register(News,NewsAdmin)
admin.site.register(Eventsgeneral,EventsgeneralAdmin)

