from django.urls import path 
from . import views
app_name ='enroll'

urlpatterns = [
		path('',views.index,name = 'index'),
		path('enroll',views.Enroll,name = 'Enroll'),
		path('enroll2',views.Enroll2,name = 'Enroll2'),
		path('Download',views.Download,name = 'Download'),
		path('Download2',views.Download2,name = 'Download2'),
		path('weixin/<int:money>/',views.weixin,name = 'weixin'),
		path('zhifubao/<int:money>/',views.zhifubao,name = 'zhifubao'),
		]
