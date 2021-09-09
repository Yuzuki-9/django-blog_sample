from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),  # path(パターン, 関数, name=このパスの名前) nameはなくても良い
	path('hello', views.hello, name='hello'),
	path('redirect', views.redirect_test, name='redirect_test'),
	path('<int:article_id>/', views.detail, name='detail'),  # 記事の詳細表示 views.pyの関数の引数として値が受け渡される
	path('<int:article_id>/delete', views.delete, name='delete'),  # 記事の削除
	path('<int:article_id>/update', views.update, name='update'),  # 記事の更新
	path('create', views.create, name='create'),
	path('<int:article_id>/like', views.like, name='like'),
	path('api/articles/<int:article_id>/like', views.api_like),
]