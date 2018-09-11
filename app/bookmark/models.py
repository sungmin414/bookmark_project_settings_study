from django.db import models


class Bookmark(models.Model):
    # title 컬럼은 공백 값을 가질수 있고 값이 없을 수도 있다
    title = models.CharField(max_length=100, blank=True, null=True)

    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title

