from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import Bookmark


# bookmarkadmin class 는 bookmark 클래스가 admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Bookmark, BookmarkAdmin)
