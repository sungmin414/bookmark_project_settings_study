# 장고 기본 필드 ImageField, ImageFieldFile 클래스를 임포트
from django.db.models.fields.files import ImageField, ImageFieldFile
# 이미지 처리 라이브러리 PIL.Image 패키지 임포트
from PIL import Image
import os


# 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만들어준다. 예) abc.jpg 면 썸네일 이미지 파일명은 abc.thumb.jpg 로 된다.
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    # 이미지 확장자가 jpeg 또는 jpg 가 아니면
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)