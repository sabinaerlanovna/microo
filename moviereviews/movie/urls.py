from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('news/', include('news.urls')),
]
