from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from fcuser.forms import LoginForm # check_password도 있음
from .models import Fcuser

# Create your views here.
def home(request):
    # session의 user키에 값이 있으면 로그인한 유저로 식별
    # user_id = request.session.get('user')

    # if user_id:
    #     fcuser = Fcuser.objects.get(pk=user_id)
        # return HttpResponse(fcuser.username)

    print(request.session.get('user'))
    print(request.user) # AnonymousUser
    # return HttpResponse('Home!')
    return render(request, "home.html")

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
        
#         res_data = {}
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력해야 합니다.'
#         else:
#             fcuser = Fcuser.objects.get(username=username)
            
#             # 비밀번호 일치, 로그인 처리
#             if check_password(password, fcuser.password):
#                 # 세션
#                 request.session['user'] = fcuser.id # 사용자의 id를 session에 저장
                
#                 print(fcuser.id) # 28
#                 for key, item in request.session.items():
#                     print(key, ":", item)
#                 '''
#                 _auth_user_id : 1
#                 _auth_user_backend : django.contrib.auth.backends.ModelBackend
#                 _auth_user_hash: bc51352bcf05e717cedbc1369d2a1ba094c729dab806d59393bb70815829e49c
#                 user : 28
#                 '''
                    
#                 # 홈으로 가기 위한 redirect
#                 return redirect('/')
#             else:
#                 res_data ['error'] = '비밀번호가 다릅니다.'
            
#         return render(request, 'login.html', res_data)

def login(request):
    status_code = 200
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            # form에서 제공하는 is_valid() 함수 : form이 유효한지 확인  
            # """Return True if the form has no errors, or False otherwise."""
            # form에 에러가 있으면 False, 없으면 True 반환   
            # LoginForm의 clean함수에 작성한 유효성 검사에서 에러 발생하면 False 반환 (password check하고 있음)
            
            
            # 세션에 로그인한 유저 아이디 저장
            request.session['user'] = form.user_id
            
            return redirect('/')
        else:
            status_code = 401 # 401 Unauthorized
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form}, status=status_code)  

def register(request):
    
    if request.method == 'GET': # 페이지 요청 - get
        return render(request, 'register.html') # request객체, 반환하고 싶은 html파일 (같은 경로 아니면 경로 포함)
    elif request.method == 'POST': # 회원가입 요청 - post
        # username = request.POST['username'] # form안의 input태그의 name속성의 값이 key가 됨
        # password = request.POST['password']
        # re_password = request.POST['re-password']
        username = request.POST.get('username', None) # get함수를 이용해 기본값 정하기
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        status_code = 0
        res_data = {} # 딕셔너리 형태로 응답 데이터 보내기
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
            # response.status_code = 400
            status_code = 400 # bad request
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다')
            res_data['error'] = '비밀번호가 다릅니다.'
            status_code = 400 # bad request
        else:
            # 비밀번호 암호화해서 저장하기 (비밀번호가 암호화되지 않은 상태, 즉 평문으로 저장되면 보안에 문제가 됨)
            fcuser = Fcuser(
                username=username,
                password=make_password(password) # 비밀번호 암호화해서 저장
            )
            
            fcuser.save()
            
            res_data['success'] = '회원가입에 성공했습니다.'
            status_code = 201 # created
        
        # return render(request, 'register.html', res_data)
        # return render(request, 'register.html', res_data, status=201)
        # return render(request, 'register.html', res_data, status=status_code)
        
        # res = HttpResponse()
        # res.request = request
        # res.content = res_data 
        
        # (function) render: (request: HttpRequest, template_name: str | Sequence[str], 
        #                     context: Mapping[str, Any] | None = ..., content_type: str | None = ..., 
        #                     status: int | None = ..., using: str | None = ...) -> HttpResponse
        res = render(request=request, template_name='register.html', context=res_data)
        res.status = status_code
        
        return res
        
    
    
    