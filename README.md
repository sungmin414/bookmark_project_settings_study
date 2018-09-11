# bookmark project

### 프로젝트 초기설정 및 순서

    take proejct -> proejct폴더명안에서 git init -> .gitignore만들기(맥, 리눅스, 파이썬, 장고, 참플러스, 깃)
    -> pipenv install django -> django-admin startproject (config) -> mv config app (config 파일 app으로 변경)
    -> 파이참환경설정에서 가상환경 경로 지정 -> settings 초기설정( static, media, templates, 한국어,한국시간 변경)
    -> migrate 해서 기본 디비 파일생성해주기 (디비는 사용하고싶은거 사용할수있음) -> startapp (프로젝트명) -> 시작!
    
### 뼈대 조성 순서( 개발자 편한대로 순서바뀌어도 무방)

    model -> admin -> url -> view -> templates 
    
 
### views
+ 함수형 뷰, 클래스형 뷰
+ 개발자가 편한 방식으로 코딩하면 되므로 보통은 하나의 프로젝트에 둘 다 사용하는 경우가 많다.
+ 클래스형 뷰를 사용하는 것이 장고가 제공하는 제네릭 뷰를 사용할 수 있고 재활용 및 확장성 측면에서 유리  
    
    
    ListView, DetailView
    

