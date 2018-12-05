from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.users),
    url(r'users_lst/', views.UsersView.as_view(), name='simple_lst'),
]
