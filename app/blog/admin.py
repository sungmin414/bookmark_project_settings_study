from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # post 객체를 보여줄때 title, modify_date를 화면에 출력하도록 지정
    list_display = ('title', 'modify_date')
    # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    list_filter = ('modify_date', )
    # title, content 컬럼에서 검색하도록 지정
    search_fields = ('title', 'content')
    # title 필드를 사용해 미리 채워지도록 지정
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
