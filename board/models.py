from django.db import models

# Create your models here.

class Board(models.Model): # id는 자동으로 생성됨
    title = models.CharField(max_length=128,
                                verbose_name='제목') 
    
    # TextField 길이 제한 없음
    contents = models.TextField(verbose_name='내용') 
    
    # ForeginKey 설정시 on_delete속성 작성 필수
    # models.CASCADE : writer가 가리키고 있는 사용자가 삭제되면 Board도 같이 삭제됨
    # SET_NULL, SET_DEFAULT, DO_NOTHING
    writer = models.ForeignKey("fcuser.Fcuser", on_delete=models.CASCADE,
                                verbose_name='작성자')
    
    registered_time = models.DateTimeField(auto_now_add=True, # auto_now_add : Fcuser가 저장되는(save) 시점에 자동으로 현재 시간이 저장됨
                                            verbose_name='등록시간')
    
    def __str__(self): # 클래스가 문자열로 변환됐을때 어떻게 변활할지 설정 (대표값 설정)
        return self.title
    
    class Meta:
        db_table = 'fastcampus_board' # app들과 이름 구분하기 위해 db_table 이름 별도 설정
        verbose_name= '패스트캠퍼스 게시글' # 장고 어드민에서 모델 클래스의 이름을 기본으로 보여줌, 설정한 문자열로 표시되게 함
        verbose_name_plural = '패스트캠퍼스 게시글' # 기본이 복수형으로 s 붙어서 표시되기 때문에 설정
    
    