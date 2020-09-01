from django.db import models
from django.contrib.auth.models import User

# 항상 모델 변경 뒤에는 python manage.py makemigrations 와 python manage.py migrate를 해주자

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) #제목. 최대 길이 200
    content = models.TextField()                #내용. 텍스트필드 형식(글자수제한 없음)
    create_date = models.DateTimeField()        #날짜. 데이트타임필드 형식
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가

    def __str__(self):#없어도 됨 // Question.objects.all()할때 id값 말고 제목 그대로를 조회해줌
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #질문, 외부키(다른 모델과의 연결), 삭제시 카스케이드(답변도함께삭제)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):#없어도 됨 // Question.objects.all()할때 id값 말고 제목 그대로를 조회해줌
        return self.content

class Comment(models.Model):   # 댓글
    author = models.ForeignKey(User, on_delete=models.CASCADE) #댓글 작성자
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) # 질문 댓글이거나 답변댓글이거나 둘 중하나기때문에 모두 null True로 해주고 하나에만 채워준다

