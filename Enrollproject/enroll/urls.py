from django.urls import path 
from . import views
app_name ='enroll'

urlpatterns = [
		path('enroll',views.Enroll,name = 'Enroll'),
		path('',views.Enroll,name = 'Enroll'),
		]
