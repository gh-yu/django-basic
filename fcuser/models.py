from django.db import models

# Create your models here.

class Fcuser(models.Model): # id는 자동으로 생성됨
    username = models.CharField(max_length=32,
                                verbose_name='사용자명') # verbose_name 설정시 관리자 페이지에서 설정한 문자열로 표시됨
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_time = models.DateTimeField(auto_now_add=True, # auto_now_add : Fcuser가 저장되는(save) 시점에 자동으로 현재 시간이 저장됨
                                            verbose_name='등록시간')
    
    def __str__(self): # 클래스가 문자열로 변환됐을때 어떻게 변활할지 설정 (대표값 설정)
        return self.username
    
    class Meta:
        db_table = 'fastcampus_fcuser' # app들과 이름 구분하기 위해 db_table 이름 별도 설정
        verbose_name= '패스트캠퍼스 사용자' # 장고 어드민에서 모델 클래스의 이름을 기본으로 보여줌, 설정한 문자열로 표시되게 함
        verbose_name_plural = '패스트캠퍼스 사용자' # 기본이 복수형으로 s 붙어서 표시되기 때문에 설정
    
    