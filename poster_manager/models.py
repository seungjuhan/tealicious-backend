from django.db import models

"""
TODO LIST
    (1) Poster 클래스를 RESTful 한 API로 만들어서 전송해줄 것.
    (2) image 필드에 들어갈 데이터는 규격화된 사진이 되어야 함, 따라서 사전 처리 작업이 필요 -> python으로 해결할 것.
    instagram 처럼 정사각형 형태로 규격화를 하면 어떨까?
    (3) Google Maps API를 토대로 하여 geo 필드에 들어가야 할 정보 확립

MEMO
"""


"""
class Poster(models.Model):
    image = "포스터 이미지"
    host = "주최자에 관련된 정보. 연합 일일호프의 경우 여러 학과"
            ex) 연세대학교 춤동아리, 서울대학교 전기정보공학부, 한양대 응화생-성신여대 불어불문 연합
    place = "주최 장소"
    geo = "주최 장소의 정확한 지리적 위치"
    time = "일일호프가 열리는 시간"
    content = "특수한 정보: 동아리 공연/홍보, 후원 행사"
    event = "특별한 이벤트에 관련된 정보, 텍스트로 처리할 예정"
            ex) 이름에 "주" 가 들어가면 소주 2000원 할인, 노래를 부르면 안주 무제한 제공!
"""

class Host(models.Model):
    single_host = models.CharField(max_length=50)

class Event(models.Model):
    single_event = models.CharField(max_length=50)

class Image(models.Model):
    single_poster = models.ImageField()

class Poster(models.Model):
    image = models.ManyToManyField(Image)
    place = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=False)
    content = models.TextField()
    # geo =

    hosts = models.ManyToManyField(Host)
    events = models.ManyToManyField(Event)
