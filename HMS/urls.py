from django.urls import path
from .views import *
urlpatterns = [
    path('',view_home,name='home'),
    path('about/',view_about,name='about'),
    path('doctor/',view_doctor,name='doctor'),
    path('news/',view_news,name='news'),
    path('appointment/',view_appointment,name='appointment'),
]
