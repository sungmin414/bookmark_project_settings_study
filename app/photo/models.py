from django.db import models

# Create your models here.
from django.urls import reverse
# 사진에 대한 원본 이미지와 썸네일 이미지를 모두 저장할 수 있는 필드로  직접만든 커스텀 필드이다. 이커스텀 필드는 fields 에 정의함
from photo.fields import ThumbnailImageField


class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # get_absolute_url() 메소드는 이 메소드가 저으이된 객체를 지칭하는 URL 반환.
    # 메소드 내에서는 장고의 내장 함수인 reverse()를 호출.
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):
    # album 컬럼은 Album 테이블에 연결된 외래 키, 본 사진이 소속된 앨범 객체를 가리키는 reference 역활
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    # image 컬럼 타입은 ThumbnailImageField, 이 필드는 사진에 대한 원본 이미지 및 썸네일 이미지 둘다를 저장할 수있는 필드
    # upload_to 옵션으로 저장할 위치를 지정, photo/%Y/%m의 의미는 MEDIA_ROOT 로 정의된 디렉터리 하위에 사진 년도 월을 포함해
    # 디렉터리를 만들고 그 곳에 업로드하는 사진의 원본 및 썸네일 사진을 저장.
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

