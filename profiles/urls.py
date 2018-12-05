from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.users),
    url(r'users_lst/', views.UsersListView.as_view(), name='simple_lst'),
    url(r'details/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user_detail'),
]
