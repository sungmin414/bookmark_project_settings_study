from django.views.generic import TemplateView


# TemplateView 제네릭 뷰를 상속받아 사용, TemplateView 를 사용하는 경우 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해줘야함!
class HomeView(TemplateView):
    # 프로젝트 첫화면을 보여주기 위한 템플릿 파일을 home.html 로 지정
    template_name = 'home.html'
