from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/', views.userprofile, name='profile'),
    url(r'^update_profile/', views.update_profile_temp, name='update_profile'),
    url(r'^$', views.home, name='home'),
]