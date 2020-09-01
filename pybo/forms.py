from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm): # 일반 폼 모델폼중에서 모델(테이블데이터)저장 가능한 폼인 모델 폼
    class Meta: # 모델폼은 내부 Inner클래스인 Meta가 반드시 필요함. 사용할 모델과 모델의 속성을 적어줌.
        model = Question
        fields = ['subject', 'content'] # 모델을 Question으로 지정해두고 속성은 subject와 content를 가짐

        #widgets = {
        #    'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        #} # 부트스트랩 지정 ## 자동 폼 말고 수동 폼을 위해서 주석처리

        labels = { # 영어로 표시되는 속성 이름들을 한글로 표시
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변을 등록해보세요',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] # 댓글 작성시엔 content 필드만 사용된다.
        labels = {
            'content': '댓글내용',
        }