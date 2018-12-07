from django.conf.urls import url
import views


app_name = "profiles"
urlpatterns = [
    url(r'^$', views.users, name="full_list"),
    url(r'users_lst/', views.UsersListView.as_view(), name='simple_lst'),
    url(r'details/(?P<pk>\d+)/', views.UserDetailView.as_view(), name='user_detail'),
    url(r'new/', views.UsersCreateView.as_view(), name='new'),
]
