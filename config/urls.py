"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include  #blogアプリへURLをとばすためにincludeをつける
from blog import views as blog_views  #blogフォルダのvies.pyをblog_viewsという名前で参照する


urlpatterns = [
    path('admin/', admin.site.urls),  # path(パターン, 関数, name=このパスの名前) nameはなくても良い
    path('', include('blog.urls')),   # include('各アプリのurls.pyへのプロジェクトのルートフォルダ（manage.pyのあるフォルダ）からの相対パス')を指定すると、指定したファイル内に記載したパス情報を読み込む（今回は、blogフォルダ内のurls.py）
]
