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
+ TemplateView를 사용하는 경우는 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해줘야 한다.
    
    ListView, DetailView
    
### model (blog models 안에 로직 설명 정리)
+ reverse() 함수를 사용하여 URL을 구하는 것은 URLconf에 이미 정의된 URL 패턴에서 URL 스트링을 추출하는 방식이므로, 
소스에 URL 스트링을 하드코딩하지 않도록 헤준다.

+ slug 는 페이지나 포스트를 설명하는 핵심 단어의 집합, 슬러그를 URL에 사용함으로써 검색 엔진에서 더빨리 페이지를 찾아주고 검색 엔진의 정확도를 높여줌.

+ SlugField 슬러그는 보통 제목의 단어들을 하이픈으로 연결해 생성하며, URL에서 PK 대신으로 사용되는 경우가 많음
pk를 사용하면 숫자로만 되어 있어 그 내용을 유츄하기 어렵지만 슬러그를 사용하면 보통의 단어들이라서 이해하기 쉬움, 필드의 디폴트 길이는 50이며, 해당 필드에는 인덱스가 디폴트로 생성됨.

`SlugField에 unique 옵션을 추가해 특정 포스트를 검색시 기본 키 대신에 사용, allow_unicode 옵션을 추가하면 한글 처리 가능, help_text는 해당 컬럼을 설명해주는 문구로 폼화면에 나타남`


### templates 

    paginator 객체의 목록, 플러스 당신이 각 페이지에 가지고 싶은 아이템의 수를, 그리고 당신에게 각 페이지에 대한 항목을 액세스하기위한 방법을 제공
    (자세한 내용은 문서 보기)

+ 템플릿에서 URL 추출 함수
> 템플릿 파일에서 URL을 추출하는 문법은 2가지가 있다. `get_absoulte_url()` 메소드를 호출하는 방법과 `{% url %}` 템플릿 태그를 사용하는 방법이 있다.
두가지 모두 URL 패턴명을 이용한다는 점은 동일함. `{% url %}` 태그는 직접 태그의 인자로 URL 패턴명을 사용하는 반면, `get_absolute_url()` 메소드에서는 간접적으로 URL 패턴명을 사용한다.
`get_absolute_url()` 메소드는 모델 클래스의 메소드로 정의되어 있어야 사용 가능하고 이메소드를 정의할때 `reverse() 함수`를 사용하고, `reverse()` 함수 인자로 URL 패턴명을 사용하고 있다.
+ 두문장은 동일한 문장이므로, 어느 문장을 사용해도 무방

       ex)
       <a href='{{ post.get_absolute_url }}'>{{ post.title }}</a>
       <a href='{% url 'blog:post_detail' post.slug %}'>{{ post.title }}</a> 

### 가상환경 사용하기
+ 인터넷에서 다운로드한 라이브러리들이 서로의 버전이 맞지 않아 오동작을 일으키는 것을 방지하기위해서 독립된 파이썬 가상환경을 만들어주는 툴


    설치)python3 -m venv (myvenv)
    가상실행)source myvenv/bin/activate
    가상나오기) deactivate
    현재의 가상 환경에 설치된 패키지 목록을 구함) pip freeze 
    패키지 최신화) pip install -U pip wheel setuptools
    
    
+ https://pypi.python.org/  파이썬용 패키지 검색 사이트
+ https://www.djangopackages.com/   장고용 패키지 검색 사이트
+ 타임존 관리하는 패키지 pytz   
+ 태그기능을 재공하는 오픈소스 패키지 django-tagging 
+ 댓글기능 오픈소스 패키지 django-disqus
+ 이미지 처리하는 패키지 Pillow
    