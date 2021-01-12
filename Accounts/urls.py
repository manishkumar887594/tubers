from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout_user,name="logout_user"),
    path('dashboard',views.dashboard,name="dashboard"),    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)