from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # widget으로 커스텀하기 위해서는 재정의 필요
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs ={
                'class':'my-title'
            }
        )
    )


    # model 등록(그냥 구조..깊게 생각x)
    class Meta: #메타데이터(데이터에 대한 데이터..기능x)
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)
