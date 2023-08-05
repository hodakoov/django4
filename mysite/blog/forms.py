from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25) # имя человека, отправляющего пост
    email = forms.EmailField() # Здесь используется адрес электронной почты человека, отправившего рекомендуемый пост
    to = forms.EmailField() # Здесь используется адрес электронной почты получателя, который будет получать электронное письмо с ркомендуемым постом
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm): # При использовании ModelForm мы обращаемся к существующей модели и на ее основе создаем форму
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
