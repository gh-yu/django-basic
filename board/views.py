from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from board.forms import BoardForm
from fcuser.models import Fcuser
from .models import Board
# Create your views here.

# pk 자리에는 url 주소로부터 받음
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk) 
    except Board.DoesNotExist: # url에 없는 board id 입력할시
        raise Http404('게시글을 찾을 수 없습니다.')
    
    # board = get_object_or_404(Board, pk=pk) # 없으면 404에러 발생시키는 함수
    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    # 로그인을 하지 않았을 경우
    # 이런건 인터셉터로 구현하면 됨
    if not request.session.get('user'): 
        return redirect('/fcuser/login')
    
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            
            return redirect('/board/list/')
        
    else:
        form = BoardForm()
            
    return render(request, 'board_write.html', {'form':form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get('p', 1)
    # Paginator(self, object_list, per_page, orphans=0,allow_empty_first_page=True)
    # per_page : 한 페이지에 몇개 보여줄 것인지
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page) # get_page() 현재 페이지에 해당하는 boards 반환

    return render(request, 'board_list.html', {'boards': boards})

