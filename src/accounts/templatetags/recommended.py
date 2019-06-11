from django import template
from django.contrib.auth import get_user_model
from accounts.models import UserModel
register = template.Library()

User = get_user_model()

@register.inclusion_tag('snippets/recommended.html')
def recommended(user):
    if isinstance(user , User):
        qs = UserModel.objects.recommended(user , 10)
        return {"recommended" : qs}