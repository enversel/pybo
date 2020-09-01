from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # django.auth를 사용한다면 따로 뷰를 만들 필요 없다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), #로그인/로그아웃과 달리 계정생성은 LoginView, LogoutView와 같은 뷰가 제공되지 않기 때문에 계정생성을 위한 뷰 함수를 직접 만들어야 한다.
]