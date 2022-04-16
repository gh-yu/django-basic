from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # 어드민 사이트에서 리스트에 표시할 모델의 필드들 명시

admin.site.register(Fcuser, FcuserAdmin)  # 어드민 사이트에 Fcuser, FcuserAdmin 등록
