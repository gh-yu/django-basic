from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        max_length=128, label="제목", 
        error_messages={
            'required' : '제목을 입력해주세요'
        })
    contents = forms.CharField(
        label="내용", widget=forms.Textarea,
        error_messages={
            'required' : '내용을 입력해주세요'
        })
        