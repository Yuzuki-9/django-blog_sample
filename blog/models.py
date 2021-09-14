from django.db import models

# Create your models here.

from django.utils import timezone

# models.Modelというクラスにデータベースとやり取りする機能は備わっているため、やることは「models.Model」を継承して、使いたいデータのモデルを作るだけ

# 記事のモデルを作成
class Article(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  posted_at = models.DateTimeField(default=timezone.now)
  published_at = models.DateTimeField(blank=True, null=True)
  like = models.IntegerField(default=0)

# 継承したクラスにpublishメソッドを追加
# publishメソッドを呼びだすと、published_atに現在時刻が追加されてデータが保存される
  def publish(self):
      self.published_at = timezone.now()
      self.save()

  def __str__(self):
      return self.title

      
class Comment(models.Model):  # コメント機能のクラス
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)  
    # ForeignKey:外部キー、どの記事に対するコメントなのかを表すときに使う、Articleクラス、related_name='comments'でArticleに対するコメントをつける
    # on_deleteで元の記事が消えるとコメントも一気に削除されるようにできている