from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, JsonResponse
from django.utils import timezone
from blog.models import Article, Comment  #models.pyからクラスをimportして使えるようにする

# Create your views here.
def index(request):
	if request.method == 'POST':
		article = Article(title=request.POST['title'], body=request.POST['text'])
		article.save()
		context = {
			"article":article,
		}
		return render(request, 'blog/detail.html', context)
	# else:
	# 	context = {
	# 		"articles":Article.objects.order_by('-posted_at')  #ソート：「'-posted_at'」で最新投稿順に並べる
	# 	}
	sort = '-posted_at'  # sortの初期値は最新投稿順
	if('sort' in request.GET):  # 「sort」がURlに含まれているとき
		sort = request.GET['sort']  # sortにURLに表示されている値を代入
	context = {"articles": Article.objects.order_by(sort) }  # Articleモデルにアクセス
	return render(request, 'blog/index.html', context)

def hello(request):
  data = {
		'name': 'alice',
		'weather': 'CLOUDY',
		'weather_detail':['Temperature: 23℃', 'Humidity: 40%', 'Wind: 5m/s'],  # 3個の文字列型の要素を持つリスト
		'isGreatFortune': True,  # bool型なので、「if isGreatFortune」 としたらその処理が実行される
		'fortune': 'Great Fortune!'
  }
  return render(request, 'blog/hello.html', data)

def redirect_test(request):
	return redirect(hello)  # redirectにアクセスすると、helloにリダイレクトする

# 記事詳細画面
def detail(request, article_id):  #引数に記事のid、「article_id」 をとってきてそれぞれ変える
	try:
		article = Article.objects.get(pk=article_id) #「pk=article_id」でこの記事を取得してarticleに格納
	except Article.DoesNotExist:  # 例外のとき（エラー） 記事がないとき
		raise Http404("Article does not exist")  # 記事が存在しないというメッセージ 404⇒ファイルがないときのメッセージ

	# コメントが投稿される⇒POSTのリクエストが発生	
	if request.method == 'POST':  #submitを押したときにPOSTのリクエストが発生、POSTメソッドでアクセスされた場合、Commentオブジェクトを生成し、データベースに保存
		comment = Comment(article=article, text=request.POST['text'], posted_at=timezone.now())  #コメントをフォームの情報からとってくる、とってきたidの記事に紐付け、入力されたテキスト、投稿時間
		comment.save()  #データベースに保存

	context = {  #detail画面に表示したいもの
		"article": article,
		'comments':article.comments.order_by('-posted_at')  #「article.comments.order_by()」の「comments」はCommentクラスの「related_name」で設定したもの。「order_by('-posted_at')」は投稿時間の新しい順
	}
	return render(request, "blog/detail.html", context)

def update(request, article_id):
	# Articleモデルから与えられたIDに対応したオブジェクトを取得
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	# postメソッドで呼び出された時
	if request.method == 'POST':
		article.title = request.POST['title']  # 更新されたtitleを代入
		article.body = request.POST['text']  # 更新されたtextを代入
		article.save()
		return redirect(detail, article_id)  # 詳細画面にリダイレクト
	context = {
		"article": article
	}
	return render(request, "blog/edit.html", context)

def delete(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	article.delete()
	return redirect(index)

def create(request):
	return render(request, "blog/create.html")

def like(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect(detail, article_id)

def api_like(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	result = {
		'id' : article_id,
		'like' : article.like
	}
	return JsonResponse(result)