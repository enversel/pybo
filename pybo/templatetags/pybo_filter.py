import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter # 이와 같은 어노테이션 적용시 템플릿에서 해당 함수를 필터('|')로 사용 가능
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
#nl2br 은 줄바꿈 문자를 <br> 로 바꾸어 준다. 이 extension을 사용하지 않을 경우 줄바꿈을 하기 위해서는 공백문자, 즉 스페이스(' ')를 두개 연속으로 입력해야 한다. fenced_code는 위에서 살펴본 소스코드 기능을 사용하기 위해 필요하다.




