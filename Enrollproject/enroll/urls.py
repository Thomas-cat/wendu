from django.urls import path 
from . import views
app_name ='enroll'

urlpatterns = [
		path('enroll',views.Enroll,name = 'Enroll'),
		path('Download',views.Download,name = 'Download'),
		path('',views.Enroll,name = 'Enroll'),
		]
