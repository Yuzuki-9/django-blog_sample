from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),  # path(パターン, 関数, name=このパスの名前) nameはなくても良い
	path('hello', views.hello, name='hello'),
	path('redirect', views.redirect_test, name='redirect_test'),
	path('<int:article_id>/', views.detail, name='detail'),  # views.pyの関数の引数として値が受け渡される
	path('<int:article_id>/delete', views.delete, name='delete'),
	path('<int:article_id>/update', views.update, name='update'),
	path('create', views.create, name='create'),
	path('<int:article_id>/like', views.like, name='like'),
	path('api/articles/<int:article_id>/like', views.api_like),
]