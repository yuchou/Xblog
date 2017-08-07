from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='读者')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='网址')
    text = models.TextField(verbose_name='评论')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
