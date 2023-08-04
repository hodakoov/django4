from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25) # имя человека, отправляющего пост
    email = forms.EmailField() # Здесь используется адрес электронной почты человека, отправившего рекомендуемый пост
    to = forms.EmailField() # Здесь используется адрес электронной почты получателя, который будет получать электронное письмо с ркомендуемым постом
    comments = forms.CharField(required=False, widget=forms.Textarea)
