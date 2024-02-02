from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    # path('blog/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.my_login, name='my_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
]
