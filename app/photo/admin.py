from django.contrib import admin

# Register your models here.
from .models import Photo, Album


# 외래 키로 연결된 Album, Photo 테이블 간에는 1:N 관계가 성립되므로, 앨범 객체를 보여줄 때 객체에 연결된 사진 객체들을 같이 보여줄수 있다.
# 보여주는 형식은 StackedInline 이고, StackedInline(세로로 나열되는 형식) 과 TabularInline(테이블모양처럼 행으로 나열되는 형식) 두가지가 있다.
class PhotoInline(admin.StackedInline):
    # 추가로 보여주는 테이블
    model = Photo
    # 이미 입력된 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수 2
    extra = 2


class AlbumAdmin(admin.ModelAdmin):
    # 앨범 객체를 보여줄때 PhotoInline 클래스에 정의한 사항을 같이 보여줌.
    inlines = [PhotoInline]
    list_display = ('name', 'description')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
