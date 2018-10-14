# User 모델의 객체를 생성하기 위해 보여주는 폼, 장고에서 기본으로 제공해줌
from django.contrib.auth.forms import UserCreationForm
# URL 패턴명을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어야함, views.py 모듈이 로딩되고 처리되는 시점에 urls.py 모듈이 로딩되지
# 않을수도 있으므로, reverse() 함수대신 reverse_lazy() 함수를 임포트함.
from django.urls import reverse_lazy
# 편집용뷰 임포트(CreateView)
from django.views.generic import TemplateView, CreateView


# TemplateView 제네릭 뷰를 상속받아 사용, TemplateView 를 사용하는 경우 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해줘야함!
class HomeView(TemplateView):
    # 프로젝트 첫화면을 보여주기 위한 템플릿 파일을 home.html 로 지정
    template_name = 'home.html'


# login view
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    # 장고의 기본 폼사용, 개발자가 직접폼을 작성하고 그폼을 사용해도 된다.
    form_class = UserCreationForm
    # 폼에 입력된 내용에 에러가 없고 테이블 레코드 생성이 완료된 후에 이동할 URL 을 지정
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
