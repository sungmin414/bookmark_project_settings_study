# 장고 기본 필드 ImageField, ImageFieldFile 클래스를 임포트
from django.db.models.fields.files import ImageField, ImageFieldFile
# 이미지 처리 라이브러리 PIL.Image 패키지 임포트
from PIL import Image
import os


# 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만들어준다. 예) abc.jpg 면 썸네일 이미지 파일명은 abc.thumb.jpg 로 된다.
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    # 이미지 확장자가 jpeg 또는 jpg 가 아니면 jpg 로 변경
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


# ImageFieldFile 을 상속받음. 이 클래스는 파일 시스템에 직접 파일을 쓰고 지우는 작업을 한다.
class ThumbnailImageFieldFile(ImageFieldFile):
    # 이미지를 처리하는 필드는 파일의 경로(path)와 URL(url) 속성을 제공해야 한다. 이 함수는 원본 파일의 경로인 path 속성에 추가해,
    # 썸네일의 경로인 thumb_path 속성을 만들어 준다.
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    # 이 함수는 원본 파일의 URL 인 url 속성에 추가해, 썸네일의 URL 인 thumb_url 속성을 만들어 준다.
    def _get_thumb_url(self):
        return _add_thumb(self.url)

    # 파일 시스템에 파일을 저장하고 생성하는 메소드
    def save(self, name, content, save=True):
        # 부모 ImageFieldFile 클래스의 save() 메소드를 호출해 원본 이미지를 저장한다.
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        # 원본 파일로부터 128 x 128 크기의 썸네일 이미지를 만든다.
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        # 가로x세로 비율이 동일한 128x128px 크기의 썸네일 이미지를 만들어준다. 이미지의 색상은 흰색이고 완전 불투명한 이미지
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        # 썸네일과 백그라운드 이미지를 합쳐서 정사각형 모양의 썸네일 이미지를 만듬. 정사각형의 빈공간은 백그라운드 이미지에 의해서 하얀색이 된다.
        background.paste(
            img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        # 합쳐진 최종 이미지를 JPEG 형식으로 파일 시스템의 thumb_path 경로에 저장한다.
        background.save(self.thumb_path, 'JPEG')

    # delete() 메소드 호출 시 원본 이미지뿐만 아니라 썸네일 이미지도 같이 삭제되도록 한다.
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


# ImageField 상속.  이 클래스가 장고 모델 정의에 사용하는 필드 역활.
class ThumbnailImageField(ImageField):
    # 새로운 클래스를 정의할때 그에 상으하는 File 처리 클래스를 attr_class 속성에 지정하는것은 필수.
    attr_class = ThumbnailImageFieldFile

    # 모델의 필드 정의 시 width, height 옵션을 지정할 수 있으며 지정하지 않으면 디폴트로 128px 를 사용
    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        # 부모 ImageField 클래스의 생성자를 호출해 관련 속성들을 초기화한다.
        super(ThumbnailImageField, self).__init__(*args, **kwargs)