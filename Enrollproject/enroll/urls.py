from django.urls import path 
from . import views
app_name ='enroll'

urlpatterns = [
		path('',views.index,name = 'index'),
		path('Login',views.Login,name = 'Login'),
		path('FormalEnroll',views.FormalEnroll,name = 'FormalEnroll'),
		#path('enroll',views.Enroll,name = 'Enroll'),
		#path('PreEnroll',views.PreEnroll,name = 'PreEnroll'),
		#path('enroll2',views.Enroll2,name = 'Enroll2'),
		path('Download',views.Download,name = 'Download'),
		path('Download2',views.Download2,name = 'Download2'),
		path('Download3',views.Download3,name = 'Download3'),
		path('Download4',views.Download4,name = 'Download4'),
		path('weixin/<int:money>/',views.weixin,name = 'weixin'),
		path('zhifubao/<int:money>/',views.zhifubao,name = 'zhifubao'),
		]
