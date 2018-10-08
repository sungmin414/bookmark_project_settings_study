from django.shortcuts import render

# Create your views here.
# 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 를 임포트
from django.views.generic import ListView, DetailView
# 테이블 조회를 위해 모델 클래스 임포트
from .models import Bookmark


# BookmarkLV 는 Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰로, ListView 제네릭 뷰를 상속받는다.
# 지정하지 않아도 장고에서 알아서 지정해주는 속성 2가지
# 1. 컨텍스트 변수로 object_list 사용.
# 2. 템플릿 파일을 모델명소문자_list.html 형식의 이름으로 지정.
# list_view
class BookmarkLV(ListView):
    model = Bookmark


# BookmarkDV 는 Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한뷰로, DetailView 제네릭 뷰를 상속받는다.
# 지정하지 않아도 장고에서 알아서 지정해주는 속성 2가지 위와 동일
# detail_view
class BookmarkDV(DetailView):
    model = Bookmark

