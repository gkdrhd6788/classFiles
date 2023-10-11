from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm): 
    content = forms.CharField(
        label='댓글 입력',
        # widget=forms.Textarea,
        )

    class Meta:
        model = Comment
        fields = ('content',)