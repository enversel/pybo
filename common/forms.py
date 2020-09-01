from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm): # UserCreationForm 클래스를 상속/세 개의 필수속성 생성, 비밀번호가 같은지 검사, email추가
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")
