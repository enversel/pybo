"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pybo.views import base_views

urlpatterns = [
    #path('', include('pybo.urls')),
    path('pybo/', include('pybo.urls')), #pybo/ 로 시작되는 URL이 요청되면 이제 pybo/urls.py 파일의 매핑정보를 읽어서 처리하라는 의미이다.
    path('common/', include('common.urls')), # 쿼리 주소가 common으로 시작하면 여기로 처리한다.
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]

handler404 = 'common.views.page_not_found'