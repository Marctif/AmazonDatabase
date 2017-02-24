from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^demo/', views.demo, name='demo'),
    #url(r'^signup/', views.signup, name='signup'),
   # url(r'^login/', views.login_view, name='login'),
    #url(r'^logout/', views.logout_view, name='logout'),
    url(r'^catalog/', views.catalog, name='catalog'),
    url(r'^formsetTest/', views.formsetTest, name='formsetTest'),
    url(r'^profile/', views.userprofile, name='profile'),
    url(r'^update_profile/', views.update_profile_temp, name='update_profile'),
    url(r'^(?P<item_id>[0-9]+)', views.ItemDetail, name='detail'),
    url(r'^$', views.home, name='home'),

]