from django import forms
#from captcha.fields import ReCaptchaField#peter
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        required=True,
        max_length=1000
    )
 #   captcha = ReCaptchaField() #peter
    class Meta:
        model = Comment
        fields = ('text', )
        #fields = ('text', 'captcha')
