from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    # slug 페이지나 포스트를 설명하는 핵심단어 집합체, unique(옵션을 추가해 특정 포스트를 검색시 기본 키대신에 사용,
    # allow_unicode(한글처리해줌), help_text(설명해주는 문구로 폼화면에 나타냄)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    # auto_now_add(객체가 생성될때의 시각을 자동기록), auto_now(객체가 데이터베이스에 저장될 때의 시각을 자동 기록)
    create_date = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_date = models.DateTimeField('MODIFY DATE', auto_now=True)

    # 필드 속성 외에 필요한 파라미터가 있으면 Meta 내부 클래스로 정의
    class Meta:
        # 테이블의 별칭을 단수와 복수로 가질수 있으며, 단수 별칠을 post 로 정함
        verbose_name = 'post'
        # 테이블 복수별칭 posts 로 정함
        verbose_name_plural = 'posts'
        # 데이터베이스에 저장되는 테이블의 이름을 my_post 로 지정, 이항목을 생략하면 디폴트는 앱명_모델클래스명을 테이블명으로 지정함
        db_table = 'my_post'
        # modify 컬럼 기준으로 내림차순으로 정렬
        ordering = ('-modify_date')

    def __str__(self):
        return self.title

    # 메소드가 정의된 객체를 지칭하는 URL 을 반환
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_date 컬럼 기준으로 이전 포스트를 반환
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # modify_date 컬럼을 기준으로 다음 포스트를 반환,
    def get_next_post(self):
        return self.get_next_by_modify_date()
