from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView, TemplateView
from tagging.views import TaggedObjectList
from .models import Post
# search 에 필요한 import
# FormView 클래스형 제네릭 뷰를 임포트, 검색폼으로 사용할 PostSearchForm 폼 클래스 임포트
# 검색 기능에 필요한 Q 클래스 임포트, 단축함수 render 임포트
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


# tag_view
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# search_view (FormView)
# FormView 제네릭 뷰를 상속받아 SearchFormView 클래스형 뷰를 정의, FormView 제네릭뷰는 GET 요청인 경우 폼을 화면에 보여주고 입력을 기다림
# 사용자가 폼에 데이터를 입력하면 POST 요청으로 접수되어 FormView 클래스는 데이터에 대한 유효성을 검사
# 데이터가 유효하면 form_valid() 함수를 실핸한 후에 적절한 URL 로 리다이렉트시키는 기능을 한다.
class SearchFormView(FormView):
    # 폼으로 사용될 클래스 지정
    form_class = PostSearchForm
    # 템플릿 파일 지정
    template_name = 'blog/post_search.html'

    # POST 요청으로 들어온 데이터에 대한 유효성 검사를 실시해 에러가 없으면 form_valid() 메소드를 실행
    def form_valid(self, form):
        # POST 요청의 search_word 파라미터 값을 추출해, schWord 변수에 지정, search_word 파라미터는 PostSearchForm 클래스에서 정의한 필드 id
        schWord = '%s' % self.request.POST['search_word']
        # Q 객체는 filter() 메소드의 매칭 조건을 다양하게 줄 수 있도록 한다. 3개의 조건을 OR 문장으로 연결하고 있다,
        # icontains 연산자는 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사
        # distinct() 메소드는 중복된 객체는 제외
        # Post 테이블의 title, description, content 컬럼에 schWord 가 포함된 레코드를 대소문자 구별없이 검색해, 서로 다른 레코드들만 리스트로 만들어서
        # post_list 변수에 지정해준다.
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        # 템플릿에 넘겨줄 컨텍스트 변수 context 를 사전 형식으로 정의
        context = {}
        # form 객체, 즉 PostSearchForm 객체를 컨텍스트 변수 form 에 지정
        context['form'] = form
        # 검색용 단어 schWord 를 컨텍스트 변수 search_term 에 지정
        context['search_term'] = schWord
        # 검색결과 리스트인 post_list 를 object_list 에 지정
        context['object_list'] = post_list

        # render() 는 템플릿 파일과 컨텍스트 변수를 처리해, 최종적으로 HttpResponse 객체를 반환, form_valid() 함수는 보통 리다이렉트 처리를 위해
        # HttpResponse 객체를 반환하는데 이 render() 함수에 의해 리다이렉트 처리가 되지 않는다.
        return render(self.request, self.template_name, context)
