from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름", 
                               error_messages={
                                   'required' : '아이디를 입력해주세요'
                                })
    
     # widget=forms.PasswordInput -> input type이 Password로
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호",
                               error_messages={
                                   'required' : '비밀번호를 입력해주세요'
                                })
   
    
    # 비밀번호 일치 여부 유효성 검사
    def clean(self):
        cleaned_data = super().clean() # 값이 들어있지 않으면 실패
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist as e:
                print(e)
                self.add_error('username', '아이디가 없습니다')
                return
            
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.') 
                # self.add_error : 특정 필드에 에러 넣음
            else:
                self.user_id = fcuser.id
            
                